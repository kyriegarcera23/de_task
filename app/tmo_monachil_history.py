from datetime import datetime
import requests
from app import logger
import importlib
import pandas as pd
from database import db_config
from sqlalchemy import MetaData
from sqlalchemy.sql import text
from app import config
import sys
import os
class Tmo_Monachil_History:
    def __init__(self):
        self.generate_create_table_sql = db_config.generate_create_table_sql
        self.load_database_config      = db_config.load_database_config
        self.create_database_engine    = db_config.create_database_engine
        self.db_json                   = os.path.join(os.getcwd(),"app", "config","database.json")
        self.content_type              = config.content_type
        self.token                     = config.token
        self.database_tmo              = config.database_tmo
        self.database_monachil         = config.database_monachil
        self.user_agent                = config.user_agent
        self.url                       = config.url


    def process_and_save_data(self,response, table_name, headers_module):
        logger.info(f"Now extracting {table_name}")
        if response.status_code == 200:
            json_response = response.json()
            if 'Data' in json_response:
                data = json_response['Data']
                df = pd.DataFrame(data)
                logger.info(f"Data retrieved for {table_name}")

                # Load table schema dynamically
                module = importlib.import_module(f'dtype_modules.{table_name}')
                data_dict = getattr(module, table_name)

                # Process date and datetime columns
                for col, dtype in data_dict.items():
                    if dtype in ['DATE', 'DATETIME']:
                        df[col] = df[col].fillna('0000-00-00')
                        df[col] = pd.to_datetime(df[col], errors='coerce')
                        if dtype == 'DATE':
                            df[col] = df[col].dt.date

                # Generate and execute SQL commands
                create_table_sql = self.generate_create_table_sql(table_name, data_dict)
                config = self.load_database_config(self.db_json)
                engine = self.create_database_engine(config)

                # Reflect the database tables
                metadata = MetaData()
                metadata.reflect(bind=engine)

                # df_f = pd.concat([df_hist,df],axis=1)
                # Session = sessionmaker(bind=engine)
                # session = Session()

                with engine.connect() as conn:
                    conn.execute(text(f"DROP TABLE IF EXISTS `{table_name}`"))
                    conn.execute(text(create_table_sql))

                df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
                logger.info(f"Data for {table_name} successfully saved to database.")
            else:
                logger.error("No 'Data' key found in the response.")
                sys.exit("Exiting program due to failed data retrieval.")
        else:
            logger.error(f"Failed to retrieve data: {response.status_code}")
            sys.exit("Exiting program due to failed data retrieval.")

    def run_history(self):
        self.process_tmo_loans_history()
        self.process_tmo_loans_history_monachil()

    def process_tmo_loans_history(self):
        table_name = 'tmo_loans_history'
        start_date = "2021-01-01"
        end_date = datetime.today().date().strftime('%Y-%m-%d')

        url = f"{self.url}/{start_date}/{end_date}"
        headers = {
            "Content-Type": self.content_type,
            "Token": self.token,
            "Database": self.database_tmo,
            "User-Agent": self.user_agent
        }

        response = requests.get(url, headers=headers)
        self.process_and_save_data(response, table_name, headers)

    def process_tmo_loans_history_monachil(self):
        table_name = 'tmo_loans_history_monachil'
        start_date = "2021-01-01"
        end_date = datetime.today().date().strftime('%Y-%m-%d')

        url = f"{self.url}/{start_date}/{end_date}"
        headers = {
            "Content-Type": self.content_type,
            "Token": self.token,
            "Database": self.database_monachil,
            "User-Agent": self.user_agent
        }

        response = requests.get(url, headers=headers)
        self.process_and_save_data(response, table_name, headers)
import os
from app import logger
import importlib
import pandas as pd
from sqlalchemy import MetaData
from sqlalchemy.sql import text
from typing import Dict
from database import db_config
class Excel_files:
    def __init__(self):
        self.generate_create_table_sql = db_config.generate_create_table_sql
        

    def process_date_column(self,df: pd.DataFrame, column: str) -> pd.DataFrame:
        try:
            df[column] = df[column].fillna('0000-00-00')
            df[column] = pd.to_datetime(df[column], errors='coerce')
            df[column] = df[column].dt.date
            return df
        except Exception as e:
            logger.error(f"Error processing date column '{column}': {e}")
            raise

    def process_file(self,df: pd.DataFrame, base_filename: str):
        if base_filename == 'raw_flight_training':
            df.rename(columns={
                'Did borrower transfered school?, if yes, pls indicate name of school': 'School if borrower transfered school',
                "Name or other searching critera used to find borrower's name on FAA website": 'Name or other searching critera used on FAA website'
            }, inplace=True)
            colist = ['Date of Loan Application', 'BIRTHDAY', '0 hours', '40/50 hours', '70/120 hours', '170/180 hours', '200/220 hours', '230 hours', 'Date of Last Funding']
            for c in colist:
                df = self.process_date_column(df, c)

        elif base_filename == 'stg_disbursements':
            df.rename(columns={df.columns[-1]: 'Boolean'}, inplace=True)
            logger.info("The last unnamed column was renamed to 'Boolean'")

        elif base_filename in ['historical_monthly_loan_status', 'disbursements_xero', 'actual_payments_xero']:
            colist = ['Date']
            for c in colist:
                df = self.process_date_column(df, c)

        return df

    def all_files(self,files,engine):
        action = 'append'
        folder = os.getcwd() + "/"
        excel_files = [f for f in os.listdir(folder) if f in files]
        for filename in excel_files:
            base_filename = os.path.splitext(filename)[0]
            table_name = base_filename
            logger.info(f"Importing to {table_name}..")

            try:
                module = importlib.import_module(f'dtype_modules.{base_filename}')
            except ModuleNotFoundError:
                logger.warning(f"Module for {base_filename} not found. Skipping.")
                continue

            try:
                df = pd.read_excel(os.path.join(folder, filename))
            except Exception as e:
                logger.error(f"Error reading {filename}: {e}")
                continue

            df = self.process_file(df, base_filename)

            create_table_sql = self.generate_create_table_sql(table_name, getattr(module, base_filename))

            # Reflect the database tables
            metadata = MetaData()
            metadata.reflect(bind=engine)

            try:
                with engine.connect() as conn:
                    conn.execute(text(f"DROP TABLE IF EXISTS `{table_name}`"))
                    conn.execute(text(create_table_sql))

                df.to_sql(name=table_name, con=engine, if_exists=action, index=False)

                logger.info(f"DataFrame for {table_name} successfully saved as SQL table.")
            except Exception as e:
                logger.error(f"Error writing DataFrame to database for {table_name}: {e}")
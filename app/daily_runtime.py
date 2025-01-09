from datetime import datetime
from app import logger
import os
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from database import db_config
from app import excel_files
from app import tmo_monachil_history

class Import_ToDB():
    def __init__(self):
        self.file = [
            'raw_flight_training.xlsx',
            'stg_disbursements.xlsx',
            'dim_payment_schedule.xlsx'
        ]
        self.db_json = os.path.join(os.getcwd(),"app", "config","database.json")

    def run_task(self):
        current_time = datetime.now().strftime("%H:%M")
        logger.info(f"Running the script at {current_time}...")
        config = db_config.load_database_config(self.db_json)
        engine = db_config.create_database_engine(config)
        logger.info(f"Running file: {self.file}")
        excel_files.Excel_files().all_files(self.file,engine)
        logger.info(f"Running tmo and monachil history")
        tmo_monachil_history.Tmo_Monachil_History().run_history()


        

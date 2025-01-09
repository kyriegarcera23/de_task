from typing import Dict
import json
from app import logger
from sqlalchemy import create_engine

def create_database_engine(config: Dict[str, str]):
    connection_string = f"mysql+pymysql://{config['DB_USERNAME']}:{config['DB_PASSWORD']}@{config['DB_HOST']}/{config['DB_NAME']}"
    return create_engine(connection_string)

def load_database_config(config_path: str = 'database.json') -> Dict[str, str]:
    try:
        with open(config_path) as config_file:
            return json.load(config_file)
    except FileNotFoundError as e:
        logger.error(f"Database configuration file not found: {e}")
        raise

def generate_create_table_sql(table_name: str, columns: Dict[str, str]) -> str:
    col_defs = [f"`{col}` {dtype}" for col, dtype in columns.items()]
    return f"CREATE TABLE IF NOT EXISTS `{table_name}` ({', '.join(col_defs)});"
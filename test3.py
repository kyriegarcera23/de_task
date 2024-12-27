import pandas as pd
from sqlalchemy import create_engine, text
import importlib
import os
import json

folder = os.getcwd() + "\\"
action = 'append'

files = [
    'raw_flight_training.xlsx',
    'stg_flight_training.xlsx',
    'historical_monthly_loan_status.xlsx',
    'disbursements_xero.xlsx',
    'actual_payments_xero.xlsx'
]

def process_date_column(df, column):
    df[column] = df[column].fillna('0000-00-00')
    df[column] = pd.to_datetime(df[column], errors='coerce')
    df[column] = df[column].dt.date
    return df

excel_files = [f for f in os.listdir(folder) if f in files]

# Load database configuration
with open('database.json') as config_file:
    config = json.load(config_file)

# Database connection parameters
host = config['DB_HOST']
username = config['DB_USERNAME']
password = config['DB_PASSWORD']
database_name = config['DB_NAME']

# Construct the connection string
connection_string = f'mysql+pymysql://{username}:{password}@{host}/{database_name}'
engine = create_engine(connection_string)

for filename in excel_files:
    base_filename = os.path.splitext(filename)[0]
    table_name = base_filename

    try:
        module = importlib.import_module(f'dtype_modules.{base_filename}')
    except ModuleNotFoundError:
        print(f"Module for {base_filename} not found. Skipping.")
        continue

    df = pd.read_excel(os.path.join(folder, filename))

    if base_filename == 'raw_flight_training':
        df.rename(columns={
            'Did borrower transfered school?, if yes, pls indicate name of school': 'School if borrower transfered school',
            "Name or other searching critera used to find borrower's name on FAA website": 'Name or other searching critera used on FAA website'
        }, inplace=True)
        colist = ['Date of Loan Application', 'BIRTHDAY', '0 hours', '40/50 hours', '70/120 hours', '170/180 hours', '200/220 hours', '230 hours', 'Date of Last Funding']
        for c in colist:
            df = process_date_column(df, c)

    elif base_filename == 'stg_flight_training':
        colist = ['Flight Training 40/50-hour Milestone', 'Flight Training 70/120-hour Milestone', 'Flight Training 170/180-hour Milestone', 'Flight Training 200/220-hour Milestone']
        for c in colist:
            df = process_date_column(df, c)

    elif base_filename in ['historical_monthly_loan_status', 'disbursements_xero', 'actual_payments_xero']:
        colist = ['Date']
        for c in colist:
            df = process_date_column(df, c)

    columns = getattr(module, base_filename, {})
    create_table_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` (" + ", ".join(
        [f"`{col}` {dtype}" for col, dtype in columns.items()]
    ) + ");"

    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS `{table_name}`"))
        conn.execute(text(create_table_sql))

        if action == 'append':
            df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        elif action == 'replace':
            df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

    print(f"DataFrame for {table_name} successfully saved as SQL table.")

print("All files processed.")
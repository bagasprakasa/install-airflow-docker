import json
import pandas as pd

from sqlalchemy import create_engine
from psycopg2 import connect

def connection_lake(conn_type):
    with open ('dags/script/credentials.json', "r") as cred:
        credential = json.load(cred)
        credential = credential['postgres_lake']

    username = credential['username']
    password = credential['password']
    host = credential['host']
    port = credential['port']
    database = credential['database']
    
    if conn_type == 'engine':
        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(username, password, host, port, database))
        conn_engine = engine.connect()
        print("Connect Engine Postgres_lake")
        return engine, conn_engine
    else:
        conn = connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=database
            )
        cursor = conn.cursor()
        print("Connect Cursor Postgres_lake")
        return conn, cursor

def connection_warehouse(conn_type):
    with open ('dags/script/credentials.json', "r") as cred:
        credential = json.load(cred)
        credential = credential['postgres_warehouse']

    username = credential['username']
    password = credential['password']
    host = credential['host']
    port = credential['port']
    database = credential['database']
    
    if conn_type == 'engine':
        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(username, password, host, port, database))
        conn_engine = engine.connect()
        print("Connect Engine Postgres_warehouse")
        return engine, conn_engine
    else:
        conn = connect(
            user=username,
            password=password,
            host=host,
            port=port,
            database=database
            )
        cursor = conn.cursor()
        print("Connect Cursor Postgres_warehouse")
        return conn, cursor

def insert_raw_to_warehouse():
    engine, engine_conn = connection_lake(conn_type='engine')
    data = pd.read_sql(sql='sales', con=engine)
    engine.dispose()

    engine, engine_conn = connection_warehouse(conn_type='engine')
    data.to_sql('sales', con=engine, index=False, if_exists='replace')
    engine.dispose()
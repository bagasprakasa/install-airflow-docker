import datetime

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python_operator import PythonOperator

from script import main


with DAG(
    dag_id="postgres2postgres_manual",
    start_date=datetime.datetime(2022, 8, 14),
    schedule_interval=None,
    catchup=False,
) as dag:
    create_lake_table = PostgresOperator(
        task_id="create_lake_table",
        postgres_conn_id='POSTGRES_DATALAKE',
        sql="./sql/datalake-script.sql",
    )

    create_warehouse_table = PostgresOperator(
        task_id="create_warehouse_table",
        postgres_conn_id='POSTGRES_DATAWAREHOUSE',
        sql="./sql/datawarehouse-script.sql",
    )

    # populate table in data warehouse
    insert_raw_to_warehouse = PythonOperator(
        task_id="insert_to_warehouse",
        python_callable=main.insert_raw_to_warehouse
    )

    create_lake_table >> create_warehouse_table >> insert_raw_to_warehouse
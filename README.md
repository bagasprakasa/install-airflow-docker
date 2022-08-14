# Install Airflow on Docker and Create first DAG
## Prerequisite:
Before you running this installation, make sure you have Docker and Docker Compose on your Linux/Unix machine.

## Airflow Setup
In this Airflow installation, you will install Airflow 2.2.0 and some services to support Airflow such as : 
1. Databases: 
    - First Postgresql image as datalake 
    - Second Postgresql image as datawarehouse

2. Airflow Setup:
    - Airflow Postgresql as repo
    - Redis
    - Airflow webserver, scheduler, worker
    - Flower

## Running Setup
1. To run this installation, you must config the credential inside the .env file. 
For example:
```
DB_NAME=dev
USER_NAME=user_dev
USER_PASSWORD=pass2022!
AIRFLOW_CONN_POSTGRES_DATALAKE=postgresql://user_dev:pass2022!@172.17.0.1:5433/dev
AIRFLOW_CONN_POSTGRES_DATAWAREHOUSE=postgresql://user_dev:pass2022!@172.17.0.1:5434/dev
```

2. Change the credential inside the ``credentials.json`` file in this folder ``dags/script/``.
For example:
```
{
    "postgres_lake": {
        "host":"172.17.0.1",
        "port":"5433",
        "database":"dev",
        "username":"user_dev",
        "password":"pass2022!"
    },
    "postgres_warehouse": {
        "host":"172.17.0.1",
        "port":"5434",
        "database":"dev",
        "username":"user_dev",
        "password":"pass2022!"
    }
}
```

2. Then, open your terminal and enter to installation folder where you can find docker-compose.yaml file.
3. Run this command to turn on your installation. It will download and install some docker images for 5-20 minutes based on your internet connection.
```
docker-compose up
```
4. After installation finish, open your browser and type this URL :
```
localhost:5584
```
5. You need to insert username and password for Airflow for the first time login, please use this credential below.
```
username : airflow
password : airflow
```
6. You will see a DAG named ``postgres2postgres_manual`` and you can trigger this DAG using play button in the right page.
7. Click on ``postgres2postgres_manual`` DAG and you will see dag tree and wait for the process until finish.
8. If all process success, you can use your Postgresql client and enter to ``postgres_warehouse`` database to see table that already created and inserted.
9. To turn off Airflow installation, you can use this command on your terminal.
```
docker-compose down
```

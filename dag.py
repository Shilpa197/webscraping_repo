from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from scrape_folder.scrape import scrape #Pipeline file is imported
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import psycopg2

args = {
    'owner': 'Shilpa Sivadas',
    'start_date': days_ago(1) # make start date in the past
}

dag = DAG(
    dag_id='scrape_py',
    default_args=args,
    schedule_interval='@daily' # make this workflow happen every day
)

with dag:
    ws = PythonOperator(
        task_id='scrapefunction',
        python_callable=scrape, #scraping function is called
      
    )

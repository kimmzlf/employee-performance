# import library
import pandas as pd
import datetime as dt
import psycopg2
from airflow import DAG
from elasticsearch import Elasticsearch
from airflow.operators.python_operator import PythonOperator

# Ambil data dari postgresql
def fetchData():

    # Sesuaikan konfigurasi dengan database
    db_user = "airflow"
    db_pass = "airflow"
    db_host = "postgres"
    db_port = "5432"
    db_name = "airflow"

    # Connect ke database
    connection = psycopg2.connect(
        user = db_user,
        password = db_pass,
        host = db_host,
        port = db_port,
        database = db_name
    )

    # Ambil data lalu simpan ke dalam variabel
    df = pd.read_sql("SELECT * FROM table_m3", connection)
    df.to_csv('/opt/airflow/dags/data_raw.csv', index=False)

# Clean data
def cleanData():
    df = pd.read_csv('/opt/airflow/dags/data_raw.csv')
    # Hapus duplikat
    df = df.drop_duplicates() 
    # Membuat nama kolom menjadi huruf kecil semua, menghapus whitespace dan simbol yang tidak diperlukan
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(' ', '_', regex=True)
        .str.replace(r'[^\w\s]', '', regex=True)
        )
    
    # Handle missing values dengan membagi menjadi kolom numerikal dan kategorikal 
    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = df.select_dtypes(include=['object', 'bool']).columns
    # Handle dengan mengisi menggunakan median
    for col in num_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].median())

    # Handle dengan mengisi menggunakan modus        
    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])
    df.to_csv('/opt/airflow/dags/data_clean.csv', index=False)

# Kirim data ke Elasticsearch
def sendES():
    # Koneksi es dengan port yang terhubung
    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv('/opt/airflow/dags/data_clean.csv')
    # kirim data 
    for i,r in df.iterrows():
        doc=r.to_json()
        res=es.index(index='datafinal', doc_type="doc", body=doc)
        print(res)

# Konfigurasi DAG
default_args = {
    'owner' : 'kim',
    'start_date': dt.datetime(2026,1,1),
    'retries': 1, 
    'retries_delay':dt.timedelta(minutes=10)
}

# Definisi DAG
with DAG('Project-M3',
         default_args=default_args,
         schedule_interval = '0 0 * * *'
         )as dag:
    
    # Definisi task 
    fetch_data = PythonOperator(task_id= 'fetch_data',
                                python_callable = fetchData)
    clean_data = PythonOperator(task_id= 'clean_data',
                                python_callable = cleanData)
    send_es = PythonOperator(task_id= 'send_es',
                                python_callable = sendES)

# Task Dependency    
fetch_data >> clean_data >> send_es
    

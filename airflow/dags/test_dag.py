from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow import DAG, AirflowException
from airflow.utils.dates import days_ago


def crap():
    print("I am POWER!")


default_args = {
    'owner': 'Test',
    'depends_on_past': False
}

dag = DAG(
    'crap',
    default_args=default_args,
    start_date=days_ago(0)
)
task1 = PythonOperator(
    task_id="CRAP",
    python_callable=crap,
    dag=dag
)

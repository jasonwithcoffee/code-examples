from google.cloud import bigquery
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'/Users/jason/GCP/data-project-21a2132a2e60.json'

query = """
select *
from `bigquery-public-data.baseball.schedules`
"""

bq_client = bigquery.Client()
df = bq_client.query(query).result().to_dataframe()

df.head()
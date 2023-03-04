import psycopg2
import pandas as pd
import numpy as np

# Connect to the database
conn = psycopg2.connect(host='localhost', port=5432, user='username', password='password', database='dbname')

# Retrieve the scraped data
query = "SELECT name, marketcap, price, 24h volume FROM crypto"
df = pd.read_sql(query, conn)

# Clean the data
df.drop_duplicates(inplace=True)  # remove duplicates
df = df[df['last_updated'].dt.year >= 2022]  # filter by date range
df['name'] = df['name'].str.upper()  # convert to uppercase
df['marketcap'].fillna(df['marketcap'].median(), inplace=True)  # substitute missing market caps with the median
df['price'].fillna(df['price'].median(), inplace=True)  # substitute missing prices with the median


# Save the cleaned data to a new table in the database
cleaned_table_name = 'cleaned_crypto'
df.to_sql(cleaned_table_name, conn, if_exists='replace', index=False)

# Close the database connection
conn.close()


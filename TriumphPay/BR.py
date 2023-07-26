# pylint: disable=E0401
import csv
import pandas as pd

df = pd.read_csv('BillingReport.csv')
print(df)

Uploaded_Date = df['Uploaded Date'] > '04/26/23'
print(Uploaded_Date)
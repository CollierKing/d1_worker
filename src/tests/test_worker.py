import pandas as pd
import requests
import json

url = "http://127.0.0.1:8787/api/query"
# url = "http://127.0.0.1:8787/api/beverages"
# url = "https://my-project.chartclass.workers.dev/"
headers = {'Content-Type': 'application/json', }

sql = "SELECT * FROM Customers"

# CustomerID
# CompanyName
# ContactName

# todo:
df = \
    pd.DataFrame({
        "CustomerID": [99, 102, 139],
        "CompanyName": ["ACME Co", "Lentil Labs", "Beyond Biz"],
        "ContactName": ["Burt", "Dave", "Mick"]
    })
#
# sql = f'''
# INSERT INTO 'Customers'
# SELECT
#     87 AS 'CustomerID',
#     'Corn Cob Enterprises' AS 'CompanyName',
#     'William' AS 'ContactName'
# UNION ALL
# SELECT
#     88 AS 'CustomerID',
#     'Ski Bum Central' AS 'CompanyName',
#     'Skitch' AS 'ContactName'
# '''.replace("\n", " ")

r = \
    requests.post(
        url=url,
        data={"sql": sql},
    )

print(r.json())

# select from company to test
sql = "SELECT * FROM Customers"
r = \
    requests.post(
        url=url,
        data={"sql": sql},
    )

print(r.json())

df = pd.DataFrame.from_records(r.json())

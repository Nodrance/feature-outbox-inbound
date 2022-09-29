#coded by an intern, forgive me

from re import X
from agilitek_utilities import database
import pandas as pd 
import os



sqlserv = database.database.DatabaseClient({
        "driver":os.environ.get("DRIVER"),
        "server":os.environ.get("SERVER"),
        "database":os.environ.get("DATABASE"),
        "uid":os.environ.get("UID"),
        "pwd":os.environ.get("PWD")
    })

def gettable(table):
    qresult = sqlserv.execute_query(f"SELECT TOP 30 * FROM {table}")
    columns = sqlserv.execute_query(
        f"""SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = '{table}'
        ORDER BY ORDINAL_POSITION""")
    print(columns)
    print("Download complete")
    data = []
    for row in qresult:
        data.append([elem for elem in row])
    db = pd.DataFrame(data, columns=[c for c in columns])
    return db

todo = ["itemSeat","item","customerOrder","orderNote"]
for table in todo:
    print(f"Downloading and processing {table}")
    gettable(table).to_json(f"output\\{table}.json",orient="records",indent=4)
    print("Processing complete")
    """
    #Get old table from cloud
    newtab = gettable(table)
    



"""
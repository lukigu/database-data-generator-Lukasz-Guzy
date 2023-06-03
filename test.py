import cx_Oracle
import datetime
from datetime import timedelta
import random
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle_cx")
rows = 0

start_date = datetime.date(2021, 1, 1)

print(start_date + timedelta(days=1))

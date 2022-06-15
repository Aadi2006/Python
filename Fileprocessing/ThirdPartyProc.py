import time
import os
import pandas

while True:
    if os.path.exists("files/temps.csv"):
        data = pandas.read_csv("files/temps.csv")
        print(data.mean()["st1"])
        print(f'{data.mean()["st2"]}\n')
    else:
        print("File does not exist")
    time.sleep(5)
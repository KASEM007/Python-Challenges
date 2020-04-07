import sqlite3
import time
import datetime
import random


conn = sqlite3.connect("happen.db")
c = conn.cursor()


def create_table():
    c.execute(
        "CREATE TABLE IF NOT EXISTS stufftoplot(unix REAL, datestamp TEXT, value REAL)"
    )


def data_entry():
    c.execute("INSERT INTO stufftoplo VALUES(145123542, '2016-01-01', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime._fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%s"))
    keyword = "python"
    value = random.randrange(0, 10)
    c.execute(
        "INSERT INTO stufftoplo (unix, datestamp, keyword, value)VALUES(?,?,?,?)",
        (unix, date, keyword, value),
    )

    conn.commit()


# create_table()
# data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close
conn.close()


create_table()
data_entry()

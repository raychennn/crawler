import requests
import pandas as pd
from pandas import DataFrame
import mysql.connector
from mysql.connector import errorcode

# Connecting to MySQL

DB_NAME = 'crypto'

try:
    cnx = mysql.connector.connect(user='root', password = 'some9001', host = '127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print('successfully connnect to MySQL server')

cursor = cnx.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# Creating Table

TABLES = {}
TABLES['block'] = (
    "CREATE TABLE `block` ("
    "  `block` varchar(20) NOT NULL,"
    "  `rise_count` int NOT NULL,"
    "  `drop_count` int NOT NULL,"
    "  `total_coin` int NOT NULL,"
    "  PRIMARY KEY (`block`)"
    ") ENGINE=InnoDB") #storage engine

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

# Inserting Data

add_block = ("INSERT IGNORE INTO block "
               "(block, rise_count, drop_count, total_coin) "
               "VALUES (%s, %s, %s, %s)"
               'block','rise_count','drop_count', 'total_coin')

block = []
rise_count = []
drop_count = []
total_coin = []

r = requests.get('https://shrtm.nu/ZEYu')
new = r.json()
data = new['data']

for table in data:
    if 'name' in table:
        name = table.get('name')
        block.append(name)

    if 'rise_count' in table:
        num1 = table.get('rise_count') 
        rise_count.append(num1)

    if 'drop_count' in table:
        num2 = table.get('drop_count') 
        drop_count.append(num2)

    if 'total_coin' in table:
        num3 = table.get('total_coin')
        total_coin.append(num3)
        print(block)
        print(rise_count)
        print(drop_count)
        print(total_coin)
        data_block = (block, rise_count,drop_count,total_coin)
        # Insert new block
        cursor.executemany(add_block, data_block)

print('closing')

# Make sure data is committed to the database
cnx.commit()

print('closing')
cursor.close()
cnx.close()






    




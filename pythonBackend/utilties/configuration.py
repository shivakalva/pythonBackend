import configparser
import mysql
from mysql.connector import Error

def getconfig():
    config = configparser.ConfigParser()
    config.read("utilties/properties.ini")
    print(config)
    return config

def getpwd():
    return "Pumba@291"

def getconnection():
    try:
        connection = mysql.connector.connect(**connectconfig)
        if connection.isconnected():
            print("connection is succesfull")
            return connection
    except Error as e:
        print(e)

connectconfig = {
    'user': getconfig()['SQL']['user'],
    'password': getconfig()['SQL']['password'],
    'host': getconfig()['SQL']['host'],
    'database': getconfig()['SQL']['database']
}

def getQuery(query):
    connection = getconnection()
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    connection.close()
    return row



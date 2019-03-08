#!/usr/bin/env python3

import psycopg2

question1 = ("What are the three most popular articles of all time?")
query1 = (
    "select * from articles;"
)

question2 = ("Who are the most popular article authors of all time?")

question3 = ("On which days did more than 1% of requests lead to errors?")

def connect(database="news"):
    try:
        connection = psycopg2.connect("dbname={}".format(database))
        cursor = connection.cursor()
        print ("Database connection successful...")
        return connection, cursor
    except (Exception, psycopg2.Error) as error:
        print ("Database connection failed: ", error)
        connection.close()

def results(query):
    connection, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    connection.close()

def print_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print ("Index: ", index, str(results[1]))

if __name__ == '__main__':
    popular_articles = results(query1), question1
    print_results(popular_articles)

#! /usr/bin/env python
# Udacity Full Stack Nanodegree Project: Logs Analysis
import time
import webbrowser
import psycopg2
import os
import sys
import datetime

now = datetime.datetime.now()


input_variable = raw_input ("Enter your file name : ")
print (input_variable + ".txt")

input_song = raw_input ("enter your song : ")

DB_NAME = "news"

FILENAME = input_variable + ".txt"

QUESTIONS = [
    '1. What are the most popular three articles in are list?',
    '2. Who are 3 top authors?',
    '3. On which days did more than 1% of requests result in errors?']


# Queries to be executed
DATA = [
    # 1 Top articles
    ('''
    SELECT articles.title, count(*) as num
    FROM articles inner join log on log.path
    like concat('%', articles.slug, '%')
    where log.status like '%200%' group by
    articles.title, log.path order by num desc limit 3;
    '''),
    # 2 Top authors
    ('''
    SELECT authors.name, count(*) as num from articles inner
    join authors on articles.author = authors.id inner join log
    on log.path like concat('%', articles.slug, '%') where
    log.status like '%200%' group by authors.name order by 
    num desc;
    '''),
    # 3 Day of errors
    ('''
    SELECT data.day, ROUND((100.0*data.err/data.total),2) 
    as error FROM (SELECT date_trunc('day', time) as day,
    count(id) as total,
    sum(case when status!='200 OK' then 1 else 0 end) as err
    FROM log
    GROUP BY day) as data
    WHERE ROUND((100.0*data.err/data.total),3) >1;
    ''')]

def fire_query(mommyAndDaddy):

    try: 
        db = psycopg2.connect(database=DB_NAME)
        c = db.cursor()
        results_in_arrays = []

        for i in mommyAndDaddy:
            c.execute(i)
            results_in_arrays.append(c.fetchall())
        db.close()

        return results_in_arrays
    except psycopg2.Error as e:
        print e
        sys.exit(1)

def formingquerynow(babyboy):
    resultsS = ''
    for pounds in babyboy:
        resultsS += ('* {i[0]} with {i[1]} views\n').format(i=pounds)
    return resultsS

def formingqueryagain(babyboy):
    resultsS = ''
    for pounds in babyboy:
        resultsS += ("* {i[0]:%B'/'%d'/'%Y'/'} we \
        encountered {i[1]:}% errors\n").format(i=pounds)
    return resultsS


def format_list(babyboy):
    result = ''
    for i in range(len(QUESTIONS)):
        result += QUESTIONS[i] + '\n'

        if(i != 2):
            result += formingquerynow(babyboy[i]) + '\n\n'
        else:
            result += formingqueryagain(babyboy[i]) + '\n\n'

    return result

def tim():
    p = now.strftime("%Y-%m-%d %H:%M")
    print 'You last searched for these entries on {}.'.format(p)
    return
def welcome():
    print "Hello......" 
    time.sleep(1)
    "I will search for your files"
    time.sleep(2)
    print "Let me get some music for you while you wait...."
    print "playing  " + input_song
    webbrowser.open("https://www.youtube.com/watch?v=D93PBlwBp8s")
    time.sleep(1)


def sendout(text):
    f = open('./' + FILENAME, 'w')
    f.write(text)
    f.close()

if __name__ == "__main__":
    welcome()
    babyboy = fire_query(DATA)
    display = format_list(babyboy)
    print(display)
    sendout(display)
    print '{} successfully generated. {}'.format(FILENAME,tim())




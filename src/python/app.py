#! /usr/bin/env python
import psycopg2


class DBConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='news' user='postgresql' host='postgresql' port='5432'"
            )
            self.connection.autocommit = True
            print("Connected to PostgreSQL database.")
            print()
        except BaseException as e:
            print("Failed to connect to the PostgreSQL database.")
            print(e.message)

    def get_cursor(self):
        return self.connection.cursor()

    def close_connection(self):
        self.connection.close()


def top_three_articles_by_popularity(cursor):
    """Print out the top three articles by popularity."""
    query = """
            SELECT articles.title,
                   count(*)
            FROM   log,
                   articles
            WHERE  log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY count(*) DESC
            LIMIT 3;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    print('=======================================')
    print('Three most popular articles of all time')

    for result in results:
        print('"{title}" - {count} views'
              .format(title=result[0], count=result[1]))
    print()


def most_popular_authors(cursor):
    """Print out the most popular authors.
    Args:
        db_cursor: psycopg2 PostgreSQL database cursor object.
    """
    query = """
            SELECT authors.name,
                   count(*)
            FROM   log,
                   articles,
                   authors
            WHERE  log.path = '/article/' || articles.slug
              AND articles.author = authors.id
            GROUP BY authors.name
            ORDER BY count(*) DESC;
    """
    cursor.execute(query)
    results = cursor.fetchall()

    print('================================')
    print('Most popular authors of all time')

    for result in results:
        print('{author} - {count} views'
              .format(author=result[0], count=result[1]))
    print()


def days_greater_than_1pc_errors(db_cursor):
    """Print out days where the error rate > 1%."""

    query = """
            WITH num_requests AS (
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), num_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT num_requests.day,
                  num_errors.count::float / num_requests.count::float * 100
                  AS error_pc
                FROM num_requests, num_errors
                WHERE num_requests.day = num_errors.day
              )
            SELECT * FROM error_rate WHERE error_pc > 1;
    """
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('Days > 1% errors')
    print('================================')

    for result in results:
        print("{date:%B %d, %Y} - {error_rate:.1f}% errors".format(
            date=result[0],
            error_rate=result[1]))
    print()


if __name__ == "__main__":
    connection = DBConnection()
    cursor = connection.get_cursor()

    if cursor:
        top_three_articles_by_popularity(cursor)
        most_popular_authors(cursor)
        days_greater_than_1pc_errors(cursor)

    connection.close_connection()

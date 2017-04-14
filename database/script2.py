import psycopg2


"""
Script using postgreSql database
"""
conn = psycopg2.connect("dbname='postgres' user='admin' password='password' host='localhost'")

def create_table():
  conn = psycopg2.connect("dbname='postgres' user='admin' password='password' host='localhost'")
  cur = conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
  conn.commit()
  conn.close()


def insert(item, quantity, price):
  conn = psycopg2.connect("dbname='postgres' user='admin' password='password' host='localhost'")
  cur = conn.cursor()
  cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
  conn.commit()
  conn.close()


def view():
  conn = psycopg2.connect("dbname='postgres' user='admin' password='password' host='localhost'")
  cur = conn.cursor()
  cur.execute("SELECT * FROM store")
  rows = cur.fetchall()
  conn.close()
  return rows


def delete(item):
  conn = psycopg2.connect("dbname='postgres' user='admin' password='password' host='localhost'")
  cur = conn.cursor()
  cur.execute("DELETE FROM store WHERE item=%s", (item,))
  conn.commit()
  conn.close()



def update(quantity, price, item):
  conn = psycopg2.connect("dbname='postgres' user='admin' password='password' host='localhost'")
  cur = conn.cursor()
  cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))
  conn.commit()
  conn.close()

create_table()

insert('coffe cup', 23, 10)
insert('plates', 25, 5)

print(view())

delete('plates')

print(view())

update(500, 1000, 'coffe cup')

print(view())
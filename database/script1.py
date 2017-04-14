import sqlite3


"""
Script using sqlite3 database
"""


def create_table():
  conn = sqlite3.connect('lite.db')
  cur = conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
  conn.commit()
  conn.close()


def insert(item, quantity, price):
  conn = sqlite3.connect('lite.db')
  cur = conn.cursor()
  cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
  conn.commit()
  conn.close()


def view():
  conn = sqlite3.connect('lite.db')
  cur = conn.cursor()
  cur.execute("SELECT * FROM store")
  rows = cur.fetchall()
  conn.close()
  return rows


def delete(item):
  conn = sqlite3.connect('lite.db')
  cur = conn.cursor()
  cur.execute("DELETE FROM store WHERE item=?", (item,))
  conn.commit()
  conn.close()



def update(quantity, price, item):
  conn = sqlite3.connect('lite.db')
  cur = conn.cursor()
  cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
  conn.commit()
  conn.close()


insert('coffe cup', 23, 10)
insert('plates', 25, 5)

print(view())

delete('plates')

print(view())

update(500, 1000, 'coffe cup')

print(view())
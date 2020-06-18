import sqlite3

conn = sqlite3.connect('mytodos1.db')
c = conn.cursor()
c.execute('CREATE TABLE todos1 (todo text)')
conn.commit()
conn.close()


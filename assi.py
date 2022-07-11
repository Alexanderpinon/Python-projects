
import sqlite3

conn = sqlite3.connect('assi.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
            col_txt TEXT)")
    conn.commit()


conn = sqlite3.connect('assi.db')


filelist = ('information.docx', 'Hello.txt', 'myImage.png'\
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

for x in filelist:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_data (col_txt) VALUES (?)", (x,))
            print(x)
conn.close()


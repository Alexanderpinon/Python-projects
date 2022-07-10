
import sqlite3

conn = sqlite3.connect('assi.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_txt TEXT, \
            col_docx TEXT, \
            col_png TEXT, \
            col_mpg TEXT, \
            col_pdf TEXT, \
            col_jpg TEXT  \
            )")
    conn.commit()
conn.close()

conn = sqlite3.connect('assi.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_data(col_txt) VALUES (?)", \
                ('Hello.txt','World.txt'))
    cur.execute("INSERT INTO tbl_data(col_docx) VALUES (?)", \
                ('information.docx'))
    cur.execute("INSERT INTO tbl_data(col_png) VALUES (?)", \
                ('myImage.png'))
   cur.execute("INSERT INTO tbl_data(col_mpg) VALUES (?)", \
                ('myMovie.mpg'))
    cur.execute("INSERT INTO tbl_data(col_pdf) VALUES (?)", \
                ('data.pdf'))
    cur.execute("INSERT INTO tbl_data(col_jpg) VALUES (?)", \
                ('myPhoto.jpg'))

    conn.commit()
conn.close()

conn = sqlite3.connect('assi.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_txt WHERE col_txt = '.txt'")
    varData = cur.fetchall()
    for item in varData:
        msg = "Data: {}".format(item[0])
    print(msg)

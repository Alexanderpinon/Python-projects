
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


conn = sqlite3.connect('assi.db')


filelist_tuple = ("Hello.txt", "World.txt")


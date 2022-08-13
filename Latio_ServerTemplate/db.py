import sqlite3

con = sqlite3.connect("testlost.db")

cur = con.cursor()

creator = "CREATE TABLE ark(Id text,name text);"
inserter = "INSERT INTO ark Values('%s','%s');"

def AddPlayer(id ,text):
    info = inserter % (id,text)
    cur.execute(info)

def CommitSql():
    con.commit()

def ExecuteSql():
    cur.execute('SELECT * FROM ark')
    for row in cur:
        print(row)

def CloseSql():
    con.close()

AddPlayer("후후","??")
CommitSql()

ExecuteSql()

CloseSql()
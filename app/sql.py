import MySQLdb

'''
增加
删除
改数据
查数据
'''
account = {"host": "localhost", "username": "root", "password": "root"}

database = "test"

def str_conv(value):
    if type(value)is not str:
        return str(value)
    else:
        return "\""+value+"\""

# 创建数据库变量，实际上是登录
# account: 账号信息，格式如下：
# {"host": "localhost", "username": "root", "password": "root"}
# 返回：一个已经登录的数据指针
def create(account):
    try:
        db = MySQLdb.connect(
            account["host"],
            account["username"],
            account["password"],
            "sys",
            charset="utf8",
        )
    except MySQLdb._exceptions.OperationalError:
        return False
    return db

# 显示某一表的属性
# db：数据库指针
# database：数据库名称，字符型
# table：表名称，字符型
# 返回：一个元组['属性名称1','属性名称2']
def showMeta(db, database, table):
    cursor = db.cursor()
    cursor.execute("use %s"% (database))
    cursor.execute("desc %s"%(table))
    res = []
    data = cursor.fetchall()
    for i in data:
        res.append(i[0])
    return res

# 向某一个表中插入一条数据
# db：数据库指针，由create()函数创建
# database：数据库名称，字符型
# table：表名称，字符型
# data：要插入的属性和数据值
# data：是一个元组，是你要插入的值，数量必须与表对应
# 如果data中的元素是str类型的，则它会被加""后加入到sql语句中
def insert(db, database, table, data):
    cursor = db.cursor()
    cursor.execute("use %s"%(database))
    sql = "insert into %s values("%(table)
    for  i in range(len(data)):
        if i != len(data)-1:
            sql += str_conv(data[i])+','
        else:
            sql += str_conv(data[i])+')'
    cursor.execute(sql)
    db.commit()
    db.close()


# 搜索某一表中的数据
# db：数据库指针，由create()函数创建
# database：数据库名称，字符型
# table：表名称，字符型
# value: 要查询的数据
def select(db,database,table,value):
    cursor = db.cursor()
    cursor.execute("use %s"%(database))
    meta = showMeta(db,database,table)
    value = str_conv(value)
    for i in meta:
        data = ''
        cursor.execute("select *from %s where %s=%s"%(table,i,value))
        data = cursor.fetchall()
        if len(data)!=0:
            return data[0]
    return False


def display(db, database, table):
    cursor = db.cursor()
    cursor.execute("use %s"%(database))
    cursor.execute("select * from %s"%(table))
    data  = cursor.fetchall()
    res = []
    for i in data:
        res.append(i)
    return res
# 删除表中的一项数据
# db：数据库指针
# database：数据库名称，字符型
# table：表名称，字符型
# position：插入的位置，行数，第一条为0
def delete(db, database, table, position):
    cursor = db.cursor()
    cursor.execute("use %s"%(database))
    cursor.execute("delete from %s limit 1 offset %s"%(table, position))
    db.commit()
    db.close()

def update(db, table, position, value):
    cursor = db.cursor()
    cursor.execute("use %s"%(database))
    cursor.execute("update %s set %s =%s limit 1 offset %s", table, )

# 显示
def show(db):
    datas = []
    cursor = db.cursor()
    cursor.execute("SHOW DATABASES;")
    data = cursor.fetchall()
    for i in data:
        datas.append(i[0])
    return datas

def show_Tables(db,database):
    datas = []
    cursor = db.cursor()
    cursor.execute("use %s"%database)
    cursor.execute("show tables")
    data = cursor.fetchall()
    for i in data:
        datas.append(i[0])
    return datas
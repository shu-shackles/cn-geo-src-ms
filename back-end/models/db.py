from sqlalchemy import create_engine

HOST = '122.9.130.89'
PORT = 3306
USERNAME = 'summer'
PASSWORD = 'shanghaiSHU'
DB = 'summer'

# dialect + driver://username:passwor@host:port/database
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

# 创建数据库引擎
engine = create_engine(DB_URI)

# 创建数据库链接对象(也可以成为指针对象)
con = engine.connect()

# 执行sql语句 select 1
# result = con.execute("select 1")
# print(result.fetchone())

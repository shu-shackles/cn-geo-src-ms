from sqlalchemy import create_engine, event, select, exc

HOST = '122.9.130.89'
PORT = 3306
USERNAME = 'summer'
PASSWORD = 'shanghaiSHU'
DB = 'summer'

# dialect + driver://username:passwor@host:port/database
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

# 创建数据库引擎
engine = create_engine(DB_URI, pool_pre_ping=True)

# 创建数据库链接对象(也可以成为指针对象)
con = engine.connect()

# 执行sql语句 select 1
# result = con.execute("select 1")
# print(result.fetchone())


# 解决重连问题
@event.listens_for(engine, "engine_connect")
def ping_connection(connection, branch):
    if branch:
        # "branch" refers to a sub-connection of a connection,
        # we don't want to bother pinging on these.
        return

    # turn off "close with result".  This flag is only used with
    # "connectionless" execution, otherwise will be False in any case
    save_should_close_with_result = connection.should_close_with_result
    connection.should_close_with_result = False

    try:
        # run a SELECT 1.   use a core select() so that
        # the SELECT of a scalar value without a table is
        # appropriately formatted for the backend
        connection.scalar(select(1))
    except exc.DBAPIError as err:
        # catch SQLAlchemy's DBAPIError, which is a wrapper
        # for the DBAPI's exception.  It includes a .connection_invalidated
        # attribute which specifies if this connection is a "disconnect"
        # condition, which is based on inspection of the original exception
        # by the dialect in use.
        if err.connection_invalidated:
            # run the same SELECT again - the connection will re-validate
            # itself and establish a new connection.  The disconnect detection
            # here also causes the whole connection pool to be invalidated
            # so that all stale connections are discarded.
            connection.scalar(select(1))
        else:
            raise
    finally:
        # restore "close with result"
        connection.should_close_with_result = save_should_close_with_result

"""
演示python pymysql库的基础操作
"""
from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="localhost", # 主机名(IP)
    port=3306,        # 端口
    user="root",      # 账户
    passwd="",        # 密码
)
# print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()            # 获取到游标对象
conn.select_db("world")
# # 执行sql
# cursor.execute("create table test_pymysql2(id int)")

# 执行查询性质SQL
cursor.execute("select * from student")

results = cursor.fetchall()
for r in results:
    print(r)

# 关闭链接
conn.close()


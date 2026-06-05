import pymysql
import json
from datetime import date

# 1. 连接数据库
conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="",
    database="py_sql",
    charset="utf8",
    autocommit=True
)

try:
    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        # 2. 查询数据
        cursor.execute("select * from orders")
        data = cursor.fetchall()

        # 3. 处理日期字段
        for record in data:
            if isinstance(record['order_date'], date):
                record['order_date'] = record['order_date'].isoformat()

        # 4. 写入 JSON 文件
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

finally:
    conn.close()




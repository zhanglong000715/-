"""
完成练习案例：JSON商品统计
需求：
1. 各个城市销售额排名，从大到小
2. 全部城市，有哪些商品类别在售卖
3. 北京市有哪些商品类别在售卖
"""
from pyspark import SparkConf, SparkContext
import json
conf = SparkConf().setMaster("local[*]").setAppName("test_Spark")
sc = SparkContext(conf=conf)

# TODD 需求1： 城市销售额排名
# 1.1读取文件到RDD
file_rdd = sc.textFile("D:/orders.txt")
# 1.2取出一个个JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x:x.split("|"))
# 1.3将一个个JSON字符串转换为字典
dict_rdd = json_str_rdd.map(lambda x:json.loads(x))
# 1.4取出城市和销售额的数据
city_with_money_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
# 1.5按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a,b:a + b)
# 1.6按销售额聚合结果进行排序
result1_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False,numPartitions=1)
print("需求1的结果：",result1_rdd.collect())
# TODD 需求2： 全部城市有哪些商品类别在售卖
# 2.1取出全部的商品类别
city_with_category_rdd = dict_rdd.map(lambda x: x['category'])    # 可在此行采用链式调用.distinct()直接去重
# 2.2对全部商品类别进行去重
distinct_rdd = city_with_category_rdd.distinct()
print("需求2的结果：",distinct_rdd.collect())
# TODD 需求3： 北京市有哪些商品类别在售卖
# 3.1过滤掉北京市的数据
beijing_data_rdd = dict_rdd.filter(lambda x:x['areaName']=="北京")
# 3.2取出北京全部商品类别
category_rdd = beijing_data_rdd.map(lambda x: (x['category']))    # 可在此行采用链式调用.distinct()直接去重
# 3.3将北京所有商品类别进行去重处理
category_distinct_rdd = category_rdd.distinct()
print("需求3的结果是：",category_distinct_rdd.collect())


"""
需求3严重偏题错误思路：
list_rdd = []
for x in dict_rdd.collect():
    if x['areaName'] == "北京":
        list_rdd = list_rdd + [x['category']]
        set_category_rdd = set(list_rdd)
print("需求3的结果是：",set_category_rdd)
"""
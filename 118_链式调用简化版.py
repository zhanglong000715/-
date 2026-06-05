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
# 1.4取出城市和销售额的数据,按城市分组按销售额聚合,按销售额聚合结果进行排序
result1_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money']))).reduceByKey(lambda a,b:a + b).sortBy(lambda x: x[1], ascending=False,numPartitions=1)
print("需求1的结果：",result1_rdd.collect())

# TODD 需求2： 全部城市有哪些商品类别在售卖
# 2取出全部的商品类别,对全部商品类别进行去重
city_with_category_rdd = dict_rdd.map(lambda x: x['category']).distinct()
print("需求2的结果：",city_with_category_rdd.collect())

# TODD 需求3： 北京市有哪些商品类别在售卖
# 3过滤掉北京市的数据,取出北京全部商品类别,将北京所有商品类别进行去重处理
category_rdd = dict_rdd.filter(lambda x:x['areaName']=="北京").map(lambda x: (x['category'])).distinct()
print("需求3的结果：",category_rdd.collect())

"""
演示RDD输出为python对象
"""

from pyspark import SparkConf, SparkContext
import json
conf = SparkConf().setMaster("local[*]").setAppName("test_Spark")
sc = SparkContext(conf=conf)

# 准备RDD
rdd = sc.parallelize([1,2,3,4,5])

# collect算子，输出RDD为list对象
rdd_list = rdd.collect()
print(rdd_list)
print(type(rdd_list))
# reduce算子，对RDD进行两两聚合
num = rdd.reduce(lambda a,b:a+b)
print(num)
print(type(num))
# take算子，取出RDD前N个元组，组成list返回
list_take_rdd= rdd.take(5)
print(list_take_rdd)
print(type(list_take_rdd))

# count，统计RDD内有多少条数据，返回值为数字
num_count = rdd.count()
print(num_count)
print(type(num_count))



sc.stop()
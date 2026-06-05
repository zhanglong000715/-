"""
演示RDD的filter成员方法的使用
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_Spark")
sc = SparkContext(conf=conf)

# 准备RDD
# 对RDD的数据进行过滤
rdd = sc.parallelize([1,2,3,4,5,]).filter(lambda x : x % 2 == 0)
print(rdd.collect())

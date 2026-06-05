"""
演示pyspark综合案例
"""

from pyspark import SparkConf, SparkContext
import os
import json
os.environ['HADOOP_HOME'] = "D:/hadoop/hadoop-3.0.0"
conf = SparkConf().setMaster("local[*]").setAppName("test_Spark")
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

# 读取文件转换成RDD
rdd = sc.textFile("D:/search_log.txt")
# TODD 需求1： 热门搜索时间段Top3（小时精度）
# 1.1 取出全部色时间并转换为小时
rdd_h = rdd.flatMap(lambda line: line.split(" ")).map(lambda x:x.split(":")).\
    map(lambda x : x[0])
# 1.2 转换为(小时,1)的二元元组
rdd_h2 = rdd_h.map(lambda line: [line,1])
# 1.3 key分组聚合Value
rdd_h3 = rdd_h2.reduceByKey(lambda a,b:a+b)
# 1.4 排序(降序)
rdd_h4 = rdd_h3.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
# 1.5 取前3
rdd_h5 = rdd_h4.take(3)
# TODD 需求2： 热门搜索词Top3
# 2.1 取出全部的搜索词
rdd_str1 = rdd.flatMap(lambda line: line.split(" ")).map(lambda x:x.split()).\
    map(lambda x : x[2])
# 2.2 (词,1)二元元组
rdd_str2 = rdd_str1.map(lambda x : [x,1])
# 2.3 分组聚合
rdd_str3 = rdd_str2.reduceByKey(lambda a,b:a+b)
# 2.4排序
rdd_str4 = rdd_str3.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
# 2.5 Top3
rdd_str5 = rdd_str4.take(3)
# TODD 需求3： 统计黑马程序员关键字在什么时段被搜索的最多
# 3.1 过滤内容： 只保留黑马程序员关键字
rdd_heima1 = rdd.flatMap(lambda line: line.split(" ")).map(lambda x : x.split()).\
    filter(lambda x : x[2]=="黑马程序员")
# 3.2 转换为(小时,1)的二元元组
rdd_heima2 = rdd_heima1.map(lambda x:x[0])
rdd_heima3 = rdd_heima2.map(lambda x:x.split(":")).map(lambda x : (x[0],1))
# 3.3 key分组聚合value
rdd_heima4 = rdd_heima3.reduceByKey(lambda a,b:a+b)
# 3.4 排序(降序)
rdd_heima5 = rdd_heima4.sortBy(lambda x : x[1],ascending=False,numPartitions=1)
# 3.2 取前1
rdd_heima6 = rdd_heima5.take(1)

# TODD 需求4： 将数据转换为JSON格式，写出到文件中
# 4.1 转换为JSON格式的RDD
rdd_json = rdd.map(lambda x:x.split()).\
    map(lambda x: {"time":x[0],"user_id":x[1],"key_word":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]})
# 4.2 写出为文件
rdd_json.saveAsTextFile("D:/otuput_json")

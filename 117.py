"""
演示sortBy的使用
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_Spark")
sc = SparkContext(conf=conf)

# 1.读取数据文件
rdd = sc.textFile("D:/hello.txt")
# 2.取出全部单词
word_rdd = rdd.flatMap(lambda x:x.split(" "))
# 3.将所有单词都转换成二元元组，单词为key，value设置为1
word_with_one_rdd = word_rdd.map(lambda word:(word,1))
# 4.分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a,b: a + b)
# 5.对结果进行排序
finaL_RDD = result_rdd.sortBy(lambda x: x[1],ascending=True,numPartitions=1)
print(finaL_RDD.collect())





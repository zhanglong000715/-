"""
演示获取pyspark的执行环境入库对象:sparkcontext
并通过sparkcontext对象获取当前pyspark的版本
"""

# 导包
from pyspark import SparkContext, SparkConf
# 创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)
# 打印pyspark的运行版本
print(sc.version)
# 停止sparkcontext对象的运行（停止pyspark程序）
sc.stop()

from pyspark.sql import SparkSession
from lib.ConfigLoader import get_spark_conf


def get_spark_session(env):
    if env == "LOCAL":
        return SparkSession.builder \
            .master("local[2]") \
            .enableHiveSupport() \
            .getOrCreate()
    else:
        return SparkSession.builder \
            .config(conf=get_spark_conf(env)) \
            .enableHiveSupport() \
            .getOrCreate()

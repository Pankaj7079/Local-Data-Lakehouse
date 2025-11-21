"""Spark Data Lake"""

from pyspark.sql import SparkSession
from src.config import Config

def init_spark():
    """Initialize Spark"""
    print("\nInitializing Spark Data Lake...")
    
    spark = SparkSession.builder \
        .appName(Config.APP_NAME) \
        .master(Config.MASTER) \
        .config("spark.driver.memory", Config.DRIVER_MEMORY) \
        .config("spark.executor.memory", Config.EXECUTOR_MEMORY) \
        .getOrCreate()
    
    spark.sparkContext.setLogLevel("ERROR")
    print(f" Spark Ready! UI: {spark.sparkContext.uiWebUrl}")
    return spark

def load_data(spark, filepath):
    """Load CSV into Spark"""
    df = spark.read.csv(filepath, header=True, inferSchema=True)
    df.createOrReplaceTempView("customers")
    print(f" Loaded {df.count():,} rows")
    return df
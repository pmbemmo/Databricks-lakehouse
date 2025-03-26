# Databricks notebook source
from pyspark.sql.functions import col, to_timestamp, current_timestamp

# Lecture des données Bronze
silver_df = (
    spark.read.format("delta").table("dev_catalog.bronze.products")
    .filter(col("ProductID").isNotNull() & col("ProductName").isNotNull())
    .withColumn("last_update", current_timestamp())
)

# Écriture en table Silver
silver_table = "dev_catalog.silver.products"
silver_df.write.format("delta").mode("append").saveAsTable(silver_table)

# Optimisation avec Z-Ordering sur `ProductID`
spark.sql(f"OPTIMIZE {silver_table} ZORDER BY ProductID")

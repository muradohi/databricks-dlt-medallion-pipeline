import dlt
from pyspark.sql.functions import sum

@dlt.table(
    name = "business_query"
)
def business_query():
  df_cust = spark.read.table("dim_customers")
  df_prod = spark.read.table("dim_products")
  df_sales = spark.read.table("fact_sales")

  df_join = df_sales.join(df_cust, df_sales["customer_id"] == df_cust["customer_id"], "inner").join(df_prod, df_sales["product_id"] == df_prod["product_id"], "inner")
  
  df_prun = df_join.select("region", "category", "total_sales")

  df_final = df_prun.groupBy("region", "category").agg(sum("total_sales").alias("total_sales_region_cat"))

  return df_final


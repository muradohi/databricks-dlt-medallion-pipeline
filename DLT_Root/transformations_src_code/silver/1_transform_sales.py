import dlt
from pyspark.sql.functions import *


@dlt.view(
    name="sales_stg_trans_view"                                                  
)
def sales_stg_trans():
    df = spark.readStream.table("sales_stg")
    df = df.withColumn("total_sales", col("amount") * col("quantity"))
    return df                                                     

dlt.create_streaming_table(
    name="sales_enr"
)


dlt.create_auto_cdc_flow(
  target = "sales_enr",
  source = "sales_stg_trans_view",
  keys = ["sales_id"],
  sequence_by = "sale_timestamp",
  ignore_null_updates = False,
  apply_as_deletes = None,
  apply_as_truncates = None,
  column_list = None,
  except_column_list = None,
  stored_as_scd_type = 1,
  track_history_column_list = None,
  track_history_except_column_list = None
)



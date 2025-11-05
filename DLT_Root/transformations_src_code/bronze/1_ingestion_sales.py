import dlt

sales_rules = {
    "rule_1" : "sales_id IS NOT NULL",
    "rule_2" : "amount > 0"
}

dlt.create_streaming_table(
    name = "sales_stg",
    expect_all_or_drop= sales_rules
)

@dlt.append_flow(target="sales_stg")
def east_sales():
    df = spark.readStream.table("dlt_catalog.bronze_schema.sales_east")
    return df

@dlt.append_flow(target="sales_stg")
def west_sales():
    df = spark.readStream.table("dlt_catalog.bronze_schema.sales_west")
    return df
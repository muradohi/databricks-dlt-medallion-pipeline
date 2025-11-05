import dlt

customers_rules = {
    "rule_1" : "customer_name IS NOT NULL",
    "rule_2" : "customer_id IS NOT NULL" 
}

@dlt.table(
    name = "customers_stg"
)
@dlt.expect_all(customers_rules)
def customers_stg():
    df = spark.readStream.table("dlt_catalog.bronze_schema.customers")
    return df
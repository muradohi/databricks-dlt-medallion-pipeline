import dlt

products_rules ={
    "rule_1": "product_id IS NOT NULL",
    "rule_2": "product_name IS NOT NULL"

}

@dlt.table(
    name = "products_stg"
)
@dlt.expect_all(products_rules)
def products_stg():
    df = spark.readStream.table("dlt_catalog.bronze_schema.products")
    return df
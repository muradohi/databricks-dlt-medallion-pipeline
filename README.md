# 🚀 Databricks ELT Pipeline — Delta Live Tables (DLT) | Medallion Architecture

## 📌 Project Description

This project demonstrates an end-to-end **ELT data engineering pipeline** built on **Databricks** using **Delta Live Tables (DLT)** and **PySpark**.  
The objective was to simulate real-world streaming data ingestion and build a pipeline that processes raw sales records into business-ready insights using the **Medallion Architecture (Bronze → Silver → Gold)**.

Data used in this pipeline includes:
- Sales data arriving from **two regions (East & West)** → incremental streaming inserts
- Product dimension data (with updates → price change, name change)
- Customer dimension data (with updates → location change, name correction)

Even though the dataset is small (created using SQL inserts), it simulates:
- **Streaming / incremental ingestion**
- **Slowly Changing Dimensions (CDC updates)**


---



## ✅ What I Built

### 🔹 Bronze Layer — Ingestion
- Ingested raw regional sales tables (`sales_east`, `sales_west`) using  
  ✅ `dlt.create_streaming_table()`  
  ✅ `@dlt.append_flow()`  
- Applied **data quality rules** (`expect_all_or_drop`) on ingestion.

### 🔹 Silver Layer — Transformations
- Cleaned/enriched data (casting, computed columns like `total_sales`)
- Applied **Auto-CDC** (`dlt.create_auto_cdc_flow`) to handle:
  - Product price changes (SCD Type 1)
  - Customer region/name updates (SCD Type 2)
- Ensured only valid incremental changes are processed.

### 🔹 Gold Layer — Business Output
- Built a star-schema style model:
  - `dim_products`
  - `dim_customers`
  - `fact_sales`
- Created a reporting layer that shows:
  - **Total sales grouped by Region and Product Category**

---

## 🛠️ Tools & Tech Used

| Component | Technology Used |
|----------|-----------------|
| Platform | Databricks |
| Storage Format | Delta Lake (ACID transactions, versioning) |
| ETL Framework | **Delta Live Tables (DLT)** |
| Language | PySpark / SQL |
| Concepts Used | Streaming Ingestion, AutoCDC, SCD Type 1 & 2, Medallion Architecture |
| Version Control | Git + GitHub + Databricks Repos |

---

## 🌟 Key Learnings

- How to build a **streaming ELT pipeline** using Databricks DLT
- How to apply **data quality expectations**
- How **CDC + SCD Type 1 & 2** are handled automatically by DLT
- How to transform raw data into **business analytics outputs**

---

> This project demonstrates hands-on experience in Data Engineering using Databricks, Delta Lake, ETL automation, and streaming pipelines similar to what real companies build in production.


# Olist E-Commerce ETL Pipeline

A end-to-end ETL pipeline built in Python that ingests, transforms, and loads the
[Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
into a local DuckDB analytical database for SQL-based analysis.

---

## Architecture
```
data/raw/ (CSV files)
     |
     v
src/extract.py       -- Loads raw CSVs into Pandas DataFrames
     |
     v
src/transform.py     -- Cleans, standardizes, and models into star schema
     |
     v
src/load.py          -- Writes transformed tables into DuckDB
     |
     v
data/olist.duckdb    -- Analytical database
     |
     v
queries/             -- SQL analytics layer
```

---

## Schema

| Table | Type | Description |
|---|---|---|
| fact_orders | Fact | Order lifecycle and status |
| fact_order_items | Fact | Line items per order |
| fact_payments | Fact | Payment transactions |
| fact_reviews | Fact | Customer review scores |
| dim_customers | Dimension | Customer records |
| dim_products | Dimension | Product catalog with English category names |
| dim_sellers | Dimension | Seller location data |

---

## Queries

| File | Description |
|---|---|
| product_velocity.sql | Units sold per day and revenue by product category |
| seller_performance.sql | On-time delivery rate, review scores, and revenue per seller |
| order_funnel.sql | Drop-off rates from order placement through delivery |

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/olist-etl-pipeline.git
cd olist-etl-pipeline
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Download the dataset from Kaggle**
```bash
kaggle datasets download -d olistbr/brazilian-ecommerce
Expand-Archive -Path brazilian-ecommerce.zip -DestinationPath data\raw  # Windows
unzip brazilian-ecommerce.zip -d data/raw  # Mac/Linux
```

**5. Run the pipeline**
```bash
python src/pipeline.py
```

---

## Tech Stack

- Python 3
- Pandas
- DuckDB
- Kaggle API
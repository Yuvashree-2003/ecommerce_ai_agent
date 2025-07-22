import pandas as pd
import sqlite3

def create_database():
    conn = sqlite3.connect("ecommerce.db")


    # Load datasets
    ad_sales = pd.read_csv("data/ad_sales.csv")
    total_sales = pd.read_csv("data/total_sales.csv")
    eligibility = pd.read_csv("data/eligibility.csv")

    # Save to SQL
    ad_sales.to_sql("ad_sales", conn, if_exists="replace", index=False)
    total_sales.to_sql("total_sales", conn, if_exists="replace", index=False)
    eligibility.to_sql("eligibility", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

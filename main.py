import duckdb
con = duckdb.connect("analytics.duckdb")
con.execute("""
    CREATE TABLE IF NOT EXISTS sales AS
    SELECT * FROM (VALUES
        (1, 150000),
        (2, 250000)
    ) AS t(order_id, revenue)
""")
print(con.sql("SELECT * FROM sales").df())
con.close()
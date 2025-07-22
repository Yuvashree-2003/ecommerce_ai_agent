import sqlite3

def run_sql_query(query):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        return {"columns": columns, "data": result}
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()

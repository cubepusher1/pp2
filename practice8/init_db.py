from connect import connect

def run_sql_file(filename):
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            with open(filename, 'r', encoding='utf-8') as f:
                sql = f.read()
            
            cur.execute(sql)
            conn.commit()
            print(f"{filename}")
        except Exception as e:
            print(f"error {filename}: {e}")
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    run_sql_file("functions.sql")
    run_sql_file("procedures.sql")
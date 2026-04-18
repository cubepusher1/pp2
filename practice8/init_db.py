from connect import connect

def run_sql_file(filename):
    conn = connect()
    if conn:
        try:
            cur = conn.cursor()
            # Читаем твой SQL файл
            with open(filename, 'r', encoding='utf-8') as f:
                sql = f.read()
            
            # Выполняем всё содержимое
            cur.execute(sql)
            conn.commit()
            print(f"✅ Файл {filename} успешно применен!")
        except Exception as e:
            print(f"❌ Ошибка в файле {filename}: {e}")
        finally:
            cur.close()
            conn.close()

if __name__ == "__main__":
    # Сначала создаем функции, потом процедуры
    run_sql_file("functions.sql")
    run_sql_file("procedures.sql")
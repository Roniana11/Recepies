import pymysql


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

def get_ingredients(table_name):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT * FROM {table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except Exception as e:
        print(e)


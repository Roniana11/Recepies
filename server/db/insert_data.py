from cmath import e, polar
import pymysql


dairy_ingredients = ["Cream","Cheese","Milk","Butter","Creme","Ricotta","Mozzarella","Custard","Cream Cheese"]
gluten_ingredients = ["Flour","Bread","spaghetti","Biscuits","Beer"]


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="recipes_app",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def insert_dairy_ingredient(name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT INTO dairy VALUES(null, '{name}')"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")

def insert_gluten_ingredient(name):
    try:
        with connection.cursor() as cursor:
            query = f"INSERT INTO gluten VALUES(null, '{name}')"
            cursor.execute(query)
            connection.commit()

    except:
        print("Error")


def insert_all():
    for dairy in dairy_ingredients:
        insert_dairy_ingredient(dairy)
    for gluten in gluten_ingredients:
        insert_gluten_ingredient(gluten)    

# insert_all()



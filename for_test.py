import sqlite3 as sql


# with sql.connect('service.db') as db:
#     cursor = db.cursor()
#     query = """ CREATE TABLE "USERS_LOCATION" (
# 	"id"	INTEGER NOT NULL UNIQUE,
# 	"city"	TEXT NOT NULL,
# 	"street"	TEXT NOT NULL,
# 	"house"	INTEGER NOT NULL,
# 	"Lo1"	REAL NOT NULL,
# 	"La1"	REAL NOT NULL,
# 	"calculated"	INTEGER NOT NULL,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# ); """
#     cursor.execute(query)


def calculated_id(id):
    with sql.connect('service.db') as db:
        cursor = db.cursor()
        result = cursor.execute(f'SELECT * FROM USERS_LOCATION WHERE id = "{id}"')
        body = list[result]
    return body

id = 5
print(calculated_id(id))






# def receiver(city, street, house, Lo1, La1, calculated):
#     insert_payment = (city, street, house, Lo1, La1, calculated)
#     with sql.connect('service.db') as db:
#         cursor = db.cursor()
#         query = """ INSERT INTO USERS_LOCATION (city, street, house, Lo1, La1, calculated)
#                                             VALUES (?,?,?,?,?,?) RETURNING id """
#         cursor.execute(query, insert_payment)
#         res = next(cursor)
#         id = res[0]
#         db.commit()
#     return id
#
#
# city = 'test'
# street = 'test'
# house = 1
# Lo1 = 43.979288
# La1 = 56.271161
# calculated = 396
#
# print(receiver(city, street, house, Lo1, La1, calculated))



# def calculated():
#     with sql.connect('service.db') as db:
#         cursor = db.cursor()
#         query = """ SELECT * FROM USERS_LOCATION ORDER BY ID"""
#         cursor.execute(query)
#         result = cursor.fetchall()
#     return result
#
# print(calculated())
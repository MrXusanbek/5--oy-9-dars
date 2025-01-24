# import redis
# import json
#
#
# conn= redis.Redis(host = "localhost", port = 6379, db=0)
#
# conn.set("phone_number", value="+998910460982")
# print(json.load(conn.get("phone_number")))
#
# conn.close()
#----------------------------------------------------------
# # Homeworks  9 dars
# homework
# import redis
#
# conn = redis.Redis(host="localhost", port=6379, db=0)

# conn.set("phone_number", "+998910460982")
# print(conn.get("phone_number"))

# -----------------------------------------------------------------------
# 1 misol
# conn.set("adress", "Fargona")
# print(str(conn.get("adress"), "utf-8"))

# -----------------------------------------------------------------------

# if conn.exists("adress"):
#     conn.set("adress", "Fergana")
#     print(f"{"adress"} o'zgartirildi. Yangi qiymat: {"Shohimardon"}")
# else:
#     print(f"{"adress"} mavjud emas.")

# -----------------------------------------------------------------------

# conn.setex("q", "300", "400")
# print(str(conn.get("q"), "utf-8"))

# -----------------------------------------------------------------------

# a = conn.getset("adress", "Fargona")
#
# if a:
#     print(f"Eski qiymat: {str(conn.get("adress"), "utf-8")}")
# else:
#     print(f"{"adress"} uchun qiymat mavjud emas edi.")
#
# print(f"{"adress"} ning yangi qiymati: {"Shohimardon"}


# -----------------------------------------------------------------------

# conn.incrby("q", "100")
# print(str(conn.get("q"), "utf-8"))

# -----------------------------------------------------------------------

# conn.decrby("q", "100")
# print(str(conn.get("q"), "utf-8"))
# -----------------------------------------------------------------------

# print(conn.ttl("q"))

# -----------------------------------------------------------------------

# data = {
#     "name1": "Husanbek",
#     "name2": "Hasanbek",
#     "name3": "Diyorbek"
# }
#
# conn.mset(data)
# print(conn.mget("name1", "name2", "name3"))

# -----------------------------------------------------------------------

# conn.append("adress", " viloyati Fergana tumani.")
# print(str(conn.get("adress"), "utf-8"))

# -----------------------------------------------------------------------


# print(str(conn.getrange("adress", "0", "143"), "utf-8"))

# -----------------------------------------------------------------------

# conn.setrange("adress", 7, " viloyati Fergana tumani")
# print(str(conn.get("adress"), "utf-8"))

# -----------------------------------------------------------------------

# conn.delete("adress")
# print(str(conn.get("adress"), "utf-8"))

# -----------------------------------------------------------------------

# print(f"Eski qiymat: {str(conn.get("name"), "utf-8")}")
# old_value = conn.getset("name", "Rahmonov")
# print(f"Yangi qiymat: {str(conn.get("name"), "utf-8")}")

# -----------------------------------------------------------------------

# print(conn.strlen("name"))

# -----------------------------------------------------------------------

# conn.delete("name")
# result = conn.set("name", "Husanbek", nx=True)
# if result:
#     print(f"name kalitga {str(conn.get("name"), "utf-8")} qiymati o'rnatildi.")
# else:
#     print(f"name kaliti allaqachon mavjud, qiymat o'zgarmadi.")

# -----------------------------------------------------------------------

# a = conn.getset("lastname", "Rahmonov")
#
# if a:
#     print(f"Eski qiymat: {a.decode('utf-8')}")
# else:
#     print("Kalit mavjud emas, yangi qiymat o'rnatildi.")

# -----------------------------------------------------------------------

# conn.append("name", " Husanbek ")
# print(f"Yangilangan qiymat: { conn.get("name").decode('utf-8')}")

# -----------------------------------------------------------------------

# print(conn.type("name"))

# -----------------------------------------------------------------------

# a = input("qaysi kalitni qidirmoqchisiz: ")
# keys = conn.keys()
# if [key.decode('utf-8') for key in keys].count(a) > 0:
#     print("Siz qidirgan kalit bizda mavjud !")
# else:
#     print("Kechirasiz bunday kalit hali qo'shilmadian !")

# -----------------------------------------------------------------------






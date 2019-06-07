from flask import Flask,render_template,request
import pymysql
app=Flask(__name__)

db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='w1903',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
# utf-8  电脑改成英文
@app.route("/",methods=["get"])
def index():
    cursor=db.cursor()

    cursor.execute("select * from classes")
    result=cursor.fetchall()
    print(result)
    return render_template("index.html",datas=result)
app.run()

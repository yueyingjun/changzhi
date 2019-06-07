from flask import Flask,render_template,request
import pymysql

#  1. flask
#  2. pymysql
#
#  3. 安装mysql

#  4.  创一个库w1903
#  5. 创建一个表 classes

#  6.  字段  id  name  age  classes


#  1. 打开摄像头   采集到数据  python  服务器的能力  python 数据库

#  python numpy

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

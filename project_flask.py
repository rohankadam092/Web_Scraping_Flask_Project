# import flask and pymysql for html and database connectivity
from flask import *
import pymysql as p

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html") 

@app.route("/findmobile")
def inputmobile():
    return render_template("findmobile.html")

@app.route("/findlaptop")
def inputlaptop():
    return render_template("findlaptop.html")

@app.route("/details",methods=["post"])
def deatil():
    brand = request.form["brand"]
    brand = f"%{brand}%"
    pricemin = request.form["pricemin"]
    pricemax = request.form["pricemax"]
    storage = request.form["storage"]
    storage = f"%{storage}%"
    t=(brand,pricemin,pricemax,storage)
    d=displaymobile(t)
    return render_template("details.html",elist=d)

def get_connect():
    return p.connect(host="localhost",user="root",password="1234",database="project_product")


def displaymobile(t):
    connection=get_connect()
    cursormysql=connection.cursor()
    sql = "select * from mobile_flipkart where description like %s and price between %s and %s and ram_storage like %s"
    cursormysql.execute(sql,t)
    data=cursormysql.fetchall()
    connection.commit()
    connection.close()
    return data

@app.route("/detailslaptop",methods=["post"])
def deatillaptop():
    brand = request.form["brand"]
    brand = f"%{brand}%"
    processor = request.form["processor"]
    processor = f"%{processor}%"
    pricemin = request.form["pricemin"]
    pricemax = request.form["pricemax"]
    ram = request.form["ram"]
    ram = f"%{ram}%"
    storage = request.form["storage"]
    storage = f"%{storage}%"
    t=(brand,processor,pricemin,pricemax,ram,storage)
    d=displaylaptop(t)
    return render_template("detailslaptop.html",elist=d)

def displaylaptop(t):
    connection=get_connect()
    cursormysql=connection.cursor()
    sql = "select * from laptop_flipkart where description like %s and processor like %s and price between %s and %s and ram like %s and storage like %s"
    cursormysql.execute(sql,t)
    data=cursormysql.fetchall()
    connection.commit()
    connection.close()
    return data

@app.route("/cosmetics")
def cosmetics():
    return render_template("cosmetics.html")

@app.route("/findcosmetics")
def inputcosmetics():
    return render_template("findcosmetics.html")


@app.route("/detailscosmetics",methods=["post"])
def deatilcosmetics():
    product = request.form["product"]
    product = f"%{product}%"
    brand = request.form["brand"]
    brand = f"%{brand}%"
    pricemin = request.form["pricemin"]
    pricemax = request.form["pricemax"]
    t=(product,brand,pricemin,pricemax)
    d=displaycosmetics(t)
    return render_template("detailscosmetics.html",elist=d)

def displaycosmetics(t):
    connection=get_connect()
    cursormysql=connection.cursor()
    sql = "SELECT description, price, number_of_ratings, offer FROM cosmetics_nykaa where description like %s and brand like %s and price between %s and %s"
    cursormysql.execute(sql,t)
    data=cursormysql.fetchall()
    connection.commit()
    connection.close()
    return data


if __name__=="__main__":
    app.run(debug=True)


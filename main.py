
from flask import Flask, render_template,request,redirect, url_for
import mysql.connector 
import random
import string

""" db= mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='url',
    port=3306
) """
db= mysql.connector.connect(
    host='academia.c1mebdhdxytu.us-east-1.rds.amazonaws.com',
    user='p6',
    password='ALrUBIaLYcHR',
    database='p6',
    port=3306
) 
db.autocommit=True

app = Flask(__name__)

cursor=db.cursor()
""" @app.get("/") """
@app.route("/", methods=["GET","POST"])

def index():
    return render_template("index.html")
@app.route("/acortador", methods=["GET","POST"])

def crear():
    length_of_string = 5
    short =(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))
    if request.method=="POST":
        url=request.form["direccionURL"]
       
        cursor.execute('insert into acortador(link_corto, link_original) values (%s,%s)',(short,url))
        db.commit()
   
    return render_template("acortador/acortador.html",short=short,url=url)
@app.get("/cortar/<url_cort>")
def redireccionar(url_cort):
    cursor.execute("SELECT link_original from acortador where link_corto = %(link_corto)s",{'link_corto':url_cort})

    result=cursor.fetchone()
  
    return redirect(result[0])


""" app.run(debug=True)
 """

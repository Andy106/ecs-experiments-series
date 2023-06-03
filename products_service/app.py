from flask import Flask, abort, jsonify
import psycopg2

app = Flask(__name__)

myconn = psycopg2.connect(database = "DataWarehouseX", user = "postgres", password = "xxxx", host = "localhost", port = "5432")
mycursor = myconn.cursor()

@app.route("/")
def hello_world():
    return 'Hello from docker!'

@app.route("/api/1.0/products")
def products_view():
    try:
        global mycursor
        mycursor.execute("SELECT * FROM core.dim_product")
        db=[]
        for x in mycursor:
            db.append(x)        
        return jsonify(db)
    except IndexError:
        abort(404)
        
@app.route("/api/1.0/products/<id>")
def product_view(id):
    try:
        global mycursor
        cmd = "SELECT * FROM core.dim_product where product_id = " + "'"+id+"'"
        mycursor.execute(cmd)
        db=[]
        for x in mycursor:
            db.append(x)        
        return jsonify(db)
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)

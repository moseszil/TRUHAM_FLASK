# importing flask 
from flask import*
# importing pymysql
import pymysql
# importing cursors from pymysql 
import pymysql.cursors
# initializing the flask app 
app = Flask(__name__)
# importing os so as to get the directory to the add_products upload photo session
import os
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# defining the route
@app.route("/api/signup", methods=['POST'])
# defining the co-responding web-app function 
def signup():
    # getting user inputs
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    # Connecting to the database
    connection = pymysql.connect(user='root', host='localhost', password='', database='truhamsokogarden')
    # defining the cursor for sql execution 
    cursor = connection.cursor()
    # sql query to add users into the database
    sql ="INSERT INTO users(username, password, email, phone) VALUES(%s,%s,%s,%s)"
    # defining the data to replace the placeholders in sql query
    data = (username, password, email, phone)
    # executing the sql query 
    cursor.execute(sql, data)
    # Saving the data into the database
    connection.commit()
    # returning a response to the user 
    return jsonify({'success' : 'Thank You For Signing Up'})

# sign in api 
@app.route("/api/signin", methods = ['POST'])
def signin():
    # get user input 
    email = request.form['email']
    password = request.form['password']
    # create a connection to the database
    connection = pymysql.connect(user='root', host='localhost', password='',database='truhamsokogarden')
    # defining the cursor, we are using the DictCursor 
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # creating the sql query 
    sql = "SELECT * FROM users WHERE email=%s AND password=%s"
    # defining the data to replace the placeholders in the sql query
    data =(email,password)
    # Execute the sql query using the cursor 
    cursor.execute(sql,data)
    # We are using if else statement to check how many rows are returned
    count = cursor.rowcount
    # If condition to check if there are 0 rows found then return no user found 
    if count ==0:
        return jsonify({'message': 'Login Failed'})
    else:
        # if there is a user the else we tell the cursor to pick only one row normally the first row
        user = cursor.fetchone()
        # return a response with the user information
        return jsonify({'message' : 'Login Success', 'user':user})

# add_products API
# creating the route
@app.route("/api/add_products", methods = ['POST'])
# defining the corresponding web application function
def add_products ():
    # getting user input
    product_name = request.form['product_name']
    product_description = request.form['product_description']
    product_cost = request.form['product_cost']
    photo = request.files['product_photo']

    #get the image file name
    filename = photo.filename
    # specify where the image will be stored
    photo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # saving the photo
    photo.save(photo_path)

    # connecting to the database
    connection = pymysql.connect(user= 'root', host= 'localhost', password= '', database= 'truhamsokogarden')
    # defining the cursor
    cursor = connection.cursor()
    # create the sql query
    sql = "INSERT INTO product_details (product_name, product_description, product_cost, product_photo) VALUES (%s, %s, %s, %s)"
    # defining the data
    data = (product_name, product_description, product_cost,filename)
    # execute the query
    cursor.execute(sql,data)
    # commiting changes to the database
    connection.commit()
    connection.close
    # return a response
    return jsonify ({"Message" : "Product details added successfully"})

# get_products_details API
@app.route("/api/get_products_details")
def get_products_details():
    # creating a connection to the database
    connection = pymysql.connect(user='root', host='localhost', password='',database='truhamsokogarden')
    # defining the cursor to execute the SQL query
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # creating the sql query
    sql="SELECT * FROM product_details"
    # executing the sql query
    cursor.execute(sql)
    # fetching all the rows returned after sql query execution
    product_details = cursor.fetchall()
    connection.close
    # returning a response to the user 
    return jsonify (product_details)

# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": "1",  # use 1 when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})
# run the app 
app.run(debug=True)
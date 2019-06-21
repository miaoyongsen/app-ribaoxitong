#from flask import Flask,render_template,request
import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
import time
import datetime
import csv


app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        user_name = request.form.get("name")
        user_gzfx = request.form.get("gzfx")
        user_gznr = request.form.get("gznr")
        user_gzjd = request.form.get("gzjd")
        user_wcqk = request.form.get("wcqk")
        user_mrjh = request.form.get("mrjh")

        username = user_name
        usergzfx = user_gzfx
        usergznr = user_gznr
        usergzjd = user_gzjd
        userwcqk = user_wcqk
        usermrjh = user_mrjh

        nowTime = datetime.datetime.now().strftime('%Y-%m-%d')

        with open(r"C:\Users\阿苗\Desktop\%s.csv" %nowTime,'a',newline='') as f:
            ff = csv.writer(f)
            ff.writerow([username, usergzfx,usergznr,usergzjd,userwcqk,usermrjh])

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=880)
    app.run(debug=True)

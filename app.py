# ----------------------------------------------------------------------------
# Copyright (c) 2023 Mohamed Rizad
# All rights reserved.
#
# This code is licensed under the MIT License.
# You may use, distribute, and modify this code under the terms of the
# MIT License.
# ----------------------------------------------------------------------------


from flask import Flask, redirect, render_template, request, jsonify, json
from ifsc import ifsc_module

app = Flask(__name__, template_folder="public", static_url_path='/static/')


@app.route("/")
def main():
    if request.args.get('ifsc'):
        query = request.args.get('ifsc')
        
    else:
        return render_template("index.html")
    try:
       info =  ifsc_module(query)
    except:
       return "Invalid Ifsc Code"
    if info is not None:
        return jsonify(info)
    else:
        return "Something wrong"


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80, use_reloader=True, threaded=True,debug=False)
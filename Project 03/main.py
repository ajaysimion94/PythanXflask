from flask import Flask, render_template, redirect, url_for, make_response, request
app=Flask(__name__)
@app.route('/')
def renderhtmlfile():
    return render_template("index.html")

@app.route('/gethere', methods = ['POST', 'GET'])
def getfromhtml():
    if request.method=='POST':
        username=request.form['name']
        regnum=request.form['regno']
    resp=make_response(redirect(url_for('generateresp')))
    resp.set_cookie('Usrname',username)
    resp.set_cookie('Regno',regnum)
    return resp
@app.route('/yourprofile')
def generateresp():
    name=request.cookies.get('Usrname')
    pswd=request.cookies.get('Regno')
    msg=f"<h1>Welcome {name}, your Register number: {pswd}</h1>"
    return msg
if __name__=='__main__':
    app.run(debug=True)
from flask import Flask
app=Flask(__name__)

@app.route("/user/<name>")
def showmsg(name):
    return "<h1>Hello %s</h1>"%name
@app.route("/Regno/<Reg>/<name>")
def showreg(Reg,name):
    return "Name : %s"%name+"<br>Reg.No: %s"%Reg
if __name__=='__main__':
    app.run(debug=True)
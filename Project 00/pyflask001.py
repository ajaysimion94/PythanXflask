from flask import Flask, redirect, url_for
app=Flask("__name__")
@app.route("/admin")
def showmsgadmin():
    return "Hello Admin"
@app.route("/guest/<username>")
def showmsgusr(username):
    return "Hello %s !"%username
@app.route("/usersite/<user>")
def showmsg(user):
    if user=="admin":
        return redirect(url_for("showmsgadmin"))
    else:
        return redirect(url_for("showmsgusr",username=user))
if __name__=='__main__':
    app.run(debug=True)
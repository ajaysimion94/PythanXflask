from flask import Flask,request,render_template
app=Flask(__name__)

@app.route('/', methods=["GET"])
def squarethenum():
    if request.method=='GET':
        if request.args.get('number1')==None:
            return render_template('getnumber.html')
        elif request.args.get('number1')==' ':
            return "<html><h1>invalid Data</h1></html>"
        else:
            number=request.args.get('number1')
            sqofnum=int(number)*int(number)
            return render_template('result_sqr.html',num=number,squareofnum=sqofnum)
if __name__=='__main__':
    app.run(debug=True)

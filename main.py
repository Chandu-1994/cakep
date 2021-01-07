from flask import Flask,request,render_template
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def pet_main() :
   result=0
   resp = request.form
   a="Chocalate"
   b="Blackforest"
   c="Whiteforest"
   d=resp.get("num")
   price = 500

   if resp.get('sel')== '1':
       result="Chocalate cake Price : 500"
       return render_template("output1.html",resp=result)
   elif resp.get('sel')== '2':
       result="Blackforest cake Price :550"
       return render_template("output2.html",resp=result)
   elif resp.get('sel')== '3':
       result="Whiteforest cake Price :600"

       return render_template("output3.html",resp=result)
   else:
       return render_template("input1.html")


if __name__ == '__main__':
    app.run(debug=True)
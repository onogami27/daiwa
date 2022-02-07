
from flask import Flask, render_template, request

def test_f(name):
    print(f"私の名前は{name}です")

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def hello_world():
    
    get_t = request.form.get("text_text")
   
    
    
    return render_template("hello.html",  get_t=get_t)

if __name__ == "__main__":
   
    app.run(debug=True)
    
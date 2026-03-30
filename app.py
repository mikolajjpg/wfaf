from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "flask dziala"

@app.route("/form", methods=["GET", "POST"])
def form():
    fullname = None
    error = None
    if request.method == "POST":
        fullname = request.form.get('fullname')
        if not fullname.strip():
            error = "Nie podales swojego imienia i nazwiska"
            return render_template("form.html", fullname = None, erorr = error)

    return render_template("form.html", fullname = fullname)

@app.route("/better_calc", methods=["GET", "POST"])
def calc():
    result = None
    error = None
    a = None
    b = None
    operator = None
    if request.method == "POST":
        a = request.form.get('a')
        b = request.form.get('b')
        operator = request.form.get('operator')

        if not a or not b:
            error = "nie podales liczb"
            return render_template("better_calc.html", result = None, error=error, a = a,
    b = b,
    operator = operator)
        
        if operator == "/" and "b" == "0":
            return render_template("better_calc.html", result = None, error=error, a = a,
    b = b,
    operator = operator)
        
        
        result = eval(f"{a}{operator}{b}")

    return render_template("better_calc.html", result=result, error=error, a=a, b=b, operator = operator)


app.run(debug=True)
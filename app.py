from flask import Flask, render_template, request, redirect


app = Flask(__name__)


expenses = []


@app.route("/")
def home():

    total = sum(
        item["amount"]
        for item in expenses
    )

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )



@app.route("/add")
def add():

    return render_template(
        "add_expense.html"
    )



@app.route("/save", methods=["POST"])
def save():


    expense = {

        "name":request.form["name"],

        "category":request.form["category"],

        "amount":float(
            request.form["amount"]
        )

    }


    expenses.append(expense)


    return redirect("/")



@app.route("/health")
def health():

    return "SpendWise Application Running"



if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
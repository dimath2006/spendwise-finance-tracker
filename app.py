from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Temporary storage
expenses = []


@app.route("/")
def home():

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    return render_template(
        "index.html",
        expenses=expenses,
        total=total
    )


@app.route("/add_expense")
def add_expense():

    return render_template(
        "add_expense.html"
    )


@app.route("/save", methods=["POST"])
def save():

    name = request.form["name"]

    category = request.form["category"]

    amount = float(
        request.form["amount"]
    )


    expenses.append(
        {
            "name": name,
            "category": category,
            "amount": amount
        }
    )


    return redirect("/")


@app.route("/health")
def health():

    return "Application is running"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
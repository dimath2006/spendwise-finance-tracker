from flask import Flask, render_template, request

app = Flask(__name__)


expenses = []


@app.route("/")
def home():

    return render_template(
        "index.html",
        expenses=expenses
    )


@app.route("/add_expense")
def add_expense():

    return render_template(
        "add_expense.html"
    )


@app.route("/save", methods=["POST"])
def save():

    title = request.form["title"]

    amount = float(
        request.form["amount"]
    )

    category = request.form["category"]

    expenses.append(
        {
            "title": title,
            "amount": amount,
            "category": category
        }
    )

    return render_template(
        "index.html",
        expenses=expenses
    )


@app.route("/health")
def health():

    return "Application is running"



if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
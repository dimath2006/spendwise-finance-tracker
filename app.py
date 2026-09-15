from flask import Flask, render_template, request

app = Flask(__name__)


expenses = []


# Home page
@app.route("/")
def home():
    return render_template(
        "index.html",
        expenses=expenses
    )


# Add expense page
# Supports both /add and /add_expense
@app.route("/add")
@app.route("/add_expense")
def add_expense():
    return render_template(
        "add_expense.html"
    )


# Save expense data
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


# Health check endpoint
@app.route("/health")
def health():
    return "Application is running"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
from flask import Flask, request, render_template, session, redirect, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config["SECRET_KEY"] = "steviebaby"

debug = DebugToolbarExtension(app)
c = CurrencyRates()
codes = CurrencyCodes()

@app.route('/')
def converter_form():
    return render_template("form.html")

@app.route('/handle-conversion')
def converter():
    currency_from = request.args["currency-from"]
    currency_from = currency_from.upper()
    currency_to = request.args["currency-to"]
    currency_to = currency_to.upper()
    amount = request.args["amount"]
    amount = int(amount)

    try:
        exchange_rate = c.get_rate(currency_from, currency_to)
    except:
        flash("We do not have this currency yet!")
        return redirect('/')
    
    if( amount <= 0 ):
        flash("This is not a valid amount!")
        return redirect('/')
    exchanged_amount = amount*exchange_rate

    currency_sign =  codes.get_symbol(currency_to)
    rounded_amount = round(exchanged_amount, 2)
    return render_template("success.html",  symbol=currency_sign, amount=rounded_amount)

 #Currency Rates Source Not Ready is the error that pops up that should notify the user that they need to pick a real currency
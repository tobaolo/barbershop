import os
import re

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpme import login_required, apology

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///barbershop.db")


@app.route("/")
@login_required
def home():
    """Show portfolio of stocks"""


    iden = session["user_id"]

    shop = db.execute("SELECT shop_name FROM owners WHERE id= :iden", iden=iden)
    store = shop[0]["shop_name"]

    barbers = db.execute("SELECT * FROM barbers WHERE store_id=:iden", iden=iden)

    for x in barbers:
        x["name"] = x["name"]
        x["chair"] = x["chair"]
        x["wait"] = x["wait"]

    return render_template("home.html", store=store, barbers=barbers)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("No username provided")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("No password provided")

        # Query database for username
        rows = db.execute("SELECT * FROM owners WHERE username = :username",
                          username=request.form.get("username"))


        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return apology("username and/or password incorrect")

        # Remember which user has logged in - store id
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

       # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":

        # Ensure username was entered
        if not request.form.get("shopname"):
            return apology("No store name provided")

        # Ensure username was entered
        if not request.form.get("username"):
            return apology("No username provided")

        # Ensure password was entered
        elif not request.form.get("password"):
            return apology("No password provided")

        # Ensure confirmation password as entered
        elif not request.form.get("confirm"):
            return apology("No confirmation password provided")

        # Ensure password matches confirmation
        elif request.form.get("password") != request.form.get("confirm"):
            return apology("Passwords do not match")

        #Ensure password does not exist already
        if (len(db.execute("SELECT * FROM owners WHERE username = :username", username = request.form.get("username"))) > 0):
            return apology("Username exists. Pick another username")

        load = db.execute("INSERT INTO owners (shop_name, username, password) VALUES (:shop, :username, :hash)", shop=request.form.get("shopname"),
            username=request.form.get("username"), hash=generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8))

        session["user_id"] = load

        # Redirect user to home page
        return redirect("/")


@app.route("/newbarber",  methods=["GET", "POST"])
def newbarber():
    """Creates new barber"""

    iden = session["user_id"]

    if request.method == "GET":

        shop = db.execute("SELECT shop_name FROM owners WHERE id= :iden", iden=iden)
        store = shop[0]["shop_name"]

        return render_template("newbarber.html", store=store)

    if request.method == "POST":

        db.execute("INSERT INTO barbers (name, chair, store_id) VALUES (:name, :chair, :iden)", name=request.form.get("barber"), chair=request.form.get("chair"), iden=iden)

        barbers = db.execute("SELECT * FROM barbers WHERE store_id=:iden", iden=iden)

        for x in barbers:
            x["name"] = x["name"]
            x["chair"] = x["chair"]
            x["wait"] = x["wait"]

        return render_template("added.html")


@app.route("/choose",  methods=["GET", "POST"])
def choose():
    """Creates new barber"""

    iden = session["user_id"]

    shop = db.execute("SELECT shop_name FROM owners WHERE id= :iden", iden=iden)
    store = shop[0]["shop_name"]

    if request.method == "GET":

        barbers = db.execute("SELECT name FROM barbers WHERE store_id= :iden", iden=iden)
        for x in barbers:
            x["name"]=x["name"]

        return render_template("choose.html", store=store, barbers=barbers)

    if request.method == "POST":

        if not request.form.get("barber"):
            return apology("No barber chosen")

        if not request.form.get("client"):
            return apology("No name provided")

        barber_id = (db.execute("SELECT id FROM barbers WHERE name = :name AND store_id = :iden", name=request.form.get("barber"), iden=iden))[0]["id"]
        new_wait = (db.execute("SELECT wait FROM barbers WHERE name = :name AND store_id = :iden", name=request.form.get("barber"), iden=iden))[0]["wait"] + 30
        db.execute("INSERT INTO queue (barber_id, client, store_id) VALUES (:barber_id, :client, :iden)", barber_id=barber_id, client=request.form.get("client"), iden=iden)
        db.execute("UPDATE barbers SET wait = :new_wait WHERE id= :barber_id AND name=:name", new_wait=new_wait, barber_id=barber_id, name=request.form.get("barber"))

        barbers = db.execute("SELECT * FROM barbers WHERE store_id=:iden", iden=iden)

        for x in barbers:
            x["name"] = x["name"]
            x["chair"] = x["chair"]
            x["wait"] = x["wait"]

        return render_template("added.html")


@app.route("/barber_login", methods=["GET", "POST"])
def barber_login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure barber name was submitted
        if not request.form.get("barbername"):
            return apology("No name provided")

        # Ensure barber id was submitted
        elif not request.form.get("barberid"):
            return apology("No Barber ID provided")

        # Ensure store id was submitted
        elif not request.form.get("storeid"):
            return apology("No Store ID provided")

        # Query database for username
        rows = db.execute("SELECT * FROM barbers WHERE id = :iden", iden=request.form.get("barberid"))


        # Ensure username exists and password is correct
        if len(rows) != 1:
            return apology("Username and/or Password Incorrect")

        # Remember which user has logged in - barber id
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/barber_home")

       # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("barber_login.html")


@app.route("/barber_home")
@login_required
def barber_home():
    """Show portfolio of stocks"""

    iden = session["user_id"]
    barber = (db.execute("SELECT name FROM barbers WHERE id = :iden", iden=iden))[0]["name"]
    storeid = db.execute("SELECT store_id FROM barbers WHERE id = :iden", iden=iden)
    shop = db.execute("SELECT shop_name FROM owners WHERE id = :store_id", store_id=storeid[0]["store_id"])
    store = shop[0]["shop_name"]

    clients = db.execute("SELECT client FROM queue WHERE barber_id=:iden", iden=iden)

    current = "Chair Open"
    next_client = "Chair Open"

    if len(clients) is 1:
        current = clients[0]["client"]

    if len(clients) > 1:
        current = clients[0]["client"]
        next_client = clients[1]["client"]

    return render_template("barber_home.html", store=store, current=current, next_client=next_client, barber=barber)


@app.route("/nxt", methods=["GET"])
def nxt():
    """Removes row from queue after barber finishes"""

    iden = session["user_id"]

    new_wait = db.execute("SELECT wait FROM barbers WHERE id=:iden", iden=iden)[0]['wait'] - 30
    if new_wait >= 0:
        db.execute("UPDATE barbers SET wait = :new_wait WHERE id=:iden", iden=iden, new_wait=new_wait)

    rows = db.execute("SELECT * FROM queue WHERE barber_id=:iden", iden=iden)
    table = []

    for x in range(len(rows)):
        table.append(rows[x])

    if len(table) > 0:
        idx = table[0]["id"]
        db.execute("DELETE FROM queue WHERE id=:idx", idx=idx)

    return barber_home()


@app.route("/reset", methods=["GET"])
def reset():
    """Resets values from home page"""

    iden = session["user_id"]

    db.execute("UPDATE barbers SET wait = 0 WHERE store_id=:iden", iden=iden)
    db.execute("DELETE FROM queue WHERE store_id=:iden", iden=iden)

    return home()


@app.route("/ids", methods=["GET"])
def ids():
    """Get login credentials for each barber in the shop"""

    iden = session["user_id"]

    barbers = db.execute("SELECT id, name FROM barbers WHERE store_id=:iden", iden=iden)
    for x in barbers:
        name = x["name"]
        bid = x["id"]

    return render_template("ids.html", barbers=barbers, iden=iden)


@app.route("/added", methods=["GET"])
def added():
    """Standby screen that confirms patron was added to que then redirects back to home"""

    return render_template("added.html")

def errorhandler(e):
    """Handle error"""
    return render_template("fail.html")


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
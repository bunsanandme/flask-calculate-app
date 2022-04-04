from flask import render_template, redirect, url_for, request
from app import app
from app import forms
import datetime

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    form = forms.LoginForm()
    if form.validate_on_submit():
        result = abs(int(str(form.end_date.data - form.start_date.data).split(" ")[0]))

        return redirect(url_for("result", result=result))
    return render_template("calculate.html", form=form)


@app.route('/result')
def result():
    r = request.args.get('result')
    return render_template("result.html", result=r)

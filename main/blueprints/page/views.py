#!/usr/bin/python
from flask import Blueprint, render_template, request

page = Blueprint('page', __name__, template_folder='templates')
calc = Blueprint('calc', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('page/home.html')


@page.route('/terms')
def terms():
    return render_template('page/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('page/privacy.html')


@page.route('/FAQ')
def FAQ():
    return render_template('page/FAQ.html')


@calc.route('/calculator', methods=['GET', 'POST'])
def calculator():
    bmi = ''
    recommend = ''
    if request.method == 'POST' and 'ca_weight' in request.form:
        weight = float(request.form.get('ca_weight'))
        height = float(request.form.get('ca_height'))
        bmi = calc_bmi(weight, height)
        if bmi > 0:
            if bmi <= 16:
                recommend = "You are very underweight."
            elif bmi <= 18.5:
                recommend = "You are underweight."
            elif bmi <= 25:
                recommend = "Congrats! You are Healthy."
            elif bmi <= 30:
                recommend = "You are overweight"
            else:
                recommend = "You are very overweight."
        else:
            recommend = "Enter valid details!"
    return render_template("calc/calculator.html", bmi=bmi, recommend=recommend)


def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 1)
    return render_template('calc/calculator.html')


@calc.route('/info')
def info():
    return render_template('calc/info.html')


@calc.route('/test', methods=['GET', 'POST'])
def test():
    bmi2 = ''
    recommend2 = ''
    if request.method == 'POST' and 'ca_weight' in request.form:
        weight = float(request.form.get('ca_weight'))
        height = float(request.form.get('ca_height'))
        bmi2 = calc_bmi2(weight, height)
        if bmi2 > 0:
            if bmi2 <= 16:
                recommend2 = "You are very underweight."
            elif bmi2 <= 18.5:
                recommend2 = "You are underweight."
            elif bmi2 <= 25:
                recommend2 = "Congrats! You are Healthy."
            elif bmi2 <= 30:
                recommend2 = "You are overweight"
            else:
                recommend2 = "You are very overweight."
        else:
            recommend2 = "Enter valid details!"
    return render_template("calc/test.html", bmi2=bmi2, recommend2=recommend2)


def calc_bmi2(weight, height):
    return round((weight / ((height / 100) ** 2)), 1)
    return render_template('calc/test.html')

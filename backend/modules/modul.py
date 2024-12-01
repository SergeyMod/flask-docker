from flask import render_template
from flask import request
from flask import Blueprint
from calc.Calc import Calc

app_in = Blueprint("h1", __name__)

@app_in.route('/<primer>')
def hello(primer: str):
    # primer = request.form['primer']
    result, num = Calc().get_result_str(primer)
    if num == 0:
        primer = ''
    return render_template('index.html', primer=primer, result=result)


@app_in.route('/', methods=['POST', 'GET'])
def calc():
    if request.method == 'GET':
        return render_template('index.html')
    primer = request.form['primer']
    result, num = Calc().get_result_str(primer)
    primer = f"Пример: {primer}"
    if num == 0:
        primer = ''
    return render_template('index.html', primer=primer, result=result)
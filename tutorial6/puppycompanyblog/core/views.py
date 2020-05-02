from flask import render_template, redirect, url_for, request, Blueprint

core = Blueprint('core', __name__)


@core.route('/')
def index():
    # more to come
    return render_template('index.html')

@core.route('/info')
def info():
    return render_template('info.html')
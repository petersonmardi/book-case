from flask import (
Blueprint, url_for, render_template, redirect)
bp = Blueprint('index', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

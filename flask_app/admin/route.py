from flask import Blueprint, render_template,redirect

admin_bp = Blueprint('admin', __name__, template_folder='templates',static_folder='static')

@admin_bp.route('/admin')
def admin_home():
    return render_template('admin_home.html')

@admin_bp.route('/index')
def index():
    return render_template('index.html')
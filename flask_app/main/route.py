from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, template_folder='templates',static_folder='static')

@main_bp.route('/')
def home():
    return "Welcome to the main site"

@main_bp.route('/about')
def about():
    return "This is the about page"
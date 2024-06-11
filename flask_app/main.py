from flask import Flask
from admin import admin_bp
from main import main_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)


'''from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Wel Come to Flask.'


@app.route('/success/<int:score>')
def success(score):
    return f'Congratulation  your pass! your Score is {score}.'


@app.route('/failed/<int:score>')
def failed(score):
    return f'Ohh Sorrey your are Failed! Your Score is {score}.'

@app.route('/result/<int:marks>')
def result(marks):
    result =''
    if marks< 50:
        result='failed'
    else:
        result='success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)'''

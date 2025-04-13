from flask import Blueprint, render_template

login = Blueprint('login', __name__)

@login.route('/login', methods=['GET'])
def login_endpoint():
   return render_template('login.html')
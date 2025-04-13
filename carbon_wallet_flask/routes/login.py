from flask import Blueprint, render_template, request, jsonify

login = Blueprint('login', __name__)

@login.route('/')
@login.route('/login', methods=['GET'])
def login_endpoint():
   return render_template('login.html')

@login.route('/login-check', methods=['POST'])
def login_check():
   data = request.get_json()
   username = data.get('username')
   password = data.get('password')

   if username == 'admin' and password == 'password':
      return jsonify(success=True)
   else:
      return jsonify(success=False)
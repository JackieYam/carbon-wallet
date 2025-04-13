from flask import Blueprint, render_template, request, jsonify

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET'])
def register_endpoint():
   return render_template('register.html')

@register.route('/register-user', methods=['POST'])
def register_user():
   data = request.get_json()
   name = data.get('name')
   birthdate = data.get('birthdate')
   gender = data.get('gender')
   email = data.get('email')
   password = data.get('password')

   if not all([name, birthdate, gender, email, password]):
      return jsonify(success=False, error="請輸入所有必填欄位！")

   if email == "existing@example.com":  # Example check for existing user
      return jsonify(success=False, error="此電子郵件已被註冊！")

   return jsonify(success=True)
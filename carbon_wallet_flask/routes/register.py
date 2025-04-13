from flask import Blueprint, render_template

register = Blueprint('register', __name__)

@register.route('/register', methods=['GET'])
def register_endpoint():
   return render_template('register.html')
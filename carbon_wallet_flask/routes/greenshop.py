from flask import Blueprint, render_template

greenshop = Blueprint('greenshop', __name__)

@greenshop.route('/greenshop', methods=['GET'])
def greenshop_endpoint():
   return render_template('greenshop.html')
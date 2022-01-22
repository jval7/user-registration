from flask import Blueprint

from app.controllers.usercontroller import signup_form, info_saved, readme, get_users

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET', 'POST'])(signup_form)
user_bp.route('/successful', methods=['GET'])(info_saved)
user_bp.route('/get_users', methods=['GET'])(get_users)

from app.models.user_schema import UserSchema, CreateUserSchema
from app.models.user_model import UserModel
from flask import render_template, redirect, url_for, request


def info_saved():
    return render_template("successful.html")


def readme():
    return render_template("readme.html")


def signup_form():
    if request.method == 'POST':
        try:
            userschema = CreateUserSchema(**request.form)
            usermodel = UserModel(**userschema.dict())
            usermodel.save()
            usermodel.generate_log()
            return redirect(url_for('user_bp.info_saved'))
        except Exception as e:
            error = str(e)
            return render_template("signup_form.html", error=error), 400
    return render_template("signup_form.html")


def get_users():
    try:
        page = int(request.args.get('page', 1))
        users = UserModel.all_paginated(page=page)
        return render_template("show_users.html", users=users)
    except Exception as e:
        error = str(e)
        return render_template("show_users.html", error=error), 500

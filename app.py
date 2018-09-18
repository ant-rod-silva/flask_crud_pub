# -*- coding: utf-8 -*-
#!flask/bin/python

# pip install -r requirements.txt

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_admin as admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import ModelView

# Create application
app = Flask(__name__)
app.debug = True

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.sqlite'
db = SQLAlchemy(app)
#app.config['SQLALCHEMY_ECHO'] = True


# Flask views
@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

class CarUserView(ModelView):
    column_display_pk = True
    form_columns = ['id', 'desc']
    column_searchable_list = ['desc']
    column_filters = ['id']
    can_create = True
    can_edit = True
    can_delete = False  # disable model deletion
    can_view_details = True
    page_size = 2  # paginacao
    create_modal = True
    edit_modal = True
    can_export = True

class CarAdminView(ModelView):
    column_display_pk = True
    form_columns = ['id', 'desc']
    column_searchable_list = ['desc']
    column_filters = ['id']
    column_editable_list = ['desc']
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    page_size = 2
    create_modal = True
    edit_modal = True
    can_export = True

class Car(db.Model):
    #__tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desc = db.Column(db.String(50))

    def __str__(self):
        return self.desc

# Create admin
admin = admin.Admin(app, name='App', template_mode='bootstrap3')
admin.add_view(CarAdminView(Car, db.session))

if __name__ == '__main__':
    # Create DB
    db.create_all()
    # Start app
app.run(debug=True)


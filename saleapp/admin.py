from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from models import *


admin = Admin(app, name="Quan ly ban hang", template_mode="bootstrap4")


admin.add_view(ModelView(Categories, db.session))
admin.add_view(ModelView(Products, db.session))

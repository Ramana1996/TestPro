from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    
    password = db.Column(db.String(150))
    projects5 = db.relationship('Project5', backref='user', passive_deletes=True)
    projects6 = db.relationship('Project6', backref='user', passive_deletes=True)
    projects7 = db.relationship('Project7', backref='user', passive_deletes=True)
    projects8 = db.relationship('Project8', backref='user', passive_deletes=True)
   
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())



class Project5(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)
    project = db.Column(db.String,  )
    resource_type = db.Column(db.String(150))
    approver = db.Column(db.String(150))

class Project6(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)    
    project = db.Column(db.String,  )
    resource_type = db.Column(db.String(150))
    approver = db.Column(db.String(150))
    machine_type = db.Column(db.String,  )
    zone = db.Column(db.String(150), )
    service_account = db.Column(db.String(150),)
    access_scopes = db.Column(db.String, )

class Project7(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True) 
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)    
    project = db.Column(db.String,  )
    resource_type = db.Column(db.String(150))
    approver = db.Column(db.String(150))
    dataset_name = db.Column(db.String(150), )
    data_location = db.Column(db.String(150), )
    
class Project8(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)   
    author = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete="CASCADE"), nullable=False)    
    project = db.Column(db.String,  )
    resource_type = db.Column(db.String(150))
    approver = db.Column(db.String(150))
    Gcs_bucket_Location = db.Column(db.String,  )
    storage_class = db.Column(db.String(150),)
    role = db.Column(db.String(150), )
    service_account1 = db.Column(db.String(150), )
    access_control = db.Column(db.String(150), )
   
   
    
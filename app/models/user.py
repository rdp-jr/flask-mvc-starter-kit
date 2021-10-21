from . import db
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
     
    def create(username, password):
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def delete(user_id):
        delete_user = User.query.filter_by(id=user_id).first()
        if delete_user is not None:
            db.session.delete(delete_user)
            db.session.commit()

    def update(user_id, updated_data):
        pass
       # User.query.filter_by(id=user_id).update(updated_data)
    #    update_user = User.query.filter_by(id=user_id).first()

    def __repr__(self):
        return '<User %r>' % self.username
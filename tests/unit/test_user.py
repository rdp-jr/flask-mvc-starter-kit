from app.models.user import User

def test_new_user():
    user = User(username='jvdoe', password='123456')
    assert user.username == 'jvdoe'
    assert user.password == '123456'
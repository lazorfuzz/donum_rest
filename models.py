from database import db

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), unique=True, nullable=False)
    address = db.Column(db.String(240), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    donations = db.Column(db.Integer, nullable=False)
    
    def __init__(self, name, address, phone_number, donations):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.donations = donations
    
    def __repr__(self):
        return '<Organization %r' % self.name


class GiftCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store = db.Column(db.String(240), nullable=False)
    balance = db.Column(db.Float, nullable=False)
    number = db.Column(db.String(30), nullable=False)
    pin = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, store, balance, number, pin, user_id):
        self.store = store
        self.balance = balance
        self.number = number
        self.pin = pin
        self.user_id = user_id
    
    def __repr__(self):
        return '<GiftCard %r>' % self.store

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.String(80))

    def __init__(self, username, password, email, role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username

if __name__ == '__main__':
    db.create_all()
    db.session.commit()

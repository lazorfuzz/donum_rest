from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import json
from controllers import mainControllers
from database import db
from models import Organization

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/donum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
CORS(app)
db.init_app(app)
db.drop_all(app=app)
db.create_all(app=app)
api = Api(app)

api.add_resource(mainControllers.OrganizationList, '/orgs')
api.add_resource(mainControllers.OrganizationController, '/orgs/<org_id>')

api.add_resource(mainControllers.NewsController, '/news/<news_keyword>')

def populate_db():
  with app.app_context():
    db.session.add(Organization('San Martin Animal Shelter', '12370 Murphy Ave, San Martin, CA 95046', '(408) 686-3900', 5))
    db.session.commit()
    

populate_db()

if __name__ == '__main__':
    app.run(debug=True)

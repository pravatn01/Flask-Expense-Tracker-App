from app import app, db

def initialize_db():
    with app.app_context():
        db.create_all()
        print('Database Tables Created Successfully.')

#when a script is run directly its special variable __name__ is set to __main__
if __name__ == '__main__':
    initialize_db()

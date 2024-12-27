from app import app, db

def initialize_db():
    with app.app_context():
        db.create_all()
        print('Database Tables Created Successfully.')

if __name__ == '__main__':
    initialize_db()

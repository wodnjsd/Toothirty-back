from app import app, db
from models


with app.app_context():
  
  try:
      print("Recreating databse..")
      db.drop_all()
      db.create_all()

      print("seeding databse 🌱")
      db.session.add_all()
      db.session.commit()


      print("bye 👋")
  
  except Exception as e:
    print (e)

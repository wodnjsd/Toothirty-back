from app import app, db
from models.problem_data import problems_list, advice_list
from models.user_data import user_list
from models.type_data import type_list


with app.app_context():
  
  try:
      print("Recreating database..")
      db.drop_all()
      db.create_all()

      print("seeding database 🌱")
      db.session.add_all(user_list)
      db.session.commit()


      db.session.add_all(type_list)
      db.session.commit()

      db.session.add_all(problems_list)
      db.session.commit()


      db.session.add_all(advice_list)
      db.session.commit()

      print("bye 👋")
  
  except Exception as e:
    print (e)

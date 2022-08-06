from models.advice import AdviceModel
from models.problem import ProblemModel


advice_1 = AdviceModel(content="Rinse with warm salt water")
advice_2 = AdviceModel(content="Make sure you're not smoking!")
advice_3 = AdviceModel(content="Call NHS 111/ contact your dentist immediately")
advice_4 = AdviceModel(content="go to A&E!")
advice_5 = AdviceModel(content="Have you tried sensodyne toothpaste? Rub it on the tooth/ teeth and leave it overnight")
advice_6 = AdviceModel(content="Have a softer diet, avoid chewing gum")
advice_7 = AdviceModel(content="Manage your pain with paracetamol/ ibuprofen as needed")
advice_8 = AdviceModel(content="You need to work on your flossing and/or using interdental brushes!")
advice_9 = AdviceModel(content="Use corsodyl mouthwash")
advice_10 = AdviceModel(content="Use a single tufted toothbrush to clean under the gum")
advice_11 = AdviceModel(content="Have a softer diet, avoid chewing gum")
advice_12 = AdviceModel(content="Try to get some temporary filling material from the pharmacy if you notice a cavity")
advice_13 = AdviceModel(content="Keep it as clean as possible")
advice_14 = AdviceModel(content="Get a nightguard to protect your teeth overnight")
advice_15 = AdviceModel(content="Avoid spicy/ acidic/ salty foods")
advice_16 = AdviceModel(content="Get some bonjela/ orajel")


problems_list = [
  ProblemModel(name="Sharp pain", diagnosis="Decay", type_id=1, advice=[advice_7, advice_12, advice_13], user_id=1),
  ProblemModel(name="Aching", diagnosis="A dying nerve/ infection", type_id=1, advice=[advice_7, advice_1, advice_13], user_id=1),
  ProblemModel(name="Throbbing", diagnosis="Infection", type_id=1, advice=[advice_1, advice_7, advice_13], user_id=1),
  ProblemModel(name="Sensitivity", diagnosis="Decay/ toothwear", type_id=1, advice=[advice_5], user_id=1),
  ProblemModel(name="Bleeding", diagnosis="Gum disease", type_id=2, advice=[advice_8, advice_9], user_id=1),
  ProblemModel(name="Swelling/gum boil", diagnosis="Infection", advice=[advice_1], type_id=2, user_id=1),
  ProblemModel(name="Clenching/grinding", diagnosis="An unwanted habit!", advice=[advice_14, advice_6], type_id=3, user_id=1),
  ProblemModel(name="Locking/Clicking", diagnosis="A jaw problem", advice=[advice_6], type_id=3, user_id=1),
  ProblemModel(name="Ulcer", diagnosis="An ulcer", advice=[advice_16, advice_15], type_id=4, user_id=1),
  ProblemModel(name="Pain after extraction", diagnosis="Dry socket", advice=[advice_2, advice_1, advice_7], type_id=4, user_id=1),
  ProblemModel(name="Pain from wisdom tooth", diagnosis="Pericoronitis", advice=[advice_1, advice_9, advice_13], type_id=4, user_id=1)
]

# problems_advice_list = [

# ]

advice_list = [
  advice_1, advice_2, advice_3, advice_4, advice_5, advice_6, advice_7, advice_8, advice_9, advice_10
]
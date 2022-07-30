from models.advice import AdviceModel
from models.problem import ProblemModel
from models.type import TypeModel


advice_1 = AdviceModel(content="rinse with warm salt water")
advice_2 = AdviceModel(content="make sure you're not smoking!")
advice_3 = AdviceModel(content="call NHS 111/ contact your dentist immediately")
advice_4 = AdviceModel(content="go to A&E!")
advice_5 = AdviceModel(content="have you tried sensodyne toothpaste?")
advice_6 = AdviceModel(content="have a softer diet")


problems_list = [
  ProblemModel(name="decay", type_id=1, advice=[advice_1], user_id=1),
  ProblemModel(name="infection", type_id=1, user_id=1),
  ProblemModel(name="gum disease", type_id=1, user_id=1),
  ProblemModel(name="ulcer", type_id=1, user_id=1),
  ProblemModel(name="grinding/clenching", type_id=1, user_id=1),
  ProblemModel(name="sensitivity", type_id=1, user_id=1),
  ProblemModel(name="dry socket", type_id=1, user_id=1)
]

advice_list = [
  advice_1, advice_2
]
import random
import classe

class TEST:
  def __init__(self) -> None:
    self.vitesse = "vts"

TEST1 = TEST()
TEST1.vitesse = int(10)

TEST2 = TEST()
TEST2.vitesse = int(10)
test = [1, 1]


if test == [1, 1]:
  if TEST1.vitesse < TEST2.vitesse:
    print("1111111")
  elif TEST1.vitesse == TEST2.vitesse:
    print("on va jeter les dés !")
    x = int(random.randint(1,2))
    print(x)
    if x == 1:
      print("l'équipe 1 va commencé a attaquer en premier")
      print("1, jcp, etvoila")
    else:
      print("l'équipe 2 va commencé a attaquer en premier")
      print("2, jcp, etvoila")
  else:
    print("22222222")
elif 1 in test:
  coordonnee = test.index(1) + 1
  print(coordonnee)
  print("33333333333333333333")
else:
  print("444444444444444444")
  pass

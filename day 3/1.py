for i in range(1,100):
  if int(i) % 3 == 0:
    print('fizz')
  elif int(i) % 5 == 0:
    print('buzz')
  elif int(i) % 3 == int(i) % 5:
    print('fizzbuzz')
  else:
     print(i)

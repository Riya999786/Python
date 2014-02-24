def while_loop(lim, inc):
  i = 0
  numbers = []

  if (inc != 1):
    lim *= inc

  while i < lim:
    print "At the top i is %d" % i
    numbers.append(i)

    i += inc
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

  return numbers

cont = 1
increment = 1

while (cont == 1):
  num_list = []
  limit = int(raw_input("How big do you want the list to be? "))
  increment = int(raw_input("How much do you want to increment by? "))

  num_list = while_loop(limit, increment)

  print "The numbers: "

  for num in num_list:
    print num

  cont = int(raw_input("Continue? Enter 1 for YES, 0 for NO: "))

  if cont == 1:
    print "Continuing\n"
  elif cont == 0 :
    print "Goodbye!"
  else:
    while (cont >= 2):
      cont = int(raw_input("ERROR - Please Enter a new choice: "))
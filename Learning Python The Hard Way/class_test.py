## CONTACT LIST
# LIST
# CONTACT
# GROUP
# ???

class Contact(object):

    def __init__(self, name, age, sex):
      self.name = name
      self.age = age
      self.sex = sex

    def get_entry(self):
      # Print output
      pass


people = {}

people[1] = Contact("Joel Santiago", 27, "Male")
people[2] = Contact("Sandra Rusakiewicz", 29, "Female")

try:
  running = True
  while running:
    for x in people:
      print x, people[x].get_name()

    num = int(raw_input("\nWhich entry do you want to edit? "))

    # print "\nName:\t", people[num].get_name(), "\nAge:\t", people[num].get_age(), "\nSex:\t", people[num].get_sex()

    edit = raw_input("\nWhat would you like to edit? ")

    if edit == "name":
      print "name"
    elif edit == "age":
      print "age"
    elif edit == "sex":
      print "sex"
    else:
      print "else"

    # print "\nName:\t", people[num].get_name(), "\nAge:\t", people[num].get_age(), "\nSex:\t", people[num].get_sex()

    choice = raw_input("\nWould you like to edit anything else? ")
    if choice == "yes":
      print "Continuing..."
    elif choice == "no":
      running = False
    else:
      print "wrong choice"

except StandardError:
  print "\nSomething was done incorrectly"

finally:
  print "Bye"
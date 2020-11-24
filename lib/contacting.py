from peewee import *

hello = str(input("Hi, welcome to your contact book! Press enter to continue "))



db = PostgresqlDatabase('newcontacts', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db
        
class Contact(BaseModel):
    name = CharField()
    phone = CharField()


db.create_tables([Contact])
contact1= Contact(name='Lina', phone= '6758996735')
contact1.save()
# print("contact created")

contact2= Contact(name='Peter', phone= '8173352789')
contact2.save()
# print("contact created")

contact3= Contact(name='Antonette', phone= '262779101')
contact3.save()
# print("contact created")

contact4= Contact(name='Billy', phone= '7812234782')
contact4.save()
# print("contact created")

contact5= Contact(name='Teo', phone= '8956671236')
contact5.save()
# print("contact created")

contact6= Contact(name='Dhruv', phone= '1879963456')
contact6.save()
# print("contact created")

contact7= Contact(name='Noah', phone= '3489907253')
contact7.save()
# print("contact created")

contact8= Contact(name='Brad', phone= '5649085643')
contact8.save()
# print("contact created")

contact9= Contact(name='Zack', phone= '9086773512')
contact9.save()
# print("contact created")

contact10= Contact(name='Alaïa', phone= '5302276359')
contact10.save()
# print("contact created")
# get
print("Search for the name of your contact " )
search= str(input("name: "))

get_contact = Contact.get(Contact.name == search)
print(get_contact.phone)



#update 
new_name=print(str(input(" What name do you want to fix? ")))
new_number= str(input(" What is the new phone-number "))
# new_search= str(input("contact: "))
hello = Contact.get(Contact.name == search)
hello.phone = new_number
hello.save()

new_num= Contact.get()
print(hello)
#delete

# hello.delete_instance()

print("Here is yourt list of contacts: ")
list_of_people = Contact.select()
print(list_of_people)
for people in list_of_people:
    print(people.name, people.phone)


new_delete= str(input(" What is the contact you want to delete? "))
hello2 = Contact.get(Contact.name == new_delete)
hello2.delete_instance()
list_of_people = Contact.select()
print("Here is your new list: ")
print(list_of_people)
for people in list_of_people:
    print(people.name, people.phone)

print("Bye")
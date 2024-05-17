#PHONE BOOK USING PYTHON

def add():
    name=input("enter the name")
    num=int(input("enter the num"))
    person={
        'name':name,
        'number':num
    }
    phonebook[name.lower()]=person

def view():
    user=input("enter name :")
    if user in phonebook.keys():
        print("name found :",phonebook[user]['name'])
        print("number :",phonebook[user]['number'])

def show_all():
    print(phonebook.values())

def phone():
    user=input("enter name")
    if user in phonebook.keys():
        new_num=int(input("enter new num"))
        phonebook[user]["number"]=new_num
    else:
        print("user not found")

def cname():
    person=input("enter name")
    if person in phonebook.keys():
        print(phonebook[person]["name"])
        new_name=input("enter the new name")
        phonebook[person]['name']=new_name
        popped_person=phonebook.pop(person)
        phonebook[new_name]=popped_person
    else:
        print("not found")

def delete():
    person=(input("enter the name"))
    if person in phonebook.keys():
        del phonebook[person]


phonebook={}
while True:
    print("""press\n1:to add user\n2:to view a user\n3:to view all user\n4:edit phone num\n5:edit user name\n6:to delete a user\n7:QUIT""")
    option=int(input("enter a num from the options :"))

    if option==1:
        add()
    elif option==2:
        view()
    elif option==3:
        show_all()
    elif option==4:
        phone()
    elif option==5:
        cname()
    elif option==6:
        delete()
    elif option==7:
        break
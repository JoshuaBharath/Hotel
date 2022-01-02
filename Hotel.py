import os
import Guest
import datetime


def clear():
    os.system("cls")


totalNumberOfGuests=0
isTrue=True
allMemeber=[]

for member in Guest.staffAndManager():
    allMemeber.append(member)


while isTrue==True:
    try:
        clear()
        print("1. Number Of Customer Joining")
        print("2. Search Guest")
        print("3. Sort And View")
        print("4. Total Number Of Customers")
        print("5. Exit")
        menu=int(input(f"===> "))
        clear()
        if menu==1:
            try:
                print("Enter The  Number Of Customer That Are Joining the hotel")
                numberOfPeopleJoining=int(input("===> "))
                clear()
                if (len(allMemeber)+numberOfPeopleJoining)<=100:
                    for guest in range(numberOfPeopleJoining):
                        print("Enter Name")
                        name=input("===> ")
                        print("Enter Surname")
                        surname=input("===> ")
                        print("Enter Date YYYY-M-D")
                        date=input("===> ")
                        splitDate=date.split("-")
                        datePieceBack=datetime.datetime(int(splitDate[0]),int(splitDate[1]),int(splitDate[2]))
                        datePlaceHolder=datePieceBack.strftime(" %d-%m-%Y ")
                        print("Are You Vaccinated")
                        print("1. True")
                        print("2. False")
                        vacinated=False
                        if int(input("===> "))==1:
                            vacinated=True
                        elif int(input("===> "))==2:
                            vacinated=False
                        else:
                            print(" you can only pick 1 for true or 2 for false")
                        allMemeber.append(Guest.Guest(name,surname,datePlaceHolder,vacinated))
                        clear()
                else:
                    print(f"their is currently: {len(allMemeber)}")
                    print(f"amount space left: {100-len(allMemeber)}")

            except:
                print('"Enter The  Number Of Customer That Are Joining the hotel" you need to enter a number OR') 
                print('"Enter Date YYYY-M-D" date must be in that format eg 2022-6-5 or 2020-11-5')   
                input()
        elif menu==2:
            print("Enter Name")
            guestName=input("===> ")
            print("Enter Surname")
            guestSurname=input("===> ")
            clear()    
            doesGuestExist=False
            for searchGuest in allMemeber:
                if searchGuest.Gname.upper()==guestName.upper() and searchGuest.Gsurname.upper()==guestSurname.upper():
                    doesGuestExist=True
                    print(f"name\t\tsurname\t\tdate\t\tvacinated")
                    print(searchGuest.ToString())
                    input()
            if doesGuestExist==False:
                    print("item doesnt exist")
                    input() 
            allMemeber.sort(key=lambda x: x.Gname)
            for item in allMemeber:
                item.ToString()
            input()
        elif menu==4:
            print("Total Number Of Guests")
            print(f"===> {len(allMemeber)}")
            input()
        elif menu==5:
            print
            isTrue=False
        else:
            print("number doesnt exist in this conent")
            input()
        
    except:
        clear()
        print("you can only enter a number")
        input()

    
    
        
import datetime
class Guest:
    #g will stand for Guest
    def __init__(self,gname,gsurname,gdate,gvaccinated):
        self.Gname=gname
        self.Gsurname=gsurname
        self.Gdate=gdate
        self.Gvaccinated=gvaccinated
    def ToString(self):
        return print(f"{self.Gname.title()}\t\t{self.Gsurname.title()}\t\t{self.Gdate}\t{self.Gvaccinated}")
    

    
def staffAndManager():
    dummyMemebers=[]
    date0=datetime.datetime(2020,3,4)
    dummyMemebers.append(Guest("Joshua","Bharath",date0.strftime("%d-%m-%Y"),'True'))
    date1=datetime.datetime(2030,3,6)
    dummyMemebers.append(Guest("zake","Bharath",date1.strftime("%d-%m-%Y"),'False'))
    date2=datetime.datetime(2030,3,6)
    dummyMemebers.append(Guest("toby","Bharath",date2.strftime("%d-%m-%Y"),'False'))
    return dummyMemebers


print("This is a program of practicing of the args and kwargs")

def funcArgs(*arggs):
    print("The args are ")
    for i in arggs:
        print(i)

names= ["Jay","Jack","BMW","AUDI","Mercedes Benz"]
funcArgs(*names)


def funcKwargs(**kwarrgs):
    print("The Bio data of the person[legend] is ")
    for key,value in kwarrgs.items():
        print(f"{key} :--:  {value}")

    print("Retrievation of the data of the person using kwargs")


   # Bio data of the person

bio_data = {
       "Name" : "Jay",
       "Age" : "19",
       "Address":  "Surat",
       "Phone":"XXXXXXXX57"

   }
  #  Now print this using a kwargs
funcKwargs(**bio_data)

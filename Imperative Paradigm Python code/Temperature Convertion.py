#---------------------Temperature Conversion------------------
#Program that converts the temperature of Fahrenheit to celsius and vice versa.
#Made by Charlie Phong
#
clear = '\n'*70
def Menu():
    print(29*"-"+"Temperture Conversion"+30*"-")
    print("Menu options:","\n 1. Fahrenheit to Celsius \n 2. Celsius to Fahrenheit \n 3. Quit")
    print(80*"-") 
    choice=input("Select: ")
    
    if(choice == "1"):
      F() 
    elif(choice == "2"):
      C()
    elif(choice == "3"):
      quit
    else:
      print("Please try again")
      print()
      Menu()

def F():
    print(clear)
    while True:
        try:
            Fahren = int(input("Enter Fahrenheit: "))
        except ValueError:
            print(clear)
            print("Please try again!")
            print(80*"-")
            continue
        print("Fahrenheit converted to Celsius:")
        print((Fahren-32)*5/9)
        print(80*"-")
        print("\n1. Try again \n2. Back to Menu")
        print(80*"-")
        Selected=input("Select: ")

        if(Selected == "1"):
            F()
        elif(Selected == "2"):
            print(clear)
            Menu()
        else:
            print("Please try again")
            F()

def C():
    print(clear)
    while True:
        try:
            Cel = int(input("Enter Celsius: "))
        except ValueError:
            print(clear)
            print("please try again!")
            print(80*"-")
            continue
        print("Celsius converted to Fahrenheit:")
        print((9*Cel)/5+32)
        print(80*"-")
        print("\n1. Try again \n2. Back to Menu")
        print(80*"-")
        Selected=input("Select: ")
        
        if(Selected == "1"):
            C() 
        elif(Selected == "2"):
            print(clear)
            Menu()
        else:
          print("Please try again")
          C()

Menu()

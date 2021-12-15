def print_weekday_name(x):
     if (x==1):
         print ("Monday")
     if (x==2):
         print("Tuesday")
     if (x==3):
         print("Wednesday")
     if (x==4):
         print("Thursday")
     if (x==5):
         print("Friday")
     if (x==6):
         print("Saturday")
     if (x==7):
         print("Sunday")
     if(x<1 or x>12):
         print("Invalid input")
Weekday = int(input("Enter the weekday number: "))
print_weekday_name(Weekday)
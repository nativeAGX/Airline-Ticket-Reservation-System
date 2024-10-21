import csv
def ticket_reservation():
    print("1. Do you want to book a airplane ticket ?")
    print("2. Exit")
    choice=int(input("Enter you option"))
    if choice==1:
     ticket_details()
    else:
     exit()
def ticket_details():
 global name
 global departure
 global destination
 global flightname
 global date
 global time
 name=input("Enter your name")
 departure=input("Enter your place of Departure")
 destination=input("Enter you Destination")
 choice2=int(input("Enter the Airline you want to travel by\n1.Air India\n2.Emirates\n3.Qatar Airways"))
 if choice2==1:
     flightname="Air India"
 elif choice2==2:
     flightname="Emirates"    
 elif choice2==3:
     flightname="Qatar Airways"
 date=input("Enter the date")
 time=input("Enter the time.  |Flights are every 4 hrs starting from 00:00 hr. i.e- 00:00,04:00,08:00,12:00,16:00,20:00|")
 ticket_details2()
def ticket_details2():
 global flightclass
 global ticketprice
 global n 
 choice3=int(input("Enter the class you want to travel in.\n1.Economy Class   Ticket Price-20000/-\n2.Business Class   Ticket Price-50000/-\n3.First Class    Ticket Price-100000/-"))
 if choice3==1:
     flightclass="Economy Class"
     ticketprice=20000
 elif choice3==2:
     flightclass="Business Class"
     ticketprice=50000    
 elif choice3==3:
     flightclass="First Class"
     ticketprice=100000
 n=int(input("How many ticket you want to book ?"))
 food_details()
def food_details():
 global cuisine
 global foodprice
 choice4=int(input("Enter the cuisine you want to have in flight.\n1.Indian   Price-5000/-\n2.Continental   Price-8000/-\n3.Thai   Price-9000/-\n4.Italian   Price-10000/-\n5.Greek   Price-12000/-"))
 if choice4==1:
     cuisine="Indian"
     foodprice=5000
 elif choice4==2:
     cuisine="Continental"
     foodprice=8000   
 elif choice4==3:
     cuisine="Thai"
     foodprice=9000    
 elif choice4==4:
     cuisine="Italian"
     foodprice=10000   
 elif choice4==5:
     cuisine="Greek"
     foodprice=12000
 ticket_confirmation()
def ticket_confirmation():
 global totalprice
 totalprice=n*ticketprice+foodprice
 print("Your Total Bill is" ,totalprice,"Rs")
 print("Your Ticket Details are:")
 print("Name: ",name) 
 print("Departure: ",departure) 
 print("Destination: ",destination)
 print("Flight: ",flightname)
 print("Date: ",date)
 print("Time: ",time)
 print("Class: ",flightclass)
 print("No. of Tickets: ",n)
 print("Cuisine: ",cuisine)
 choice5=input("Press Y to confirm the Booking and N to cancel it")
 if choice5=="Y" or choice5=="y":
    add_reservation(name,departure,destination,flightname,date,time,flightclass,ticketprice,n,cuisine,foodprice,totalprice)
    print("Congratulations !!! Your tickets have been booked.")
    ticket_reservation()
 elif choice5=="N" or choice5=="n":
    print("Your ticket has been cancelled")
    ticket_reservation() # Function to add a reservation
def add_reservation(name1,departure1,destination1,flightname1,date1,time1,flightclass1,ticketprice1,n1,cuisine1,foodprice1,totalprice1):
    with open("Air_Ticket_Reservations.csv", "a", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Name','Departure','Destination','Flight Name','Date','Time','Flight Class','Ticket Price','No. of Tickets','Cuisine','Food Price','Total Bill'])
        csv_writer.writerow([name1,departure1,destination1,flightname1,date1,time1,flightclass1,ticketprice1,n1,cuisine1,foodprice1,totalprice1])

ticket_reservation()
        



              
    
    

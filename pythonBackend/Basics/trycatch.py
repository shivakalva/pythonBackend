tickets = input("what is the ticket number?")
ticket = int(tickets)
try:
    if ticket < 5:
        print("no tickets get more if you need")
except valueError:
        print("try again")
else:
    print(" Tickets are printing")

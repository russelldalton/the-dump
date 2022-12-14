class attendee:
    def __init__(self, name, company, state, email):
        self.name = name
        self.company=company
        self.state = state
        self.email = email

    def __str__(self):
        return f"{self.name} {self.company} {self.state} {self.email}"

    def getState(self):
        return self.state

class speaker(attendee):
    def __init__(self, name, company, state, email, day, capacity, title):
        self.title = title
        self.day = day 
        self.capacity = capacity
        attendee.__init__(self, name, company, state, email)

    def __str__(self):
        return f"{self.name} presents {self.title} on day {self.day}"

class conference: 
    def __init__ (self):
        self.attendees = []

    def addattendee(self, name, company, state, email):
        self.attendees.append(attendee(name,company,state,email))

    def deleteattendee(self):
        pass

    def listattendees(self):
        for attendee in self.attendees:
            print(attendee)

    def listattendeebystate(self, state):
        for attendee in self.attendees:
            if attendee.getState() == state:
                print(attendee)

    def addspeaker(self, name, company, state, email, day, capacity, title):
        self.attendees.append(speaker(name, company, state, email, day, capacity, title))

def main():
    myconference = conference()
    file = open('attendees.csv')
    file.readline()
    for line in file:
        data = line.rstrip('\n').split(',')
        if data[4]=="yes":
            myconference.addspeaker(data[0],data[1],data[2],data[3],data[5],data[6], data[7])
        else:
            myconference.addattendee(data[0],data[1],data[2],data[3])
    file.close()
    print("\nall attendees:")
    myconference.listattendees()
    print("\nattendees from maine:\n")
    myconference.listattendeebystate("ME")
if __name__ == '__main__':
    main()
    
        

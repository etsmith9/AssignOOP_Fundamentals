# Extend an existing Event class by adding a feature to keep track
#  of the number of participants. Implement a method add_participant 
# that increases the count and a method get_participant_count to 
# retrieve the current count.

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants = []

    def add_participant(self, name):
        if name not in self.participants:
            self.participants.append(name)
        else:
            print("Participant already included.")

    def get_participant_count(self):
        return len(self.participants)

event = None

while True:
    action = input("Enter action (add, count, exit) to keep track of your event participants:   ")
    if action == 'exit':
        break

    try:
        if action == "add":
            if event is None:
                event_name = input("Enter name of event:  ")
                event_date = input("Enter date of event:  ")
                event = Event(event_name, event_date)       
                print(f"Event '{event_name}'scheduled for {event_date}.")

            name = input("Enter name of participant:  ")
            event.add_participant(name)
            print(f"{name} added to the event on {event.date}.")

        elif action == "count":
            if event:
                print(f"The total count of participants is {event.get_participant_count()}")
            else:
                print("No event scheduled yet.")

    except Exception as e: 
            print(f"An error occured: {e}")
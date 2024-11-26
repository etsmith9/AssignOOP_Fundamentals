#question1.py

#Create a Python class Vehicle with attributes registration_number,
#  type, and owner. Implement a method update_owner to change 
# the vehicle's owner. Then, create a few instances of Vehicle and 
# demonstrate changing the owner.


class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_details(self):
        print(f"Registration: {self.reg_num}, Type: {self.vehicle_type}, Owner: {self.owner}")

vehicles = {}

def register_vehicle(reg_num, vehicle_type, owner):
    if reg_num in vehicles:
        print("Error: Registration number already exists.")
        return
    vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print(f"Vehicle with reg number {reg_num} registered.")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner) 
        print(f"Updated owner for vehicle {reg_num}.")
    else:
        print("Vehicle not found.")

def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_details()

while True:
    action = input("Enter action (register, update, display, exit):  ").lower()
    if action == "exit":
        break

    try:
        if action == "register":
            reg_num = input("Enter registration number: ")
            vehicle_type = input("Enter vehicle type:  ")
            owner = input("Enter owner name:  ")
            register_vehicle(reg_num, vehicle_type, owner)
        elif action == "update":
            reg_num = input("Enter registration number:  ")
            new_owner = input("Enter new owner name:  ")
            update_vehicle_owner(reg_num, new_owner)
        elif action == "display":
            display_all_vehicles()
    except Exception as e:
        print(f"An error occured: {e}")
print("System exiting.")
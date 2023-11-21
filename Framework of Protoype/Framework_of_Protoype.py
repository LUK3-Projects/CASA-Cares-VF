class UserAuth:
    def __init__(self):
        self.valid_username = "Admin"
        self.valid_password = "password1"

    def login(self, username, password):
        return username == self.valid_username and password == self.valid_password

class MyApp:
    def __init__(self):
        self.auth = UserAuth()
        self.is_logged_in = False
        self.venues = [
            {"name": "Venue A", "location": "Montreal", "cost": 1000, "max_capacity": 100, "phone": "111-111-1111"},
            {"name": "Venue B", "location": "Montreal", "cost": 1500, "max_capacity": 150, "phone": "111-111-1112"},
            {"name": "Venue C", "location": "Quebec City", "cost": 2000, "max_capacity": 300, "phone": "111-111-1113"},
            {"name": "Venue D", "location": "Quebec City", "cost": 2500, "max_capacity": 400, "phone": "111-111-1114"},
            {"name": "Venue E", "location": "Laval", "cost": 900, "max_capacity": 100, "phone": "111-111-1115"},
            {"name": "Venue F", "location": "Laval", "cost": 500, "max_capacity": 50, "phone": "111-111-1116"},
        ]
        self.services = [
            {"name": "Service A", "location": "Montreal", "cost": 500, "max_attendees": 50, "service_type": "Catering", "phone": "111-111-1116"},
            {"name": "Service B", "location": "Montreal", "cost": 750, "max_attendees": 75, "service_type": "Music", "phone": "111-111-1117"},
            {"name": "Service B", "location": "Quebec City", "cost": 1000, "max_attendees": 200, "service_type": "Catering", "phone": "111-111-1118"},
            {"name": "Service B", "location": "Quebec City", "cost": 1500, "max_attendees": 300, "service_type": "Music", "phone": "111-111-1119"},
            {"name": "Service B", "location": "Laval", "cost": 200, "max_attendees": 50, "service_type": "Catering", "phone": "111-111-1110"},
            {"name": "Service B", "location": "Laval", "cost": 350, "max_attendees": 75, "service_type": "Music", "phone": "111-111-1121"},
        ]
    def start(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.is_logged_in = self.auth.login(username, password)
        
        if self.is_logged_in:
            print("Login successful!")
            self.navigate()
        else:
            print("Invalid credentials.")

    def navigate(self):
        while True:
            print("\n1. Venues\n2. Services\n3. Search Tool\n4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.venues_page()
            elif choice == "2":
                self.services_page()
            elif choice == "3":
                self.search_tool_page()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    #Defining Service Class
    def services_page(self):
        print("Welcome to the Services page!\n")
        for service in self.services:
            print(f"Name: {service['name']}")
            print(f"Location: {service['location']}")
            print(f"Cost: ${service['cost']}")
            print(f"Maximum Attendees: {service['max_attendees']}")
            print(f"Service Type: {service['service_type']}")
            print(f"Phone Number: {service['phone']}\n")

      #Defining Venue Class
    def venues_page(self):
        print("Welcome to the Venues page!\n")
        for venue in self.venues:
            print(f"Name: {venue['name']}")
            print(f"Location: {venue['location']}")
            print(f"Cost: ${venue['cost']}")
            print(f"Maximum Capacity: {venue['max_capacity']}")
            print(f"Phone Number: {venue['phone']}\n")

    #Defining Search Tool Function
    def search_tool_page(self):
        print("Welcome to the Search Tool page!\n")
        choice = input("Search for (1) Venue or (2) Service? Enter 1 or 2: ")

        if choice == "1":
            self.search_venue()
        elif choice == "2":
            self.search_service()
        else:
            print("Invalid choice. Please try again.")

    def search_venue(self):
        budget = float(input("Enter your budget for the venue: "))
        attendees = int(input("Enter estimated number of attendees: "))
        location = input("Enter the desired location (leave blank for all locations): ")

        matches = [venue for venue in self.venues if venue['cost'] <= budget 
                   and venue['max_capacity'] >= attendees 
                   and (location.lower() in venue['location'].lower() or not location)]

        if matches:
            print("\nMatching Venues:")
            for venue in matches:
                print(f"Name: {venue['name']}, Location: {venue['location']}, Cost: ${venue['cost']}, Capacity: {venue['max_capacity']}")
        else:
            print("No matching venues found.")

    def search_service(self):
        budget = float(input("Enter your budget for the service: "))
        attendees = int(input("Enter estimated number of attendees: "))
        location = input("Enter the desired location (leave blank for all locations): ")

        matches = [service for service in self.services if service['cost'] <= budget 
                   and service['max_attendees'] >= attendees 
                   and (location.lower() in service['location'].lower() or not location)]

        if matches:
            print("\nMatching Services:")
            for service in matches:
                print(f"Name: {service['name']}, Location: {service['location']}, Cost: ${service['cost']}, Max Attendees: {service['max_attendees']}, Type: {service['service_type']}")
        else:
            print("No matching services found.")

# Run App
app = MyApp()
app.start()


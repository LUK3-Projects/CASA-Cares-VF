import webbrowser
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from PIL import Image, ImageTk


# Define Venue Class
class Venue:
    def __init__(self, name, budget, location, max_capacity, image_path, phone_number):
        self.name = name
        self.budget = budget
        self.location = location
        self.max_capacity = max_capacity
        self.image_path = image_path
        self.phone_number = phone_number


 # Define Services Class
class Services:
    def __init__(self, name, location, budget, service_type, image_path, phone_number):
        self.name = name
        self.location = location
        self.budget = budget
        self.service_type = service_type
        self.image_path = image_path
        self.phone_number = phone_number

# Create a list of venues using the Venue class
venues = [
    Venue("Venue A", "$1000", "City A", 200, "venueA.jpg", "123-456-1111"),
    Venue("Venue B", "$1500", "City B", 150, "venueB.jpg", "123-456-1112"),
    Venue("Venue C", "$2000", "City C", 100, "venueC.jpg", "123-456-1113"),
    Venue("Venue D", "$500", "City D", 50, "venueD.jpg", "123-456-1114"),
]

# Create a list of services using the Services Class
services = [
    Services("Service 1", "Location 1", "$1000", "Type A", "service1.jpg", "123-456-1115"),
    Services("Service 2", "Location 2", "$1500", "Type B", "service2.jpg", "123-456-1116"),
    Services("Service 3", "Location 3", "$100", "Type C", "service3.jpg", "123-456-1117"),
    Services("Service 4", "Location 4", "$500", "Type D", "service4.jpg", "123-456-1118"),
]

# Create the main window
root = tk.Tk()
root.title("Venue Viewer")
# Define chosen font from UI/UX team
#custom_font = Font(family="X", size=20)

# Create a Notebook widget for tabs
notebook = ttk.Notebook(root)

# Creating user DB
users = {
    'Admin': {'password': 'password1'},
    'Worker': {'password': 'password2'},
    # Add more users as needed
}

# Login page main function design start:

# Define a global variable to keep track of login attempts
login_attempts = 0
locked_until = None

# Define login function
def login():
    global current_user, login_attempts, locked_until
    
    if locked_until and datetime.datetime.now() < locked_until:
        remaining_time = (locked_until - datetime.datetime.now()).seconds
        confirmation_label.config(text=f"", foreground='red')
        return  # Do not proceed with login
    else:
        confirmation_label.config(text='')

    username = username_entry.get()
    password = password_entry.get()

    if username in users and users[username]['password'] == password:
        # Successful login
        current_user = users[username]
        confirmation_label.config(text='Login successful', foreground='green')
        notebook.tab(1, state='normal')  # Enable Venues tab
        notebook.tab(2, state='normal')  # Enable Services tab
        notebook.tab(3, state='normal')  # Enable Search Venues tab
        credits_label.config(text='')  # Reset credits_label
        login_attempts = 0  # Reset login attempts
    else:
        # Failed login
        login_attempts += 1
        if login_attempts >= 3:
            # Lock login for 1 minute
            locked_until = datetime.datetime.now() + datetime.timedelta(minutes=1)
            login_attempts = 0  # Reset login attempts after locking
        confirmation_label.config(text='Invalid credentials', foreground='red')
        update_timer()

def update_timer():
    global locked_until
    if locked_until and datetime.datetime.now() < locked_until:
        remaining_time = (locked_until - datetime.datetime.now()).seconds
        timer_label.config(text=f"Too many invalid logins, please wait {remaining_time} seconds in order to try again.")
        root.after(1000, update_timer)  # Update every second
    else:
        timer_label.config(text='')

# Define Call function
def initiate_call(phone_number):
    # Use the webbrowser module to open the default VoIP application with the provided phone number
    webbrowser.open(f"tel:{phone_number}")

# Login page design START ---------------------------------------------------------------

# Create Login Tab
login_tab = ttk.Frame(notebook)
notebook.add(login_tab, text='Login')

# Load the CCLogo image
desired_width = 200 # Adjust desired width
desired_height = 200  # Adjust desired height
cc_logo = Image.open("CClogo.png")
cc_logo = cc_logo.resize((desired_width, desired_height), Image.ANTIALIAS)
cc_logo = ImageTk.PhotoImage(cc_logo)

# Place the logo in the login tab
logo_label = ttk.Label(login_tab, image=cc_logo)
logo_label.grid(row=0, column=0, columnspan=2, pady=(20, 0))

# Assign the image to the label to prevent garbage collection
logo_label.image = cc_logo

# Username Entry
# Example Code for font testing
#username_label = ttk.Label(login_tab, text="Username:", font=custom_font)
username_label = ttk.Label(login_tab, text="Username:")
username_label.grid(row=1, column=0, padx=(50, 5), pady=(10, 5), sticky='e')
username_entry = ttk.Entry(login_tab)
username_entry.grid(row=1, column=1, padx=5, pady=(10, 5), sticky='w')

# Password Entry
password_label = ttk.Label(login_tab, text="Password:")
password_label.grid(row=2, column=0, padx=(50, 5), pady=5, sticky='e')
password_entry = ttk.Entry(login_tab, show='*')
password_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

# Login Button
login_button = ttk.Button(login_tab, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=(10, 20))

# Credit label in the GUI
credits_label = ttk.Label(login_tab)
credits_label.grid(row=4, column=0, columnspan=2, pady=(0, 5))

# Confirmation label in the GUI
confirmation_label = ttk.Label(login_tab, text='', font=('Arial', 12))
confirmation_label.grid(row=5, column=0, columnspan=2, pady=(0, 20))

# Center everything
login_tab.grid_rowconfigure(6, weight=1)
login_tab.grid_columnconfigure((0,1), weight=1)

# binding return to enter
username_entry.bind('<Return>', lambda event: login())
password_entry.bind('<Return>', lambda event: login())

# lockout timer
timer_label = ttk.Label(login_tab, text='', font=('Arial', 12))
timer_label.grid(row=6, column=0, columnspan=2, pady=(0, 20))


# Login page design END ---------------------------------------------------------

# Venue Tab design START --------------------------------------------------------

# Create Venue Tab
venue_tab = ttk.Frame(notebook)
notebook.add(venue_tab, text='Venues')

# Disable the Venues tab initially
notebook.tab(1, state='disabled')

# Display venues with resized images and information
for i, venue in enumerate(venues):
    image = Image.open(venue.image_path)
    image = image.resize((200, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    label = ttk.Label(venue_tab, image=image)
    label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

    info = f"Name: {venue.name}\nBudget: {venue.budget}\nLocation: {venue.location}\nMax Capacity: {venue.max_capacity}"
    info_label = ttk.Label(venue_tab, text=info, justify='left')
    info_label.grid(row=i, column=1, padx=5, pady=5, sticky='w')

    #testing
    # call button venue
    call_button = ttk.Button(venue_tab, text="Call", command=lambda number=venue.phone_number: initiate_call(number))
    call_button.grid(row=i, column=2, padx=5, pady=5, sticky='w')

    label.image = image

#Venue Tab Design END------------------------------------------------------------------

#Service Tab design START-----------------------------------------------------------------------------

# Create Services Tab
services_tab = ttk.Frame(notebook)
notebook.add(services_tab, text='Services')
# Disable the Services tab initially
notebook.tab(2, state='disabled')

# Display services with resized images and information
for i, service in enumerate(services):
    image = Image.open(service.image_path)
    image = image.resize((200, 150), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    label = ttk.Label(services_tab, image=image)
    label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

    info = f"Name: {service.name}\nLocation: {service.location}\nBudget: {service.budget}\nType: {service.service_type}"
    info_label = ttk.Label(services_tab, text=info, justify='left')
    info_label.grid(row=i, column=1, padx=5, pady=5, sticky='w')

    #testing
    #call button services
    call_button = ttk.Button(services_tab, text="Call", command=lambda number=service.phone_number: initiate_call(number))
    call_button.grid(row=i, column=2, padx=5, pady=5, sticky='w')

    label.image = image

    # Function to search for services
def search_services():
    desired_location = location_entry_services.get()
    min_budget = budget_min_entry_services.get()
    max_budget = budget_max_entry_services.get()
    service_type = service_type_entry.get()

    # Error handling to ensure valid integers are provided
    try:
        min_budget = int(min_budget)
        max_budget = int(max_budget)
    except ValueError:
        # If conversion to integer fails, set values to 0
        min_budget = 0
        max_budget = float('inf')  # Use infinity as the default maximum budget

    # Filter services based on search parameters
    search_results = []
    for service in services:
        if (desired_location == '' or desired_location.lower() in service.location.lower()) and \
           (min_budget <= int(service.budget[1:]) <= max_budget) and \
           (service_type == '' or service_type.lower() in service.service_type.lower()):
            search_results.append(service)

    # Display search results
    display_search_results_services(search_results)

# Create Search Tab DESIGN---------------------------------------------------------------------------------------

#Search results logic

search_results_frame = None
# Function to search for venues
def search_venues():
    desired_location = location_entry.get()
    min_budget = budget_min_entry.get()
    max_budget = budget_max_entry.get()
    min_capacity = capacity_min_entry.get()
    max_capacity = capacity_max_entry.get()

    # Error handling to ensure valid integers are provided
    try:
        min_budget = int(min_budget)
        max_budget = int(max_budget)
        min_capacity = int(min_capacity)
        max_capacity = int(max_capacity)
    except ValueError:
        # If conversion to integer fails, set values to 0
        min_budget = 0
        max_budget = float('inf')  # Use infinity as the default maximum budget
        min_capacity = 0
        max_capacity = float('inf')  # Use infinity as the default maximum capacity

    # Filter venues based on search parameters
    search_results = []
    for venue in venues:
        if (desired_location == '' or desired_location.lower() in venue.location.lower()) and \
           (min_budget <= int(venue.budget[1:]) <= max_budget) and \
           (min_capacity <= venue.max_capacity <= max_capacity):
            search_results.append(venue)

    # Display search results
    display_search_results(search_results)

# Function to display search results for Venues
def display_search_results(results):
    # Clear previous search results (if any)
    for widget in search_results_frame.winfo_children():
        widget.destroy()

    for i, venue in enumerate(results):
        image = Image.open(venue.image_path)
        image = image.resize((200, 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        label = ttk.Label(search_results_frame, image=image)
        label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

        info = f"Name: {venue.name}\nBudget: {venue.budget}\nLocation: {venue.location}\nMax Capacity: {venue.max_capacity}"
        info_label = ttk.Label(search_results_frame, text=info, justify='left')
        info_label.grid(row=i, column=1, padx=5, pady=5, sticky='w')

        call_button = ttk.Button(search_results_frame, text="Call", command=lambda number=venue.phone_number: initiate_call(number))
        call_button.grid(row=i, column=2, padx=5, pady=5, sticky='w')

        label.image = image

search_tab = ttk.Frame(notebook)
notebook.add(search_tab, text='Search')

# Disable search tab initially until login
notebook.tab(3, state='disabled')  

# Create a frame for venue search parameters
venue_search_parameters_frame = ttk.LabelFrame(search_tab, text="Venue Search Parameters")
venue_search_parameters_frame.grid(row=0, column=0, padx=10, pady=10, sticky='w')

# Location Entry for Venues
location_label = ttk.Label(venue_search_parameters_frame, text="Desired Location:")
location_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
location_entry = ttk.Entry(venue_search_parameters_frame)
location_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Budget Range Entry for Venues
budget_range_label = ttk.Label(venue_search_parameters_frame, text="Budget Range (Min - Max):")
budget_range_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
budget_min_entry = ttk.Entry(venue_search_parameters_frame)
budget_min_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
budget_max_entry = ttk.Entry(venue_search_parameters_frame)
budget_max_entry.grid(row=1, column=2, padx=5, pady=5, sticky='w')

# Capacity Range Entry for Venues
capacity_range_label = ttk.Label(venue_search_parameters_frame, text="Capacity Range (Min - Max):")
capacity_range_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
capacity_min_entry = ttk.Entry(venue_search_parameters_frame)
capacity_min_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
capacity_max_entry = ttk.Entry(venue_search_parameters_frame)
capacity_max_entry.grid(row=2, column=2, padx=5, pady=5, sticky='w')

# Search Button for Venues
search_button_venues = ttk.Button(venue_search_parameters_frame, text="Search Venues", command=search_venues)
search_button_venues.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky='w')


# Create a frame for search results for Venues
search_results_frame_venues = ttk.Frame(search_tab)
search_results_frame_venues.grid(row=1, column=0, padx=10, pady=10, sticky='w')
search_results_frame = search_results_frame_venues

# Create a frame for service search parameters on the Search Tab
service_search_parameters_frame = ttk.LabelFrame(search_tab, text="Service Search Parameters")
service_search_parameters_frame.grid(row=0, column=1, padx=10, pady=10, sticky='w')  

# Location Entry for Services
location_label_services = ttk.Label(service_search_parameters_frame, text="Desired Location:")
location_label_services.grid(row=0, column=0, padx=5, pady=5, sticky='w')
location_entry_services = ttk.Entry(service_search_parameters_frame)
location_entry_services.grid(row=0, column=1, padx=5, pady=5, sticky='w')

# Budget Range Entry for Services
budget_range_label_services = ttk.Label(service_search_parameters_frame, text="Budget Range (Min - Max):")
budget_range_label_services.grid(row=1, column=0, padx=5, pady=5, sticky='w')
budget_min_entry_services = ttk.Entry(service_search_parameters_frame)
budget_min_entry_services.grid(row=1, column=1, padx=5, pady=5, sticky='w')
budget_max_entry_services = ttk.Entry(service_search_parameters_frame)
budget_max_entry_services.grid(row=1, column=2, padx=5, pady=5, sticky='w')

# Type of Service Entry
service_type_label = ttk.Label(service_search_parameters_frame, text="Type of Service:")
service_type_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
service_type_entry = ttk.Entry(service_search_parameters_frame)
service_type_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

# Search Button for Services
search_button_services = ttk.Button(service_search_parameters_frame, text="Search Services", command=search_services)
search_button_services.grid(row=3, column=0, padx=5, pady=5, sticky='w')

# Create a frame for search results for Services
search_results_frame_services = ttk.Frame(search_tab)
search_results_frame_services.grid(row=3, column=0, padx=10, pady=10, sticky='w')
search_results_frame = search_results_frame_services


# Function to display search results for Services
def display_search_results_services(results):
    for widget in search_results_frame_services.winfo_children():
        widget.destroy()

    for i, service in enumerate(results):
        image = Image.open(service.image_path)
        image = image.resize((200, 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

        label = ttk.Label(search_results_frame_services, image=image)
        label.grid(row=i, column=0, padx=5, pady=5, sticky='w')

        info = f"Name: {service.name}\nLocation: {service.location}\nBudget: {service.budget}\nType: {service.service_type}"
        info_label = ttk.Label(search_results_frame_services, text=info, justify='left')
        info_label.grid(row=i, column=1, padx=5, pady=5, sticky='w')

        call_button = ttk.Button(search_results_frame_services, text="Call", command=lambda number=service.phone_number: initiate_call(number))
        call_button.grid(row=i, column=2, padx=5, pady=5, sticky='w')

        label.image = image

# Search Tab Design END----------------------------------------------------------------------------------------------------------


# Pack and start main loop
notebook.pack(padx=10, pady=10)
root.mainloop()
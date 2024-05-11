# CASA-Cares-VF
Venue finder app developed for CC non-business use
This is an app designed for BTM 495 section AA under guidance of professor Ka Pong Law.

The main goal of this app is to help combat the redudancy in repeated research within CASA Cares when searching for a venue and stream-line the process all together. 
In line with this goal our app covers 3 main use cases: Displaying Venue information, Displaying Service information and allowing us to search said information for a match to project parameters.

UPDATE 11/21/23: MAJOR REHAUL

To follow project guidelines app has shifted from Procedural paradigm to OOP paradigm. App funcationality has been replicated so forth:

1. login function: Username: Admin   Password: password1
2. Venues tab: display all venues within our placeholder DB (static library). 
3. Service tab: display all services within our placeholder DB (static library).
4. Search Tool: search the placeholder DB for venues and services that match the inputted project parameters:
5.   Parameters are as followed:
6.   Venues: Maximum Budget (Funds to rent venue), Estimated Attendees (Maximum value of possible attendees), Desired Location (Desired city within Quebec)
7.   Services: Maximum Budget (Funds to hire services), Estimated Attendees (Maximum value of possible attendees), Desired location (Desired city within Quebec), Service Type (Type of service you want to hire).

NOTES: 
1. Parameters: Locations available: Montreal, Quebec City, Laval.
                Service types available: Catering, Music.

2. tkinter GUI removed and opted to keep it simple with a terminal interface. 

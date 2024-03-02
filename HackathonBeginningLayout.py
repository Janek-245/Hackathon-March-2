from dataclasses import dataclass
@dataclass
class activity_info:
    activity: str
    location:str
    schedule: schedule
    slots: int
    price: price
    contact: str
class schedule:
    Sunday: str
    Monday: str
    Tuesday: str
    Wednesday: str
    Thursday: str
    Friday: str
    Saturday: str
class contact:
    phone: str
    email: str
    website: str
class price:
    adults: str
    minors: str
    special: str
def activity_price(activity:str) -> price:
    if activity == activities[0]:
        return price("Admission for adults: $28", "Admission for minors: $25", "")
    elif activity == activities[1]:
        return price("Admission for adults: $9", "Admission for minors: $7", """Seniors admission: $8.00 \n 
                     Free from December 1 to March 15""")
    elif activity == activities[2]:
        return price("3 years+ admissoin: $14.50", "1-2 years admission: $4.25", "")
    elif activity == activities[3]:
        return price("Admission for adults: $18", "Admission for minors: $7", "")
activities = ["Axxiom Escape Rooms Newark", "Brandywine Zoo", "Delaware Museum of Nature & Science",
              "Delaware Art Museum"]
activityInfo = [activity_info("Axxiom Escape Rooms Newark", "280 E Main St, DE 19711", activity_price(activities[0])), 
                activity_info("Brandywine Zoo", "1001 N Park Dr, Wilmington, DE 19802", activity_price(activities[1])),
                activity_info("Delaware Museum of Nature & Science", "4840 Kennett Pike, Wilmington, DE 19807", activity_price(activities[2])),
                activity_info("Delaware Art Museum", "2301 Kentmere Pkwy, Wilmington, DE 19806", activity_price[3])]
def execute(command: str):
    print('For usable commans enter "HELP"')
    command = input("What would you like to know?")
    if command == "activity":
        print(activities)
        return "";
    elif command == "HELP":
        print("""Input commands below for desired information:
              ACTIVITIES: gives a list of possible activities
              SCHEDULE('name of activity'): gives schedule correspodent to particular activity,
              PRICE('name of activity'): price of activity
              LOCATION('name of activity'): location of activity
              CONTACT('name of activity'): contact information for activity""")
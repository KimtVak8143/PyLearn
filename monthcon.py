# Month Conversions
# Concept - Dictionary , .get(), .lower()


conversions = {
    "jan": "January", "feb": "February", "mar": "March",
    "apr": "April", "may": "May", "jun": "June", "jul": "July",
    "aug": "August", "sep": "September", "oct": "October",
    "nov": "November", "dec": "December"
}

mon_input = str(input("Enter the initials of Month :\t")).lower()
print(conversions.get(mon_input, "Invalid input"))

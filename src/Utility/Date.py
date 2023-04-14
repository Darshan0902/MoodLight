# File  : Date.py
# Contains the class Date, that are used to
# Save information about date and operate the information

class Date:
    # CONSTRUCTOR
    # Default constructor 
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0
    
    # Take a string of date and turn it into appropriate attributes
    # Format : DD-MM-YYYY
    def __init__(self, dateString):
        self.day = int(dateString[0:2])
        self.month = int(dateString[3:5])
        self.year = int(dateString[6:])

    # COMPARATOR
    # Return true if this date is after the other date, otherwise return false
    def __gt__(self, other):
        return ((self.year > other.year) or 
                (self.year == other.year and self.month > other.month) or 
                (self.year == other.year and self.month == other.month and self.day > other.day))
    
    # Return true if this date is the same as other date, otherwise return false
    def __eq__(self, other):
        return (self.year == other.year and self.month == other.month and self.day == other.day)
    
    # Return true if this date is before the other date, otherwise return false
    def __lt__(self, other):
        return (not self > other and not self == other)
    
    # STRING TRANSFORM
    # Return the string representation of date object in format DD-MM-YYYY
    def toString(self):
        result = ""

        if (self.day < 10):
            result += f"0{self.day}-"
        else:
            result += f"{self.day}-"
        if (self.month < 10):
            result += f"0{self.month}-"
        else:
            result += f"{self.month}-"
        result += f"{self.year}"

        return result
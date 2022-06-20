""" This file is the equivalent to the Rohan.java class in the ForRohan project. """
import ex

#If the school is not some version of the University of South Carolina a RohanException is thrown
#If school equals None an AttributeError is thrown.
def school_error_checking(schl):
    school = schl.lower()
    if (school != "usc" and school != "uofsc" and school != "the university of south carolina"
       and school != "university of south carolina" and school != "south carolina"):

       message = "Rohan doesn't attend \"" + schl + "\"!"
       raise ex.RohanException(message)

    if school == None:
        raise AttributeError("School cannot equal None.");

#If the mascot equals None an AttributeError is thrown
def mascot_error_checking(mascot):
    if mascot == None:
        raise AttributeError("Mascot cannot equal None")

#If Rohans favorite sport is not golf or football a RohanException is thrown.
def sport_error_checking(spt):
    sport = spt.lower()
    if sport != "football" and sport != "golf":
        raise ex.RohanException()

#Appends the string "lol" to the mascot variable if cock
#is a substring of mascot.
def haha_funny(mascot):
    if "cock" in mascot.lower():
        mascot += " (lol)"
    return mascot

#Calculates Rohans age given the current date.
def calc_age(date):
    dates = [int(i) for i in date.split("/")]

    if dates[0] > 12 or dates[0] <= 0:
        raise Exception("Month in date is wrong ")

    if dates[1] > 31 or dates[1] <= 0:
        raise Exception("Day in date is wrong ")
        
    if dates[2] > 2022 or dates[2] <= 2002:
        raise Exception("Year in date is wrong. Rohan wasn't alive!")

    months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    rohansBirthDay = [4, 9, 2002]

    days = 0;

    for i in range(rohansBirthDay[0] + 1, dates[0]):
        days += months[i]

    days += dates[1] + (months[rohansBirthDay[0]] - rohansBirthDay[1])

    percent = days / 365.0;
    almostFinalAge = (dates[2] - rohansBirthDay[2]) + percent;

    return str("{:.2f}".format(almostFinalAge))

#Throws exception if a slash character is not in the parameter
def date_error_checking(date):
    if "/" not in date:
        raise Exception("Date not formatted properly.");

"""Error checks parameters and constructs a Rohan object"""
class Rohan:

    #Constructs a Rohan Object
    def __init__(self, school, date, mascot, sport):
        school_error_checking(school)
        date_error_checking(date)
        mascot_error_checking(mascot)
        sport_error_checking(sport)

        self.school = school
        self.age = calc_age(date)
        self.mascot = haha_funny(mascot)
        self.sport = sport

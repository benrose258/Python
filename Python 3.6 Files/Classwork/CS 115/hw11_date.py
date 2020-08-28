'''
Created on Apr 17, 2017

@author: Ben Rose

Pledge: I pledge my honor that I have abided by the Stevens Honor System. -Ben Rose

Homework 11
'''

DIM = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#Days in Month ^^

DIW = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
#Days in a Week ^^

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day

    def tomorrow(self):
        '''Changes self.month,self.year, and self.day to the next day. If it isn't the end of the month,
        just add 1 to the day. If it is the end of the month but not the end of the year, then add 1 to the
        month and set the day equal to 1. If it is the last day of the end of the year, set the month equal
        to 1, set the day equal to 1, and add 1 to the year. And if it is a leap year, february, and it is the 28th,
        then we will only add 1 to the date, as we have 1 more day that month.'''
        if self.day >= DIM[self.month]:
            if self.month == len(DIM) - 1:
                self.month = 1
                self.day = 1
                self.year += 1
            elif self.isLeapYear() == True and self.month == 2 and self.day == 28:
                self.day += 1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1

    def yesterday(self):
        '''If it is the first day of the month and the first month of the year, the month loops back to 12, the day is the last
           day of the month (31 in this case), and subtract 1 from the year. If it is a leap year, march, and the first day of
           march, then subtract 1 from the month and the day is the last day of february (28) plus 1 (29) to give us the correct
           day for the leap year. If it is the first day of the month, but nothing of note, subtract 1 from the month and set
           the day equal to the last day of that month. If none of the above conditions are met, just subtract 1 from the day.'''
        if self.day == 1:
            if self.month == 1:
                self.month = 12
                self.day = DIM[self.month]
                self.year -= 1
            elif self.isLeapYear() == True and self.month == 3:
                self.month -= 1
                self.day = DIM[self.month] + 1
            else:
                self.month -= 1
                self.day = DIM[self.month]
        else:
            self.day -= 1

    def addNDays(self,mynum):
        '''Takes in a number. First prints the initial date value, then enters a while loop. While
           the amount of days we have added does not exceed our counter "addedDays", add a day to
           self, print it, and add 1 to our counter. This function stops when the counter equals
           the number we put in.'''
        addedDays = 0
        print(self)
        while mynum != addedDays:
            self.tomorrow()
            print(self)
            addedDays += 1

    def subNDays(self,mynum):
        '''Takes in a number. First prints the initial date value, then enters a while loop. While
           the amount of days we have subtracted does not exceed our counter "subtractedDays", subtract a day from
           self, print it, and add 1 to our counter. This function stops when the counter equals
           the number we put in.'''
        subtractedDays = 0
        print(self)
        while mynum != subtractedDays:
            self.yesterday()
            print(self)
            subtractedDays += 1

    def isBefore(self,date2):
        '''Returns True if self is before date2 and False if self and date2 are the same or
           if self is after date2.'''
        if self.equals(date2) == True:
            return False
        elif self.year != date2.year:
            return self.year < date2.year
        elif self.month != date2.month:
            return self.month < date2.month
        else:
            return self.day < date2.day

    def isAfter(self,date2):
        '''Returns True if self is after date2 and False if self and date2 are the same or
           if self is after date2. Works by doing isBefore with the variables switched.'''
        return date2.isBefore(self)


    def diff(self,date2):
        '''Returns how many days apart the first and second given date are.'''
        totalDays = 0
        date1 = self.copy()
        while date1.equals(date2) == False:
            if date1.isBefore(date2) == True:
                date1.tomorrow()
                totalDays -= 1
            else:
                date1.yesterday()
                totalDays += 1
        return totalDays

    def dow(self):
        '''Returns the day of the week of self by first determining the number of days since 1,1,1970, then using the
           list of days to determine the day of the week. Since our starting day is a thursday, we will add 4 to account
           for the difference in indices from the beginning of the list (Sunday). Then use that new number % 7 (for the
           amount of days) and return the corresponding day from the DIW list. If you don't understand why I used the
           original date that I did, it is because computers use this date to compute the date and time.'''
        daysFromOrigin = self.diff(Date(1,1,1970))
        return DIW[(daysFromOrigin + 4) % 7]

d = Date(4,15,2017)
endD = Date(7,7,2017)
print(endD.diff(d))

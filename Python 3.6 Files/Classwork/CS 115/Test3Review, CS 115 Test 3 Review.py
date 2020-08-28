'''
Created on Apr 25, 2017

@author: Ben Rose
'''
import sys

#Spring test
'''if __name__ == '__main__':
    try:
        int(input('Please put in an integer> '))
        print('Thanks')
        sys.exit(0)
    except:
        print('No Thanks')
        sys.exit(1)
'''

def sum_rows(mylists):
    finallist = []
    for index in range(len(mylists)):
        sublist = mylists[index]
        mysum = 0
        curindex = 0
        while curindex < len(sublist):
            mysum += sublist[curindex]
            curindex += 1
        finallist.append(mysum)
    return finallist

def sum_negatives_up_to(mylist, target):
    '''Assume lst is a list of integers.
    Return the sum of only negative values up to but not including the
    first occurrence of a number that is >= target.
    If lst is empty, return 0.
    For example,
    sum_negatives_up_to([], 10) should return 0.
    sum_negatives_up_to([-5, -1, 42, -3], 100) should return -9.
    sum_negatives_up_to([1, -3, -8, 9, 2], 5) should return -11.
    '''
    mysum = 0
    for index in mylist:
        if index >= target:
            break
        elif index < 0:
            mysum += index
    return mysum

class Employee(object):
    '''Write the constructor below. It should take in five arguments:
       - first_name (a string)
       - last_name (a string)
       - title (a string)
       - hours_per_week (an int)
       - hourly_rate (a float)
       All fields must be private. No error checking or type conversions
       are required.
       5 points'''
    def __init__(self,first_name,last_name,title,hours_per_week,hourly_rate):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__title = title
        self.__hours_per_week = hours_per_week
        self.__hourly_rate = hourly_rate

    '''Write a property for hourly_rate. 3 points'''
    def hourly_rate(self):
        return self.__hourly_rate

    '''Write a setter for hourly rate. 3 points'''
    def hourly_rate(self,hourly_rate):
        self.__hourly_rate = hourly_rate

    '''Write a method called get_total_compensation.
       It returns the total amount of money an employee earns in a year.
       Assume that the employee works 50 weeks each year, with the remaining
       2 set aside for vacation.
       4 points'''
    def get_total_compensation(self):
        return self.__hourly_rate * self.__hours_per_week * 50

    def __str__(self):
        return 'Employee: %s %s\n  Title: %s\n  Hours per week: %d\n' \
               '  Hourly rate: $%.2f\n  Yearly compensation: $%.2f' % \
            (self.__first_name, self.__last_name, self.__title, \
             self.__hours_per_week, self.__hourly_rate, \
             self.get_total_compensation())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (15 points)
' Implement missing sections of the Manager class. Manager should be a
' subclass of Employee.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Manager(Employee):  # 2 points
    '''Write the constructor below. It should take in six arguments:
    - the first five are the same as in the Employee constructor
    - bonus_percent, a float >= 0. This attribute represents the percentage
      of the employee's yearly compensation that will be used to
      create the manager's annual bonus. MAKE SURE the argument is a float
      >= 0.  Otherwise, if it's not a float raise a TypeError stating,
      "Bonus percent must be a float." If it's a float but < 0, raise a
      ValueError stating, "Bonus percent cannot be negative."
      bonus_percent must be private.
    8 points'''
    def __init__(self,first_name,last_name,title,hours_per_week,hourly_rate,bonus_percent):
        super().__init__(first_name, last_name, title, hours_per_week, hourly_rate)
        try:
            self.__bonus_percent = float(bonus_percent)
        except:
            raise TypeError('Bonus percent must be a float.')
        if self.__bonus_percent < 0:
            raise ValueError('Bonus percent cannot be negative.')

    '''Override the method get_total_compensation.
    It returns the total amount of money the manager earns in a year, i.e.
    basic employee compensation + bonus.
    To get full credit, you must call get_total_compensation in the superclass.
    Note: If a manager's yearly compensation is $100,000 and the bonus_percent
          is 10 (ten), the total compensation will be 110,000.
    5 points'''
    def get_total_compensation(self):
        return super().get_total_compensation() * (1 + self.__bonus_percent / 100)

e = Employee('Ben','Rose','League Champion',1,10000000.00)
m = Manager('Ben','Rose','League Champion',1,10000000.00,10.0)

class Car(object):
    def __init__(self,make,model,mpg,tank_capacity):
        self.__make = make
        self.__model = model
        self.__mpg = mpg
        self.__tank_capacity = tank_capacity

    def mpg(self):
        return self.__mpg

    def tank_capacity(self):
        return self.__tank_capacity

    def mpg(self,mpg):
        self.__mpg = mpg

    def tank_capacity(self,tank_capacity):
        self.__tank_capacity = tank_capacity

    def get_total_range(self):
        return self.__mpg * self.__tank_capacity

    def __str__(self):
        return self.__make + ' ' + self.__model + ', MPG: ' + str(self.__mpg) + ', tank capacity: ' + str(self.__tank_capacity)

mycar = Car('Jeep Grand Cherokee','2018',15,20)
print(mycar)
print()
# Jeep Grand Cherokee 2018, MPG: 15, tank capacity: 20

class HybridCar(Car):
    def __init__(self,make,model,mpg,tank_capacity,battery_kWh,miles_per_kWh):
        super().__init__(make, model, mpg, tank_capacity)
        self.__battery_kWh = battery_kWh
        self.__miles_per_kWh = miles_per_kWh

    def get_battery_range(self):
        return self.__battery_kWh * self.__miles_per_kWh

    def get_total_range(self):
        return super().get_total_range() + self.get_battery_range()

    def __str__(self):
        return super().__str__() + ', battery kWh: ' + str(self.__battery_kWh) + ', miles/kWh: ' + str(self.__miles_per_kWh)

prius = HybridCar('Toyota', 'Prius', 50.2, 8.8, 4.4, 25.8)
print(prius)
print(prius.get_battery_range())
print(prius.get_total_range())

# Toyota Prius, MPG: 50.2, tank capacity: 8.8, battery kWh: 4.4, miles/kWh: 25.8
# 113.52000000000001
# 555.2800000000001

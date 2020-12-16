# ------------------------------------------------------------------------ #
# Title: Assignment 09 - Data Classes
# Description: Data Class module for Assignment 09

# ChangeLog (Who,When,What):
# ALi,Dec. 15, 2020,Created started script
# ------------------------------------------------------------------------ #

# Create Person class
# Create Employee class

if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

class Person(object):   # Inherits from object
    """ Stores data about a person:

    properties:
        first_name: (string) with the person's first name

        last_name: (string) with a person's last name

    methods:
        to_string() returns comma separated product data (alisa for __str__())

    changelog: (When, Who, What)
        ALi, Dec. 15, 2020, Created Class
    """

    # -- Constructor --
    def __init__(self, first_name, last_name):
        # -- Attributes --
        self.__first_name = first_name
        self.__last_name = last_name

    # -- Properties --
    @property
    def first_name(self):
        return str(self.__first_name).title()

    @first_name.setter
    def first_name(self, value):
        if not str(value).isnumeric():
            self.__first_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def last_name(self):
        return str(self.__last_name).title()

    @last_name.setter
    def last_name(self, value):
        if not str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("Names cannot be numbers")

    # -- Methods --
    def to_string(self):
        """ Explicitly returns a string with this object's data"""
        return self.__str__()

    def __str__(self):
        """Implicitly returns a string with this object's data"""
        return self.first_name + "," + self.last_name


class Employee(Person):     # Inherits from Person
    """ Stores data about an Employee:

    properties:
        employee_id: (int) with the employee's ID

        first_name: (string) with the employee's first name

        last_name: (string) with the employee's last name

    methods:
        to_string() returns comma separated product data (alias for __str__())

    changelog: (When, Who, What)
            ALi, Dec. 15, 2020, Created Class
    """

    def __init__(self, employee_id, first_name, last_name):
        # Attributes
        self.__employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name

    # --Properties--
    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, value):
        if str(value).isnumeric():
            self.__last_name = value
        else:
            raise Exception("IDs must by numbers")

    # --Methods--
    def to_strings(self):   # Overrides the original method (polymorphic)
        """ Explicitly returns a string with this object's data """
        # Linking to self.__str__() does not work with inheritance
        data = super().__str__()    # get data from parent(super) class
        return str(self.employee_ID) + "," + data

    def __str__(self): # Overrides the oginal method (polymorphic)
        """ Implicityly returns field data """
        data = super().__str__()    # get data from parent(super) class
        return str(self.employee_id) + "," + data
    # --End of Class--


'''
Builder Method is a Creation Design Pattern which aims to “Separate the construction of a complex object
from its representation so that the same construction process can create different representations.”
It is basically designed to provide flexibility to the solutions to various object creation problems in object-oriented programming.
'''
# Abstract course
class Course:

    def __init__(self):
        self.Fee()
        self.available_batches()

    def Fee(self):
        raise NotImplementedError

    def available_batches(self):
        raise NotImplementedError

    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

# concrete course
class DSA(Course):

    """Class for Data Structures and Algorithms"""

    def Fee(self):
        self.fee = 8000

    def available_batches(self):
        self.batches = 5

    def __str__(self):
        return "DSA"

# concrete course
class SDE(Course):

    """Class for Software Development Engineer"""

    def Fee(self):
        self.fee = 10000

    def available_batches(self):
        self.batches = 4

    def __str__(self):
        return "SDE"

# concrete course
class STL(Course):

    """Class for Standard Template Library"""

    def Fee(self):
        self.fee = 5000

    def available_batches(self):
        self.batches = 7

    def __str__(self):
        return "STL"

# Complex Course
class ComplexCourse:

    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)

# Complex course
class Complexcourse(ComplexCourse):

    def Fee(self):
        self.fee = 7000

    def available_batches(self):
        self.batches = 6

    # def available_time(self):
    #     self.time = 4

# construct course
def construct_course(cls):

    course = cls()
    course.Fee()
    course.available_batches()
    # course.time()
    return course # return the course object

# main method
if __name__ == "__main__":

    dsa = DSA() # object for DSA course
    sde = SDE() # object for SDE course
    stl = STL() # object for STL course

    complex_course = construct_course(Complexcourse)
    print(complex_course)

'''
Advantages of using Builder Method:
Reusability: While making the various representations of the products, we can use the same construction code for other representations as well.
Single Responsibility Principle: We can separate out both the business logic as well as the complex construction code from each other.
Construction of the object: Here we construct our object step by step, defer construction steps or run steps recursively.

Disadvantages of using Builder method:
Code complexity increases: The complexity of our code increases, because the builder pattern requires creating multiple new classes.
Mutability: It requires the builder class to be mutable
Initialization: Data members of the class are not guaranteed to be initialized.
'''


"""Code implemented with Bridge Method.
We have a Cuboid class having three attributes
named as length, breadth, and height and three
methods named as produceWithAPIOne(), produceWithAPItwo(),
and expand(). Our purpose is to separate out implementation
specific abstraction from implementation-independent
abstraction"""

class ProducingAPI1:

	"""Implementation specific Abstraction"""

	def produceCuboid(self, length, breadth, height):

		print(f'API1 is producing Cuboid with length = {length}, '
			f' Breadth = {breadth} and Height = {height}')

class ProducingAPI2:

	"""Implementation specific Abstraction"""

	def produceCuboid(self, length, breadth, height):

		print(f'API2 is producing Cuboid with length = {length}, '
			f' Breadth = {breadth} and Height = {height}')

class Cuboid:

	def __init__(self, length, breadth, height, producingAPI):

		"""Initialize the necessary attributes
		Implementation independent Abstraction"""

		self.length = length
		self.breadth = breadth
		self.height = height

		self.producingAPI = producingAPI

	def produce(self):

		"""Implementation specific Abstraction"""

		self.producingAPI.produceCuboid(self.length, self.breadth, self.height)


"""Instantiate a cuboid and pass to it an
object of ProducingAPIone"""

cuboid1 = Cuboid(5, 7, 9, ProducingAPI1())
cuboid1.produce()

cuboid2 = Cuboid(2, 3, 5, ProducingAPI2())
cuboid2.produce()

'''
Advantage
Single Responsibility Principle: Bridge method clearly follows the Single Responsibility principle as
 it decouple an abstraction from its implementation so that the two can vary independently.
 
Open/Closed Principle: It does not violate the Open/Closed principle because at any time we can 
introduce the new abstractions and implementations independently form each other

Platform independent feature: Bridge Method can be easily used for implementing the platform 
independent features.

Disadvantage

Complexity: Our code might become complexive after applying Bridge method because we are introding 
new abstarction classes and interfaces.

Double Indirection: Bridge method might have slight negative impact on the preformance because the
 abstraction needs to pass messages along with the implementation for the operation to get executed.
Interfaces with only single implementation: If we have only limited interfaces, then it doesn’t 
sweat a breath but if you have an exploded set of interfaces with minimal or only one implementation
 it becomes hard to manage
'''
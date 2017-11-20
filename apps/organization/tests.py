from django.test import TestCase

# Create your tests here.


class Animal(object):
    def run(self):
        print('Animal is running....')

def run_twice(animal):
    animal.run()
    animal.run()



class Dog(Animal):
    def run(self):
        print('dog is running')

    def eat(self):
        return 'eatting meat...'


print(run_twice(Animal()))


print(run_twice(Dog()))
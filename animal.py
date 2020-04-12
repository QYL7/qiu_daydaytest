class Animal(object):
    def run(self):
        print("animal is running")


class Dog(Animal):
    def run(self):
        print('dog is running')

def run_twice(animal):
    animal.run()
    animal.run()

#run_twice(Animal())  #传入Animal的实例
# run_twice(Dog())  #传入Dog的实例
class Timer(object):
    def run(self):
        print('Start time')

#run_twice(Timer()) #传入Timer的实例
dog = Dog()
print(dir(dog))


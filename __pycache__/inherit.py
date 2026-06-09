# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks.")

# d= Dog("Buddy")
# d.speak()
# print(d.name)

class Vehicle:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is a cruise bike.")

d= Vehicle("Interceptor")        
d.speak()
print(d.name)
class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        # Introduce the person by printing their information
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alex", 30, "Male")

# Call the introduce method
person1.introduce()

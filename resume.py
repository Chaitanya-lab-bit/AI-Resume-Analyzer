class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Person:", self.name)


class Resume(Person):

    def __init__(self, name, email, phone):
        super().__init__(name)
        self.email = email
        self.phone = phone

    # Method Overriding (Polymorphism)
    def display(self):
        print("\n===== Candidate Details =====")
        print("Name :", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)
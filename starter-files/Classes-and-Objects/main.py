class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self):
        # pass

    def change_name(self, name):
        self.name = name



# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
Bob = Student("Peter")
# Expected methods
Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()

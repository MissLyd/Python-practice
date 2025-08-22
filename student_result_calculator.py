# this project collects averages from a defined number of students as well as coefficients.
# It calculates the overall mark and decides on the students' status(failed or succeeded) and prints it.
# It then stores the students' names and status into a dictionary and prints it.

# we're choosing three subjects and their coefficients, as well as their sum
math_coeff, science_coeff, sport_coeff = 5, 3, 1
coeff_sum=sum([math_coeff,science_coeff,sport_coeff]) 

# we're creating a Student class with the instance variables "name" and all the marks
class Student:
    def __init__(self, name, math_mark, science_mark, sport_mark):
        self.name = name 
        self.overall_mark = self.overall_mark_calculator(math_mark,science_mark,sport_mark)
        self.status = "succeded" if self.overall_mark >= 10 else "failed"
    
    # calculating the average
    def overall_mark_calculator(self, math_mark, science_mark, sport_mark):
        return (math_mark*math_coeff+science_mark*science_coeff+sport_mark*sport_coeff)/coeff_sum
    
    #what gets printed if we print(student)
    def __str__(self):
        return f"{self.name} has {self.status} with an overall mark of {self.overall_mark:.2f}"
    
    #here __repr__ is what gets printed when you call Student(), it's essentially a string representation of the class
    # we will use it to fill the dictionary
    def __repr__(self):
        return f"Student({self.name},{self.status})"
    
# the students' names and status get stored in the dictionary "students"
students = {}

#storing the number of students in a variable
nbr = int(input("Enter the number of students: ").strip())

for _ in range(nbr):
    #collecting all the variables
    name = input("Enter your name: ").strip()
    math_mark = float(input("Enter your math mark /20: ").strip())
    science_mark = float(input("Enter your science mark /20: ").strip())
    sport_mark = float(input("Enter your sport mark /20: ").strip())

    #we can see the use of __repr__
    students [name]= Student( name,math_mark, science_mark, sport_mark)

#printing the statement in __str__ directly from,the dictionary
for student in students.values():
    print(student)

#printing the dictionary itself
print (students)
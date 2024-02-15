
# Question 1
employee_salaries = {}

while True:
    name = input("Enter employee name (or 'no' to stop): ")
    if name.lower() == 'no':
        break
    salary = float(input("Enter employee salary: "))
    employee_salaries[name] = salary

print("Employee data stored in dictionary:", employee_salaries)


# Question 2
numbers_list = []
for i in range(10):
    value = int(input("Enter a number: "))
    numbers_list.append(value)

largest_number = numbers_list[0]
for num in numbers_list:
    if num > largest_number:
        largest_number = num

print("The largest number in the list is:", largest_number)


# Question 3
celsius_temperature = float(input("Enter Celsius temperature: "))
fahrenheit_temperature = 9/5 * celsius_temperature + 32
print("Equivalent Fahrenheit temperature:", fahrenheit_temperature)


# Question 4
number = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")


# Question 5
x = int(input("Enter a number of repetitions: "))

def repeat_decorator(func):
    def wrapper():
        for _ in range(x):
            func()
    return wrapper

@repeat_decorator
def hello():
    print('Hello')

hello()

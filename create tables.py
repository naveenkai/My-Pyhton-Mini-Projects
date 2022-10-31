from tabulate import tabulate
data = [["Name", "Place", "Gender"], ["Naveen K", "Bengaluru", "Male"], ["Hritika", "New Delhi", "Female"], ["Krishna", "UP", "Male"]]
print(tabulate(data))

print(tabulate(data, headers='firstrow'))

print(tabulate(data, headers='firstrow', tablefmt='grid'))

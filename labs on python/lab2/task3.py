import random


months = [
    "Січень", "Лютий", "Березень", "Квітень",
    "Травень", "Червень", "Липень", "Серпень",
    "Вересень", "Жовтень", "Листопад", "Грудень"
]

salary = []
for i in range(10):
    row = []
    for j in range(12):

        row.append(random.randint(1000, 55000))
    salary.append(row)

print("Зарплати 10 працівників за 12 місяців:\n")
for i in range(10):
    print(f"Працівник {i+1:2}: ", end="")
    for j in range(12):
        print(f"{salary[i][j]:7}", end=" ")
    print()

print("\nЗагальна зарплата кожного працівника за рік:")
for i in range(10):
    total = sum(salary[i])
    print(f"Працівник {i+1:2}: {total:8}")

print("\nСередня зарплата по місяцях:")
for j in range(12):
    month_sum = 0
    for i in range(10):
        month_sum += salary[i][j]
    avg = month_sum / 10
    print(f"{months[j]:9}: {avg:8.2f}")

def input_array():
    while True:
        try:
            n = int(input("Введіть n (>0): ").strip())
            if n <= 0:
                print("n має бути додатнім.")
                continue
            break
        except ValueError:
            print("Потрібне ціле число.")
    arr, need = [], n
    print(f"Введіть {n} цілих (через пробіл/рядки):")
    while need > 0:
        for token in input().split():
            try:
                arr.append(int(token))
                need = need - 1
                if need == 0: break
            except ValueError:
                print(f"Пропущено неціле '{token}'.")
    return arr

def sum_of_uniques(arr):
    total = 0
    for x in arr:
        if arr.count(x) == 1:
            total += x
    return total

def print_result(s):
    print("Сума унікальних елементів:", s)

def main():
    a = input_array()
    s = sum_of_uniques(a)
    print_result(s)

if __name__ == "__main__":
    main()

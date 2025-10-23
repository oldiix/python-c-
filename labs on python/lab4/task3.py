import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import datetime
import os

INPUT_FILE = "Input_data.txt"
OUTPUT_FILE = "Output_data.txt"
LOG_FILE = "Session_log.txt"


def log_action(action):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        f.write(f"[{time}] Дія: {action}\n")


def start_session():
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write(f"Нова сесія: {datetime.datetime.now()} ---\n")
    log_action("додаток запущено")


def close_session():
    log_action("додаток закрито")


def import_data():
    try:
        if not os.path.exists(INPUT_FILE):
            raise FileNotFoundError("Файл не знайдено")

        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data = f.read().strip()

        if not data:
            raise ValueError("Файл порожній")

        input_entry.delete(0, tk.END)
        input_entry.insert(0, data)
        messagebox.showinfo("Успіх", f"Вхідні дані імпортовано: {data}")
        log_action("імпортовано вхідні дані")
    except FileNotFoundError:
        messagebox.showerror("Помилка", "Файл порожній або відсутній. Введіть дані вручну.")
    except ValueError as e:
        messagebox.showerror("Помилка", str(e))

def calculate():
    try:
        data = input_entry.get().strip()
        if not data:
            raise ValueError("Введіть дані!")

        parts = data.split()
        if len(parts) != 2:
            raise ValueError("Недопустимі вхідні параметри!")

        num1, num2 = map(float, parts)

        op = operation_var.get()
        log_action(f"обрано арифметичну операцію ({op})")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                raise ZeroDivisionError("Ділення на 0 заборонено!")
            result = num1 / num2
        elif op == "^":
            result = num1 ** num2
        else:
            raise ValueError("Невідома операція!")

        output = f"{num1} {op} {num2} = {result}"
        result_label.config(text=f"Результат: {output}")
        log_action("обчислено вираз")
        return output

    except ValueError as e:
        messagebox.showerror("Помилка", str(e))
        log_action("некоректні дані користувача")
    except ZeroDivisionError as e:
        messagebox.showerror("Помилка", str(e))
        log_action("помилка ділення на нуль")
    except Exception as e:
        messagebox.showerror("Невідома помилка", str(e))


def export_result():
    output = calculate()
    if not output:
        return

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(output + "\n")

    messagebox.showinfo("Експортовано", "Результат записано у файл Output_data.txt.")
    log_action("експортовано результат у файл")


window = tk.Tk()
window.title("Лабораторна 4. Арифметичний калькулятор")
window.geometry("550x500")
window.config(bg="#f4f4f4")

start_session()

tk.Label(window, text="Введіть два числа (через пробіл):", font=("Arial", 12, "bold"), bg="#f4f4f4").pack(pady=5)
input_entry = tk.Entry(window, width=40)
input_entry.pack(pady=5)

tk.Button(window, text="Імпортувати вхідні дані", command=import_data, width=40, bg="#cce5ff").pack(pady=5)

tk.Label(window, text="Оберіть арифметичну операцію:", bg="#f4f4f4", font=("Arial", 11, "bold")).pack(pady=5)

operation_var = tk.StringVar(value="+")
operations = [("+", "Додавання"), ("-", "Віднімання"), ("*", "Множення"), ("/", "Ділення"), ("^", "Степінь")]
for sym, name in operations:
    tk.Radiobutton(window, text=f"{name} ({sym})", variable=operation_var, value=sym, bg="#f4f4f4").pack(anchor="w", padx=120)

tk.Button(window, text="Обчислити вираз", command=calculate, width=40, bg="#d4edda").pack(pady=5)
tk.Button(window, text="Експортувати результат у файл", command=export_result, width=40, bg="#fff3cd").pack(pady=5)

result_label = tk.Label(window, text="Результат: ", bg="#f4f4f4", font=("Arial", 12))
result_label.pack(pady=10)

tk.Label(window, text="Журнал дій (Session log):", bg="#f4f4f4", font=("Arial", 11, "bold")).pack(pady=5)
log_box = scrolledtext.ScrolledText(window, width=65, height=8)
log_box.pack(pady=5)

def refresh_log():
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        log_box.delete(1.0, tk.END)
        log_box.insert(tk.END, f.read())
    window.after(1500, refresh_log)  # автооновлення кожні 1.5 с

refresh_log()
window.protocol("WM_DELETE_WINDOW", lambda: (close_session(), window.destroy()))
window.mainloop()

import tkinter as tk
from tkinter import messagebox, scrolledtext
import string

def create_input_file():
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Помилка", "Введіть текст перед створенням файлу!")
        return

    with open("TF_1.txt", "w", encoding="utf-8") as f:
        f.write(text)
    messagebox.showinfo("Файл створено", "Файл TF_1.txt успішно створено!")

def process_file():
    vowels = ('a', 'e', 'i', 'o', 'u', 'а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я')
    try:
        with open("TF_1.txt", "r", encoding="utf-8") as f:
            text = f.read()

        for ch in string.punctuation:
            text = text.replace(ch, " ")
        words = text.split()

        vowel_words = [w for w in words if w and w[0].lower() in vowels]

        with open("TF_2.txt", "w", encoding="utf-8") as f2:
            for w in vowel_words:
                f2.write(w + "\n")

        messagebox.showinfo("Готово", f"Знайдено {len(vowel_words)} слів, записано у TF_2.txt.")
    except FileNotFoundError:
        messagebox.showerror("Помилка", "Файл TF_1.txt не знайдено!")

def show_output_file():
    try:
        with open("TF_2.txt", "r", encoding="utf-8") as f:
            content = f.read()
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showerror("Помилка", "Файл TF_2.txt не знайдено")

window = tk.Tk()
window.title("Лабораторна №4")
window.geometry("550x500")
window.config(bg="#f4f4f4")

tk.Label(window, text="Введіть текст для TF_1.txt:", font=("Arial", 12, "bold"), bg="#f4f4f4").pack(pady=5)
input_box = scrolledtext.ScrolledText(window, width=60, height=6, wrap=tk.WORD)
input_box.pack(pady=5)

tk.Button(window, text="Зберегти введений текст у TF_1.txt", command=create_input_file, bg="#cce5ff", width=40).pack(pady=5)
tk.Button(window, text="Знайти слова з голосної", command=process_file, bg="#d4edda", width=40).pack(pady=5)
tk.Button(window, text="Показати TF_2.txt", command=show_output_file, bg="#fff3cd", width=40).pack(pady=5)

tk.Label(window, text="Вміст TF_2.txt:", bg="#f4f4f4", font=("Arial", 12)).pack(pady=5)
output_box = scrolledtext.ScrolledText(window, width=60, height=10, wrap=tk.WORD)
output_box.pack(pady=5)

window.mainloop()

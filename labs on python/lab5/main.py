# main.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from classes.test import Exam, FinalExam, Trial

def show_result():
    try:
        name = entry_name.get().strip() or "Без назви"
        subject = entry_subject.get().strip() or "Невідомо"
        score = int(entry_score.get())
        mark = int(entry_mark.get())
        date = entry_date.get().strip() or "Невідомо"
        exam_type = entry_type.get().strip() or "Державна атестація"
        organizer = entry_organizer.get().strip() or "Невідомо"
        duration = entry_duration.get().strip() or "Невідомо"

        trial = Trial(name, subject, score, organizer, duration)

        exam = Exam(name, subject, score, mark, date)
        final_exam = FinalExam(name, subject, score, mark, date, exam_type)

        info_exam = exam.get_info()
        info_final = final_exam.get_info()

        result_text = (
                "=== Іспит ===\n" + exam.Show() +
                "\n\n=== Випускний іспит ===\n" + final_exam.Show() +
                "\n\n=== Випробування ===\n" + trial.Show() +
                "\n\n--- Коротка інформація (метод get_info) ---\n" +
                exam.get_info() + "\n" +
                final_exam.get_info() + "\n" +
                trial.get_info()
        )

        txt_result.delete(1.0, tk.END)
        txt_result.insert(tk.END, result_text)

        # збереження у файл
        with open("results/output.txt", "w", encoding="utf-8") as f:
            f.write(result_text)

        messagebox.showinfo("Збережено", "Результати записані у файл results/output.txt")
    except ValueError:
        messagebox.showerror("Помилка", "Переконайся, що 'Макс. бал' і 'Оцінка' — це числа.")



root = tk.Tk()
root.title("Ієрархія: Тест • Іспит • Випускний іспит (варіант 6)")
root.geometry("640x720")
root.configure(bg="#1F3327")  # темно-зелений

labels = ["Назва:", "Предмет:", "Макс. бал:", "Оцінка:", "Дата:", "Тип атестації:", "Організатор:", "Тривалість (хв):"]
entries = []
for i, text in enumerate(labels):
    tk.Label(root, text=text, bg="#1F3327", fg="#F0E1D2", font=("Segoe UI", 11)).place(x=60, y=40 + i*45)
    e = tk.Entry(root, width=32, bg="#EDE3C8", font=("Segoe UI", 10))
    e.place(x=260, y=40 + i*45, height=28)
    entries.append(e)

(entry_name, entry_subject, entry_score, entry_mark, entry_date, entry_type, entry_organizer, entry_duration) = entries

btn = tk.Button(root, text="Показати результат", command=show_result,
                bg="#4A6853", fg="#F0E1D2", activebackground="#608A6B",
                font=("Segoe UI Semibold", 11), relief=tk.FLAT, padx=12, pady=6)
btn.place(x=230, y=400)

tk.Label(root, text="Результат:", bg="#1F3327", fg="#E6D9C6", font=("Segoe UI", 10, "italic")).place(x=60, y=440)
txt_result = scrolledtext.ScrolledText(root, width=70, height=12, bg="#F6EFE0", font=("Consolas", 10))
txt_result.place(x=60, y=460)


root.mainloop()

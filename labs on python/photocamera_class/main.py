import tkinter as tk
from tkinter import messagebox, scrolledtext
from classes.camera_classes import PhotoCamera, DigitalCamera, Camera
import atexit

@atexit.register

def show_result():
    try:
        model = entry_model.get().strip() or "Без моделі"
        zoom = float(entry_zoom.get())
        material = entry_material.get().strip() or "пластик"
        megapixels = int(entry_mp.get())
        cam_type = entry_type.get().strip() or "відеокамера"

        photo = PhotoCamera(model, zoom, material)
        digital = DigitalCamera(model, zoom, material, megapixels)
        camera = Camera(model, zoom, material, megapixels, cam_type)


        before = ("=== Початкові дані ===\n\n" +
                  "ФОТОАПАРАТ:\n" + photo.info() + "\n\n" +
                  "ЦИФРОВИЙ:\n" + digital.info() + "\n\n" +
                  "КАМЕРА:\n" + camera.info() + "\n")

        digital.update_model()
        camera.update_model()

        after = ("\n=== Після оновлення ===\n\n" +
                 "ЦИФРОВИЙ:\n" + digital.info() + "\n\n" +
                 "КАМЕРА:\n" + camera.info())

        result_text = before + after

        txt_result.delete(1.0, tk.END)
        txt_result.insert(tk.END, result_text)

        with open("results/output.txt", "w", encoding="utf-8") as f:
            f.write(result_text)

        messagebox.showinfo("Збережено", "Результати записані у файл results/output.txt")
    except ValueError:
        messagebox.showerror("Помилка", "Поле Zoom або Мегапікселі повинні бути числами!")

root = tk.Tk()
root.title("Фотоапарат • Цифровий • Камера (варіант 6)")
root.geometry("650x750")
root.configure(bg="#1F3327")

labels = [
    "Модель:", "Zoom (1-35):", "Матеріал (метал/пластик):",
    "Мегапікселі:", "Тип камери:"
]
entries = []

for i, text in enumerate(labels):
    tk.Label(root, text=text, bg="#1F3327", fg="#F0E1D2", font=("Segoe UI", 11)).place(x=60, y=40 + i*50)
    e = tk.Entry(root, width=30, bg="#EDE3C8", font=("Segoe UI", 10))
    e.place(x=300, y=40 + i*50, height=28)
    entries.append(e)

entry_model, entry_zoom, entry_material, entry_mp, entry_type = entries

btn = tk.Button(root, text="Показати результат", command=show_result,
                bg="#4A6853", fg="#F0E1D2", activebackground="#608A6B",
                font=("Segoe UI Semibold", 11), relief=tk.FLAT, padx=12, pady=6)
btn.place(x=230, y=320)

tk.Label(root, text="Результат:", bg="#1F3327", fg="#E6D9C6", font=("Segoe UI", 10, "italic")).place(x=60, y=370)
txt_result = scrolledtext.ScrolledText(root, width=70, height=15, bg="#F6EFE0", font=("Consolas", 10))
txt_result.place(x=60, y=395)

root.mainloop()

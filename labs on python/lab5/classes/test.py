class Test:
    def __init__(self, name="Невідомий тест", subject="Невідомо", max_score=100):
        self.name = name
        self.subject = subject
        self.max_score = max_score

    def __del__(self):
        print("Лабораторна робота виконана студенткою 2 курсу групи 243Б — Дорофтей Катериною.")

    def get_info(self):
        return f"Тест '{self.name}' з предмету '{self.subject}' (макс. бал: {self.max_score})"

    def Show(self):
        return f"Назва тесту: {self.name}\nПредмет: {self.subject}\nМаксимальний бал: {self.max_score}"


class Exam(Test):
    def __init__(self, name="Іспит", subject="Невідомо", max_score=100, mark=0, date="Невідомо"):
        super().__init__(name, subject, max_score)
        self.mark = mark
        self.date = date

    def get_info(self):
        return f"Іспит '{self.name}' ({self.subject}), оцінка: {self.mark}, дата: {self.date}"

    def Show(self):
        base = super().Show()
        return f"{base}\nОтриманий бал: {self.mark}\nДата проведення: {self.date}"


class FinalExam(Exam):
    def __init__(self, name="Випускний іспит", subject="Невідомо", max_score=100,
                 mark=0, date="Невідомо", exam_type="Державна атестація"):
        super().__init__(name, subject, max_score, mark, date)
        self.exam_type = exam_type

    def get_info(self):
        return f"Випускний іспит з {self.subject} ({self.exam_type}), оцінка: {self.mark}"

    def Show(self):
        base = super().Show()
        return f"{base}\nТип атестації: {self.exam_type}"


class Trial(Test):
    def __init__(self, name="Випробування", subject="Невідомо", max_score=100,
                 organizer="Невідомо", duration="Невідомо"):
        super().__init__(name, subject, max_score)
        self.organizer = organizer
        self.duration = duration

    def get_info(self):
        return f"Випробування '{self.name}' з {self.subject}, організатор: {self.organizer}, тривалість: {self.duration}"

    def Show(self):
        base = super().Show()
        return f"{base}\nОрганізатор: {self.organizer}\nТривалість: {self.duration}"

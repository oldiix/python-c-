class PhotoCamera:
    def __init__(self, model="Невідомо", zoom=1, material="пластик"):
        self.model = model
        self.zoom = zoom
        self.material = material

    def cost(self):
        if self.material.lower() == "метал":
            return (self.zoom + 2) * 15
        else:
            return (self.zoom + 2) * 10

    def expensive(self):
        return self.cost() > 200

    def info(self):
        return (f"Модель: {self.model}\n"
                f"Збільшення: {self.zoom}\n"
                f"Матеріал: {self.material}\n"
                f"Вартість: {self.cost()} $\n"
                f"Дорогий: {'Так' if self.expensive() else 'Ні'}")

class DigitalCamera(PhotoCamera):
    def __init__(self, model="Невідомо", zoom=1, material="пластик", megapixels=10):
        super().__init__(model, zoom, material)
        self.megapixels = megapixels

    def cost(self):
        return super().cost() * self.megapixels

    def update_model(self):
        self.megapixels += 2

    def info(self):
        return (super().info() +
                f"\nМегапікслеів: {self.megapixels}\n"
                f"(Цифровий фотоапарат)")

class Camera(DigitalCamera):
    def __init__(self, model="Невідомо", zoom=1, material="пластик",
                 megapixels=10, cam_type="відеокамера"):
        super().__init__(model, zoom, material, megapixels)
        self.cam_type = cam_type

    def cost(self):
        return super().cost() * 10

    def update_model(self):
        self.megapixels += 20

    def info(self):
        return (super().info() +
                f"\nТип камери: {self.cam_type}\n"
                f"(Камера)")

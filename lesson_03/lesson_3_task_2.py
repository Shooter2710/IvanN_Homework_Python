from smartphone import Smartphone

catalog = [
    Smartphone("Xiaomi", "Mi15TPro", "+79999999999"),
    Smartphone("Samsung", "S25Edge", "+79888888888"),
    Smartphone("Iphone", "16Pro", "+79777777777"),
    Smartphone("Huawei", "Pura70", "+79666666666"),
    Smartphone("Honor", "MagicV2", "+79555555555")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")

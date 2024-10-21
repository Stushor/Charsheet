from Charsheet import file_operations
from faker import Faker
import random
import os


FAKE = Faker('ru_RU')

SKILLS = ["Стремительный прыжок",
          "Электрический выстрел",
          "Ледяной удар",
          "Стремительный удар",
          "Кислотный взгляд",
          "Тайный побег",
          "Ледяной выстрел",
          "Огненный заряд"]

LETTERS = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}


def create_people():
    for i in range(1, 11):
        random_skills = random.sample(SKILLS, 3)
        runic_skills = []

        for skill in random_skills:
            runic_skill = skill
            for key_letter, value_letter in LETTERS.items():
                runic_skill = runic_skill.replace(key_letter, value_letter)
            runic_skills.append(runic_skill)

        context = {
            "first_name": f"{FAKE.first_name()}",
            "last_name": f"{FAKE.last_name()}",
            "job": f"{FAKE.job()}",
            "town": f"{FAKE.city()}",
            "strength": f"{random.randint(3, 18)}",
            "agility": f"{random.randint(3, 18)}",
            "endurance": f"{random.randint(3, 18)}",
            "intelligence": f"{random.randint(3, 18)}",
            "luck": f"{random.randint(3, 18)}",
            "skill_1": f"{runic_skills[0]}",
            "skill_2": f"{runic_skills[1]}",
            "skill_3": f"{runic_skills[2]}"
        }

        os.makedirs('Charsheet/output', mode=0o777, exist_ok=True)
        file_operations.render_template("Charsheet/template/charsheet.svg", f"Charsheet/output/charsheet-{i}.svg", context)


def main():
    create_people()


if __name__ == '__main__':
    main()

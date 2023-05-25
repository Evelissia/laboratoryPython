# файл grades.py для кода, связанного с получением информации об успеваемости
def get_grades(username):
    grades = {
        'Vika Vika': "Успеваемость вашего ребенка:\n\nМатематика: Отлично\nИстория: Хорошо\nАнглийский: Удовлетворительно",
        'John Doe': "Успеваемость вашего ребенка:\n\nМатематика: Хорошо\nИстория: Удовлетворительно\nАнглийский: Отлично",
        'Jane Smith': "Успеваемость вашего ребенка:\n\nМатематика: Удовлетворительно\nИстория: Отлично\nАнглийский: Хорошо"
    }

    if username in grades:
        return grades[username]
    else:
        return "Информация об успеваемости для указанного ученика не найдена."
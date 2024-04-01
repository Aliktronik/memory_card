import typing
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QRadioButton,
    QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup,
    QMessageBox
)
import random


class Question:
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions = list()
questions.append(Question('Какая планета является самой большой в Солнечной системе?', 'Меркурий', 'Венера', 'Земля', 'Юпитер'))
questions.append(Question('Что означает слово “самурай”?', 'Ловкость', 'Верность', 'Честь', 'Слава'))
questions.append(Question('Как называется столица Италии?', 'Рим', 'Милан', 'Турин', 'Флоренция'))
questions.append(Question('Какова формула воды?', 'H2O', 'O2H', 'H2OH', 'HHO'))
questions.append(Question('Какие горы являются самыми высокими в мире?', 'Альпы', 'Анды', 'Гималаи', 'Кордильеры'))


def next_question():
    if win.q_index == len(questions):
        win.q_index = 0
        show_score()
        win.score = 0
    
    if win.q_index == 0:
        random.shuffle(questions)

    ask(questions[win.q_index])
    win.q_index += 1


def show_score():
    percent = win.score / win.total * 100
    percent = round(percent, 1)

    text = 'Уважаемый пользователь!\n'
    text += 'Ваш результат составил ' + str(percent) + '%\n'
    text += 'Вы ответили правильно на ' + str(win.score) + ' из ' + str(win.total) + ' вопросов\n'
    text += 'После закрытия данного окна - тест начнется заново. Удачи!'

    msg_box = QMessageBox()
    msg_box.setWindowTitle('Результат тестирования')
    msg_box.setText(text)
    msg_box.exec()


def ask(q):  # функция для установки вопроса
    question_text.setText(q.question)  # установка на виджет QLabel формулировки вопроса
    random.shuffle(answers)  # перемешали кнопки
    answers[0].setText(q.right_answer)  # установили на "нулевую" кнопку правильный ответ
    answers[1].setText(q.wrong1)  # установили на "первую" кнопку неправильный ответ №1
    answers[2].setText(q.wrong2)  # установили на "вторую" кнопку неправильный ответ №2
    answers[3].setText(q.wrong3)  # установили на "третью" кнопку неправильный ответ №3

def check_answer():  # функция для проверки правильного ответа
    for rbtn in answers:  # цикл для перебора всех кнопок с ответами
        if rbtn.isChecked():  # если кнопка была выбрана
            if rbtn.text() == answers[0].text():  # если это был правильный ответ
                right_text.setText('Правильно')  # меняем текст на "Правильно"
                right_answer.setText('Поздравляем!')  # и поздравляем пользователя
                win.score += 1
            else:  # иначе
                right_text.setText('Неправильно')  # меняем текст на "Неправильно"
                right_answer.setText('Правильный ответ: ' + answers[0].text())  # и показываем правильный ответ


def show_result():  # функция для показа результатов ответа на вопрос
    grp_box.hide()  # спрятать группу с вариантами ответов
    grp_box_result.show()  # показать группу с результатом
    btn.setText('Следующий вопрос')  # меняем текст на кнопке
    check_answer()  # вызов функции для проверки ответа

def show_question():  # функция для показа вопроса и вариантов ответа
    next_question()  # вызов функции для отображения следующего вопроса
    grp_box.show()  # показать группу с вариантами ответов
    grp_box_result.hide()  # спрятать группу с результатом
    btn.setText('Ответить')  # меняем текст на кнопке
    radio_group.setExclusive(False)  # снимаем ограничение на выбор вариантов
    radio1.setChecked(False)  # делаем кнопку №1 не нажатой
    radio2.setChecked(False)  # делаем кнопку №2 не нажатой
    radio3.setChecked(False)  # делаем кнопку №3 не нажатой
    radio4.setChecked(False)  # делаем кнопку №4 не нажатой
    radio_group.setExclusive(True)  # возвращаем ограничение на выбор вариантов

def start_test():  # функция для выбора реакции на нажатие на кнопку
    if btn.text() == 'Ответить':  # если на кнопке текст "Ответить"
        show_result()  # то запускаем функцию show_result
    else:  # иначе
        show_question()  # запускаем функцию show_question

app = QApplication([])  # создание экземпляра приложения
win = QWidget()  # создание главного окна
win.setWindowTitle('MemoryCard')  # установка заголовка для окна
win.resize(400, 300)  # изменение размера окна
win.q_index = 0  # создали индекс вопроса
win.score = 0
win.total = len(questions)

question_text = QLabel('Тут будет вопрос')  # создание виджета текста для вопроса
grp_box = QGroupBox('Варианты ответа')  # создание виджета группы
radio1 = QRadioButton('1 вариант')  # создание виджета кнопки варианта ответа
radio2 = QRadioButton('2 вариант')  # создание виджета кнопки варианта ответа
radio3 = QRadioButton('3 вариант')  # создание виджета кнопки варианта ответа
radio4 = QRadioButton('4 вариант')  # создание виджета кнопки варианта ответа
btn = QPushButton('Ответить')  # создание виджета кнопки для ответа
grp_box_result = QGroupBox('Результат')  # создание виджета группы для результата
right_text = QLabel('Правильно/Неправильно')  # создание виджета текста
right_answer = QLabel('Правильный ответ')  # создание виджета текста

radio_group = QButtonGroup()  # экземпляр класса для группы кнопок
radio_group.addButton(radio1)  # добавление кнопки №1 в группу кнопок
radio_group.addButton(radio2)  # добавление кнопки №2 в группу кнопок
radio_group.addButton(radio3)  # добавление кнопки №3 в группу кнопок
radio_group.addButton(radio4)  # добавление кнопки №4 в группу кнопок
answers = [radio1, radio2, radio3, radio4]  # список с кнопками "ответов"

main_layout = QVBoxLayout()  # создание главной направляющей
h_main1 = QHBoxLayout()  # вспомогательная горизонтальный направляющая №1
h_main2 = QHBoxLayout()  # вспомогательная горизонтальный направляющая №2
h_main3 = QHBoxLayout()  # вспомогательная горизонтальный направляющая №3
grp_box_layout = QHBoxLayout()  # главная направляющая для виджета группы
grp_box_v1 = QVBoxLayout()  # вспомогательная вертикальная направляющая №1
grp_box_v2 = QVBoxLayout()  # вспомогательная вертикальная направляющая №2
grp_box_result_layout = QVBoxLayout()  # главная направляющая для виджета группы "результат"

grp_box_result_layout.addWidget(right_text)  # добавление виджета текста
grp_box_result_layout.addWidget(right_answer, alignment=Qt.AlignCenter)  # добавление виджета текста по центру
grp_box_result.setLayout(grp_box_result_layout)  # добавление направляющей на виджет группы "результат"

grp_box_v1.addWidget(radio1)  # добавление на вспомогательную вертикальную направляющую №1 кнопки ответа №1
grp_box_v1.addWidget(radio2)  # добавление на вспомогательную вертикальную направляющую №1 кнопки ответа №2
grp_box_v2.addWidget(radio3)  # добавление на вспомогательную вертикальную направляющую №2 кнопки ответа №3
grp_box_v2.addWidget(radio4)  # добавление на вспомогательную вертикальную направляющую №2 кнопки ответа №4
grp_box_layout.addLayout(grp_box_v1)  # добавление на главную направляющую виджета группы вспом. напр. №1
grp_box_layout.addLayout(grp_box_v2)  # добавление на главную направляющую виджета группы вспом. напр. №1
grp_box.setLayout(grp_box_layout)  # установка направляющей на виджет группы

h_main1.addWidget(question_text, alignment=Qt.AlignCenter)  # добавления на вспом. напр. №1 виджета вопроса
h_main2.addWidget(grp_box)  # добавления на вспом. напр. №2 виджета группы
h_main2.addWidget(grp_box_result)  # добавления на вспом. напр. №2 виджета группы "результат"
h_main3.addStretch(1)  # добавления на вспом. напр. №3 1/4 пустоты
h_main3.addWidget(btn, stretch=2)  # добавления на вспом. напр. №3 виджет кнопки с шириной 2/4
h_main3.addStretch(1)  # добавления на вспом. напр. №3 1/4 пустоты

main_layout.addLayout(h_main1)  # добавление на главную направляющую окна вспом. напр. №1
main_layout.addLayout(h_main2)  # добавление на главную направляющую окна вспом. напр. №2
main_layout.addLayout(h_main3)  # добавление на главную направляющую окна вспом. напр. №3

win.setLayout(main_layout)  # установить главную направ. на главное окно

btn.clicked.connect(start_test)  # привязка функции по событию "нажатие"

next_question()
grp_box_result.hide()  # скрыть группу с результатом

win.show()  # сделать окно видимым
app.exec()  # запуск приложения
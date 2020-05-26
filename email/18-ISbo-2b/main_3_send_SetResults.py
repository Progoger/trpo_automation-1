# coding=utf-8
import inspect
from Loger import Logs 
logs = Logs()
name = None

from time import sleep
from datetime import datetime

# from main_4_moderate_FormAnswers import FormAnswers
import config_Project as cfg
from google_Sheet import Sheet

def SetResults(letterResults):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,letterResults)
    """
    Выставить необходимые оценки в журнал
    """
    # Выставление оценок в журнал (функция пока не реализована)
    SetMarks(letterResults)

    print(letterResults)

    # Вызов следующей функции для формирования ответов
    # FormAnswers(letterResults)
    return letterResults

def SetMarks(letterResults):
    name = inspect.currentframe().f_code.co_name
    logs.Infor(name,letterResults)
    """
     Функционал:
    - Выставить необходимые оценки в журнал
    На входе:
    - letterResults - заполненный и проверенный список писем - экземпляров класса LetterResults
    На выходе:
    - None
    Что предусмотреть:
    - None
    """
    with open(cfg.filename, "a") as file:
        file.write("\nВыставление оценок... ")

    for i in letterResults:
        if i.CodeStatus == "30":
            value = 0
            if i.IsOK:
                value = 1

            group = i.Student.GroupOfStudent
            name = i.Student.NameOfStudent.split(' ')
            first_name = name[0]
            surname = name[1]
            patronymic = name[2]
            lab_id = '{}'.format(i.NumberOfLab)

            result = Sheet.journal(group, first_name, surname, patronymic, lab_id, value)
            if result:
                if result[0] == '1':
                    i.CodeStatus = '10'

    with open(cfg.filename, "a") as file:
        file.write("Оценки выставлены!")
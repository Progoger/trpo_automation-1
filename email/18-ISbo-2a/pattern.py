"""
Шаблоны для заполнения писем
"""


def funcSt(str_of_val_er, str_of_er):  
    """
    Паттерн сообщений для рассылки писем студентам
    :param str_of_val_er: ошибки в валидации письма, где накосячил студент
    :param str_of_er: ошибки в коде студента
    :return: pattern: шаблоны писем, которые мы отправляем студенту после проверок
    """
    pattern = [
        {
             'title': 'ТРПО. Работа успешно принята',
             'our_msg': 'Поздравляю!\nРабота успешно принята!' +
                        '\nОценку можно проверить в журнале:' +
                        '\nhttps://docs.google.com/spreadsheets/d/1gOX8T8ihy3J1khhC16U1qDwaI-K6ndkp9LFWAHncuWA' +
                        '/edit?usp=sharing'
        },
        {
            'title': 'ТРПО. Обнаружены ошибки в работе',
            'our_msg': 'В Вашей работе обнаружены ошибки:\n\n' + str_of_val_er +
                       '\nПросьба исправить их и отправить письмо повторно.'
        },
        {
            'title': 'ТРПО. Обнаружены ошибки в заполнении письма',
            'our_msg': 'В структуре письма обнаружены следующие ошибки:\n\n' +
                       str_of_er + '\nПросьба исправить их в соответствии с ' +
                       'документом\n' + 'https://docs.google.com/document/d/' +
                       '1DRhgepxVwoscylIS2LCW-po5SFBdqOr-oo92bP_XfHE/edit?' +
                       'usp=sharing'
        },
        {
            'title': 'ТРПО. Авторизация пользователя',
            'our_msg': 'Вы не найдены в системе. Пожалуйста, перейдите по' +
                       ' ссылке и зарегистрируйтесь.\n'
                       'https://forms.gle/pNzAtYKWAiDom6MEA'
        },
        {
            'title': 'Ошибка модуля',
            'our_msg': 'В модуле ... обнаружена ошибка. В ближайшее время ' +
                       'проблема будет исправлена. Просим прощения за неудобства.'
        }
    ]
    return pattern


def funcTs(name_of_student, validation_dictionary, str_of_er):
    """
    Паттерн сообщений для рассылки писем преподавателю или команде
    :param name_of_student: имя и фамилия студента.
    :param validation_dictionary: словарь с валидации письма,
    в котором есть ('Numder')номер работы и ('URL')ссылка на работу.
    :param str_of_er: ошибки в коде студента
    :return: pattern: шаблоны писем, которые мы отправляем студенту после проверок
    """
    pattern = [
        {
            'hello': 'Здравствуйте, Юрий Викторович!\n\n',
            'title': 'ТРПО. Ошибка в работе студента',
            'our_msg': 'Студент ' + name_of_student +
                       ' не справился с задачей №' +
                       validation_dictionary['Numder'] +
                       ' (' + validation_dictionary['URL'] + ')' +
                       '\nБыли допущены ошибки в работе:\n\n' +
                       str_of_er
        },
        {
            'hello': 'Здравствуйте!',
            'title': 'ТРПО. Служба дала сбой',
            'our_msg': 'В модуле ... возникла ошибка ...'
        }
    ]
    return pattern


SIGNATURE = "\n\nС уважением,\nБот"

def funcReturnMsg(hello_student, our_msg, SIGNATURE, 
                   date_of_msg, return_body, return_head):
    """
    Паттерн сообщений для рассылки писем преподавателю или команде
    :param hello_student: приветсвие студента, полученное из метода funcHello.
    :param our_msg: тело нашего ответного письма, полученного из паттерна писем из функции funcSt
    :param SIGNATURE: подпись в нашем ответном письме(С уважением,Бот)
    :param date_of_msg: время письма
    :param return_body: тело письма
    :param return_head: заголовок письма
    :return: pattern: шаблоны писем, которые мы отправляем студенту после проверок
    """
    date_part = f'\n\n-----\nRe: <{date_of_msg}>\n'
    return_part = date_part + f'Тема: {return_head}\n{return_body}\n-----'
    text_of_msg = hello_student + our_msg + return_part + SIGNATURE
    return text_of_msg

def funcHello(name_of_student):
    return 'Здравствуйте, '+ f'{name_of_student}' + '!\n\n'


GMAIL_OF_TRPO = "trpo.automation@gmail.com"


EMAIL_OF_TEACHER = 'yuri.silenok@gmail.com'


MAS_OF_TO = ['yuri.silenok@gmail.com', '0sashasmirnov0@gmail.com',
             'k.svyat395@gmail.com', 'MaXLyuT2000@gmail.com',
             'majishpro@gmail.com', 'Sirokko77@gmail.com',
             'nikita.lukyanow@gmail.com', 'generalgrigorevous@gmail.com', 
             'molchok.yurij@gmail.com', 'amr15319@gmail.com']


"""
Валидация
"""


SUBJECT_LIST = ['трпо'] # Список предметов
SUBJECTNUMBER_LIST = ['лр№1', 'лабораторная работа №1', 
                      'лр№2', 'лабораторная работа №2',
                      'лр№3', 'лабораторная работа №3',
                      'лр№4', 'лабораторная работа №4',
                      'лр№5', 'лабораторная работа №5',
                      'лр№6', 'лабораторная работа №6',
                      'лр№7', 'лабораторная работа №7',
                      'лр№8', 'лабораторная работа №8',
                      'лр№9', 'лабораторная работа №9',
                      'лаба №1','лабораторная №1',
                      'лаба №2','лабораторная №2',
                      'лаба №3','лабораторная №3',
                      'лаба №4','лабораторная №4',
                      'лаба №5','лабораторная №5',
                      'лаба №6','лабораторная №6',
                      'лаба №7','лабораторная №7',
                      'лаба №8','лабораторная №8',
                      'лаба №9','лабораторная №9',]
GREATING_LIST =  ['добрый день','добрый вечер',# Список приветствий
                  'добрейший вечерочек','доброй ночи','здравствуйте','привет',
                  'здравия желаю','хаю хай','доброго времени суток'] 
SUBJECTNUMBERURL_LIST = ['7', '8', '9'] # Список ЛР c URL


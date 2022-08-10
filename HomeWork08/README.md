## Домашнее задание 8
Доделать решение задачи: Задача: Создать информационную систему позволяющую работать 
с сотрудниками некой компании \ студентами вуза \ учениками школы
https://github.com/denis01111/Python_live
Доделать нашу мини-систему

### Описание
Есть два файла -- школьники и родители, оба файла считываются в словари по которым можно произвести
поиск: по ФИО школьника сопоставляются родители. В случае, если задана только фамилия и есть несколько 
однофамильцев, программа попросит уточнить имя и отчество. Ключи словарей: кортежи вида
(фамилия, id-отца). 

### Содержимое:
* main.py -- Основной файл
* data_part.py -- Логика работы с данными (считывание файлов в словари, поиск по словарям)
* view.py -- интерфейс
* children.csv -- детский список
* parents.csv -- взрослый список.
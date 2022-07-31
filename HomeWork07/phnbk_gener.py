import csv
import faker
import json
import os
from random import randint as rint
import time
from data_manager import saver, adder, storage

fio = faker.Faker('ru_RU')  # Fake full name trio generator

# storage = []  # old variant
# storage = {}
# storage = {}


def generate(amt: int = 500) -> None:
    """
    Takes a fake full name string generated by Faker.
    Calls phone generator and compiles a phonebook entry.
    :param amt:
    :return:
    """
    global storage
    extra = ('тов.', 'г-н', 'г-жа')
    print('GENERATING')
    for _ in range(amt):
        unit = {}
        line: str = fio.name()
        if line.startswith(extra):
            line = ' '.join(line.split()[1:])
        else:
            line = ' '.join(line.split())
        tmp = arrange(line)

        unit['id'] = time.time_ns()
        # unit['id'] = hash(tmp[0])
        unit['Name'] = tmp
        unit['Phone'] = [phone for phone in phone_generator(rint(1, 3))]
        unit['Dsc'] = 'No Description'
        saver(unit)
        # storage.append(unit)
        # if unit['Name'][0][0] not in storage.keys():
        #     storage[unit['Name'][0][0]] = [unit]
        # else:
        #     (storage[unit['Name'][0][0]]).append(unit)
        del tmp, unit


def arrange(line_in: str) -> list:
    """
    Gets a line of Surname Name Father-name and arranges it in common way.
    :param line_in: str
    :return: line_in: list
    """
    suffixes = ('ов', 'ова', 'ев', 'ева', 'ив', 'ива', 'ин', 'ина')
    line_in = line_in.split()
    if line_in[-1].endswith(suffixes):
        line_in = [line_in[-1]] + line_in[:-1]
    return line_in


def phone_generator(amt: int) -> str:
    """
    Fake-phone number generator-function.
    :param amt:
    :return: str
    """
    for _ in range(amt):
        phn = '+7(' + str(rint(900, 999)) + ')' +str(rint(100_00_00, 999_99_99))
        yield phn

#
# # Command Add section
# def saver(unit_in: dict) -> None:
#     global storage
#     if unit_in['Name'][0][0] not in storage.keys():
#         storage[unit_in['Name'][0][0]] = [unit_in]
#     else:
#         (storage[unit_in['Name'][0][0]]).append(unit_in)
#
#
# def adder() -> [str, dict]:
#     response = '0'
#     phone = []
#
#     surname = input('Input surname (Enter to skip): ')
#     name = input('Input name (Enter to skip): ')
#     f_name = input('Input father\'s_name (Enter to skip): ')
#     if surname or name or f_name:
#         response = {'id': time.time_ns(), 'Name': [item for item in (surname, name, f_name) if item]}
#         while True:
#             phone_num = input('Input phone number(s) or "end" to finish: ').lower()
#             if phone_num == 'end':
#                 break
#             elif phone_num.replace('+', '').replace('(', '').replace('+', ')').isdigit():
#                 phone.append(phone_num)
#             else:
#                 print('Wrong input')
#         response['Phone'] = phone   # [phone for phone in phone_generator(rint(1, 3))]
#         response['Dsc'] = input('Input description: ') or 'No Description'
#
#     return response


def dump_json(file_name: str) -> None:
    global storage
    # file_name += '.json'
    generate()
    print(storage)
    storage = json.dumps(storage, indent=4, ensure_ascii=False, sort_keys=True)  # ensure_ascii=False for cyrillic
    with open(file_name, 'w', encoding='utf-8', newline='') as out_fl:
        out_fl.write(str(storage))
        # out_fl.write(str(storage))


def dump_csv(file_name: str) -> None:
    global storage
    file_name += '.csv'
    generate()
    print(storage)
    storage = json.dumps(storage, indent=4, ensure_ascii=False, sort_keys=True)  # ensure_ascii=False for cyrillic
    with open(file_name, 'w', encoding='utf-8') as out_fl:
        out_fl.write(str(storage))


# file_nm = os.path.abspath(os.curdir) + '/phn_bk3'
# dump_json(file_nm)
# dump_csv(file_nm)


# while True:
#     choice = input('Make choice: ')
#     if choice == 'exit':
#         raise SystemExit
#     elif choice == 'generate':
#         # file_nm = os.path.abspath(os.curdir) + '/'
#         # file_nm += input('Input filename (extension is not required, .txt is used): ') + '.json'
#         # file_nm = input('Input filename (extension is not required): ')
#         file_nm = 'phn_bk3'
#         file_nm = os.path.join(os.path.abspath(os.curdir), file_nm)
#         dump_json(file_nm)
#     else:
#         print('WRONG INPUT')

# file_nm = 'phn_bk3'
file_nm = 'SWOFF_testing.json'
file_nm = os.path.join(os.path.abspath(os.curdir), file_nm)
dump_json(file_nm)


# print(adder())

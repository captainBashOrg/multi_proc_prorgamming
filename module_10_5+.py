
"""
2 Костюченко Артём
Решение выполнено в принципе верно, но есть несколько недочетов:
1. В функции `read_info` строки добавляются в список `all_data` после считывания следующей строки, в итоге последняя строка добавляется пустой. Чтобы исправить это, добавляйте строку в `all_data` до считывания следующей строки.

Ошибка, исправлено. Спасибо!

2. Импорт модуля `PIL` (from PIL import Image) не нужен в данном контексте и должен быть убран.

Закоментировал.
3. Весь код, связанный с выполнением должен быть внутри блока `if __name__ == '__main__'`, включая объявление списка `filenames`. Следует оставить только один блок `if __name__ == '__main__'` и убрать дублирующий.

Для лучшей читабельности? Закоментировал
4. В списке `filenames` номера файлов начинаются с 1, а не с 0.

Создал свой файл, с нулём. Но в ТЗ с 1, поправлено.
Поправьте эти моменты, чтобы код работал корректно и соответствовал заданию.
"""

def read_info(name):

    all_data = []
    #print(name)
    file = open(name, "r" )
    line = file.readline()

    while  (line != ""):
        #print(line )
        all_data.append(line)
        line = file.readline()

    file.close() # Уходя мы гасим свет

if __name__ == '__main__':
    print("Многопроцессное считывание")
    from datetime import datetime
#    from PIL import Image
    import multiprocessing
# Линейный вызов
    start_line =  datetime.now()

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    for name in filenames:
        read_info(name)

    res_time_line = datetime.now() - start_line
    print(f"Линейный способ требует  {res_time_line} времени")
# Многопроцессный

    for i in range (1, 10):
        start_mult = datetime.now()
        with multiprocessing.Pool(processes=i) as pool:
            pool.map(read_info, filenames)

        res_time_mult = datetime.now() - start_mult
        print(f"Многопроцессорный. {i} процессоров, требует  {res_time_mult} времени")
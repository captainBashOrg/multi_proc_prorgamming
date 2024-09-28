

def read_info(name):

    all_data = []
    #print(name)
    file = open(name, "r" )
    line = file.readline()

    while  (line != ""):
        #print(line )
        line = file.readline()
        all_data.append(line)
    file.close() # Уходя мы гасим свет

if __name__ == '__main__':
    print("Многопроцессное считывание")
    from datetime import datetime
    from PIL import Image
    import multiprocessing
# Линейный вызов
    start_line =  datetime.now()

    filenames = [f'./file {number}.txt' for number in range(0, 5)]

    for name in filenames:
        read_info(name)

    res_time_line = datetime.now() - start_line
    print(f"Линейный способ требует  {res_time_line} времени")
# Многопроцессный

if __name__ == '__main__':

    for i in range (1, 10):
        start_mult = datetime.now()
        with multiprocessing.Pool(processes=i) as pool:
            pool.map(read_info, filenames)

        res_time_mult = datetime.now() - start_mult
        print(f"Многопроцессорный. {i} процессоров, требует  {res_time_mult} времени")

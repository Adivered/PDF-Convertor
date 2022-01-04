import os
import tabula
import time
from multiprocessing import Process

def convert_to_csv(*args):
    for arg in args:
        df = tabula.read_pdf(arg, pages='all', encoding='utf-8')[0]
        tabula.convert_into(f'{arg}', f'{arg[:-4]}.csv', output_format='csv', pages='all', stream=True)
        deletePDF(arg)


def isPDF(file):
    return True if file.endswith('.pdf') else False

def deletePDF(file):
    os.remove(file)

def get_pdf_list(path):
    lst = []
    for file in os.listdir(path):
        filename = os.fsdecode(file)
        if isPDF(filename):
            lst.append(file)
    return lst

def main():
    start = time.time()
    _DIRPATH = ''
    processes = []
    files = get_pdf_list(_DIRPATH)
    for file in files:
        print(file)
        p = Process(target=convert_to_csv, args= [file])
        p.start()
        processes.append(p)
    

    for p in processes:
        p.join()
    finish = time.time()
    print(f"All tasks completed in {round(finish - start, 3)} seconds")

                    


if __name__ == "__main__":
    main()
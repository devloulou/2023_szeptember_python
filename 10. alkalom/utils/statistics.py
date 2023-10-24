'''
if __name__ == '__main__':
    from file_handler import get_data_from_txt
else:
    from utils.file_handler import get_data_from_txt
'''

'''import sys

sys.path.append(r'C:\WORK\2023_szeptember_python\10. alkalom')

from utils.file_handler import get_data_from_txt

'''

def get_page_number(book_data):
    import math
    return math.ceil(len(book_data)/3000)

def get_release_date(book_data: str):

    release_date = book_data.splitlines()

    for item in release_date:

        if 'Release Date:' in item:
            return item.replace('Release Date:', '')

def get_book_title(book_data):
    title = book_data.split('Title: ')
    return title[1].split('\n')[0]

def count_words(book_data:str):
    words = book_data.split()
    return len(words) 

def count_line(book_data: str):
    lines = book_data.splitlines()
    lines = [item for item in book_data.split('\n') if item != '']

    return len(lines)

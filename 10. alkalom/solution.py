# from utils.file_handler import get_data_from_txt
# from utils.statistics import (get_book_title,
#                               get_page_number,
#                               get_release_date,
#                               count_line,
#                               count_words)

from utils import get_data_from_txt, write_json
from utils import (get_book_title,
                    get_page_number,
                    get_release_date,
                    count_line,
                    count_words)


def main():
    file_path = r"C:\WORK\2023_szeptember_python\8. alkalom\data\A Tale of Two Cities.txt"
    data = get_data_from_txt(file_path)

    statistic_dict = {
        'page_num': get_page_number(data),
        'lines': count_line(data),
        'words': count_words(data),
        'release_date': get_release_date(data),
        'title': get_book_title(data) }
    
    write_json('statistics.json', statistic_dict)

if __name__ == '__main__':
    main()
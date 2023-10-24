"""
az __init__.py file feladatai: -> teljesen opcionális -> üresen hagyható

    - csökkenteni az importok mélységét
    - vezérelni tudod a láthatóság -> namespace használatra
    - ki tudjátok ajánlani az azonnal elérhető modulokat, változókat, függvvényeket, osztályokat

"""

from .file_handler import get_data_from_txt, write_json
from .statistics import (get_book_title,
                         get_page_number,
                         get_release_date,
                         count_line,
                         count_words)
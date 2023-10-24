def get_data_from_txt(file_path):
    book = None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            book = f.read()
    except OSError as o_er:
        print(f"OSError: {o_er}")
    except Exception as err:
        # raise Exception(f"{err}")
        print(f'Exception: {err}')
    finally:
        print("Ez mindig lefut")


    return book

def write_json(file_path, data):
    import json
    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

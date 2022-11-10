# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
JSON = { "Users": [
    {
        "id": 1,
        "employee": {
            "department": "tech",
            "name": "Mark",
            "project": [
                {
                    "id": 2,
                    "name": "Test",
                    "status": "ok",
                    "mistakes": []
                }
            ]

        }
    },
    {
        "id": 2,
        "employee": {
            "department": "tech",
            "name": "Alex",
            "project": [
                {
                    "id": 3,
                    "name": "parser",
                    "status": "filed",
                    "mistakes": [
                        404, "IO error"
                    ]
                }
            ]
        }
    }
] }


def transform_to_list(j_dict, lst=None):
    if lst is None:
        lst = []
    if type(j_dict) == dict:
        for item in j_dict:
            if item not in lst:
                lst.append(item)
            if j_dict.get(item, None) is not None:
                transform_to_list(j_dict[item], lst)
    elif type(j_dict) == list:
        for item in j_dict:
            transform_to_list(item, lst)
    else:
        if j_dict not in lst:
            lst.append(j_dict)


    return lst








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(transform_to_list(JSON))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

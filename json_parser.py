from sys import argv
import json


try:
    _, json_path = argv
except ValueError:
    raise(ValueError('Script needs a path of json file'))

if not json_path[-5:].lower() == ".json":
    raise(ValueError("File extension must be '.json'"))

with open(json_path) as f:
    json_data = json.load(f)


def transform_to_list(j_object, lst=None):
    if lst is None:
        lst = []
    if type(j_object) == dict:
        for item in j_object:
            if item not in lst:
                lst.append(item)
            if j_object.get(item, None) is not None:
                transform_to_list(j_object[item], lst)
    elif type(j_object) == list:
        for item in j_object:
            transform_to_list(item, lst)
    else:
        if j_object not in lst:
            lst.append(j_object)

    return lst


print(transform_to_list(json_data))

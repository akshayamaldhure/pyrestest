import json


def transform_json(json_file, replacements_dict=None):
    with json_file as json_data:
        json_dict = json.load(json_data)
    for key, value in replacements_dict.iteritems():
        if key in json_dict:
            json_dict[key] = value
    print("Transformed JSON: {}".format(str(json_dict)))
    return json.dumps(json_dict)


def remove_key_from_json(json_file, key):
    json_dict = json.load(open(json_file), encoding='utf-8')
    new_dict = dict(json_dict)
    print("Removing key {} from dictionary {}".format(key, str(json_dict)))
    del new_dict[key]
    return json.dumps(new_dict)


def write_json_to_file(data, output_file):
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)


def get_value_from_json_file(json_file, key):
    try:
        with open(json_file) as infile:
            data = json.load(infile)
            return data[key]
    except KeyError:
        print("Invalid key {}".format(key))

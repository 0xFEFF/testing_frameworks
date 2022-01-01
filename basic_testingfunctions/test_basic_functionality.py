import re

KEY_PATTERN = "[a-zA-Z0-9]"

def test_dictionary_keys_format(dictionary):
    for key, value in dictionary.items():
        print(re.match(KEY_PATTERN, key))

def test_dictionary_keys_exist(dictionary, key_list):
    dict_keys = dictionary.keys()
    assert key_list[1] in dict_keys


if __name__ == "__main__":
    obj = {" wrong key": "wrong", "right key": "right"}
    key_list = ["right key", "blabla"]

    test_dictionary_keys_format(obj)

    test_dictionary_keys_exist(obj, key_list)
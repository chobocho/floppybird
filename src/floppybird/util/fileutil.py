import json
import os
import random


def save_as_json(data, filename, json_indent=2):
    """

    :param data:
    :param filename:
    :param json_indent:
    """
    print(data['high_score'])
    data['high_score'] = encode_high_score(data['high_score'])
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=json_indent)

    print(decode_high_score(data['high_score']))
    print(f"save high score: {data['high_score']}")

def load_json_file(filename, default_value=0):
    print(f"loadConfig: {filename}")
    if not os.path.exists(filename):
        print(filename, "not exist!")
        return default_value

    config_data = {}
    try:
        with open(filename) as json_file:
            config_data = json.load(json_file)
    except:
        print(f"Error! fail to load {filename}")
        return default_value

    if 'high_score' in config_data:
        print(f"previous high score: {config_data['high_score']}")
        if type(config_data['high_score']) == int:
            return config_data['high_score']
        else:
            return decode_high_score(config_data['high_score'])

    return default_value

def encode_high_score(score):
    alpha = "ABCDEFGHIJK"
    random_str = "ABQWERQWETASVCECADSGASDKJMZXCMVLASDKJFGASPDOGIALJFKELJLASDKFLASD"

    start = random.randint(0, len(random_str)-5)
    end = random.randint(0, len(random_str)-5)
    new_score = ""
    for c in list(str(score)):
        new_score += alpha[ord(c)-ord('0')]
    save_score = random_str[start:start+4] + new_score + random_str[end:end+4]
    print(f'encode_high_score {save_score}')
    return random_str[start:start+4] + new_score + random_str[end:end+4]


def decode_high_score(encoded_score) -> int:
    score = 0
    try:
        for i in list(encoded_score[4:-4]):
            if ord(i) < ord('A') or ord(i) > ord('Z'):
                print("Error! modifed score! score force set to 0")
                return 0
            score = score * 10 + ord(i)-ord('A')
    except:
        score = 0

    print(f'score : {score}')
    return score
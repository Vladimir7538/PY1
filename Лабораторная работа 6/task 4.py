import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",") -> list[dict]:
    json_array = []
    count = 0

    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
            line = line.strip()

            if count == 1:
                keys_list = line.split(delimiter)
                continue

            data_list = line.split(delimiter)
            csv_reader = {keys_list[i]: data_list[i] for i in range(len(keys_list))}

            json_array.append(csv_reader)

    return json_array


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

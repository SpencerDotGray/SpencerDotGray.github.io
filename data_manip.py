
from pprint import pprint
import json

with open('./flower.txt', 'r+') as file_in:
    lines = file_in.readlines()

    output = []
    for line in lines:
        # print(line)

        line = line.strip()

        splits = line.split('@')

        output.append({
            'name': splits[0].split('(')[0].strip(),
            'scientific_name': splits[0].split('(')[1].replace(')', '').strip(),
            'description': splits[1].strip()
        })

    dumps = json.dumps(output)
    with open('./flowers.json', 'w+') as file_out:
        file_out.write(dumps)
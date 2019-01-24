import json
import os

file =os.path.join(os.path.dirname(__file__),'emoji_ios6.json')

def load_emoji_map(file):
	json_data = json.load(open(file, encoding='utf-8'))
	sb_dict = {}
	for m in json_data:
		sb_dict[m['sb'].lower()]=m['utf8']
	return sb_dict


def softband_to_utf8(emoji):
    hex_emoji = sb_dict.get(emoji.lower(), '')
    if hex_emoji:
        return bytes.fromhex(hex_emoji).decode('utf-8')
    else:
        return '' 

sb_dict = load_emoji_map(file)

# a=os.path.join(os.path.dirname(__file__),'emoji_ios6.json')
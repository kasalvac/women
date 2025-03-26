import re
import json
from functools import partial

# function to fix the mojibake from double encoding
fix_mojibake_escapes = partial(
    re.compile(rb'\\u00([\da-f]{2})').sub, #replace all \u00hh JSON sequences with the byte the last two hex digits represent,
    lambda m: bytes.fromhex(m[1].decode()),
)



output_text = ''

for i in range(1,22):
    print(i)

    dir_name = ('data/message_' + str(i) + '.json')

    with open(dir_name, 'rb') as binary_data:
        repaired = fix_mojibake_escapes(binary_data.read())
    data = json.loads(repaired)

    for message in data['messages']:
        try:
            sender = message['sender_name']
            content = message['content']
            output_text += f"{sender}:\n{content}\n\n"

        except KeyError:
            continue

# Save to a text file
output_filename = "chat_conversation.txt"
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(output_text)

print(f"Text file has been saved as {output_filename}")

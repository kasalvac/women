import json

output_text = ''

for i in range(1,21):

    dir_name = ('data/message_' + str(i) + '.json')
    with open(dir_name, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for message in data['messages']:
        sender = message['sender_name']
        content = message['content']
        output_text += f"{sender}:\n{content}\n\n"

# Save to a text file
output_filename = "chat_conversation.txt"
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(output_text)

print(f"Text file has been saved as {output_filename}")

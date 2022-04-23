import os 
import openai

openai.api_key = "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"

prompt = "collect all the information you can find on William Skaugvolldal Strzelecki from Oslo, Norway and write it"

response = openai.Completion.create(
    engine = 'text-davinci-002',
    prompt = prompt,
    temperature = 0,
    max_tokens = 2048,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
)

print(response['choices'][0]['text'])

with open('C:\\Users\\Gaming_Dator_VII\\Desktop\\Mitt-repo\\python-development\\prj-ai\\essay.txt', 'w+') as f:
    f.write(prompt + '\n\n')
    f.write(response['choices'][0]['text'])
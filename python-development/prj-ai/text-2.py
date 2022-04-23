import os 
import openai

openai.api_key = "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"

prompt = "As the A+ student you are,`\
    write an essay about the following topic:\
    what use cases are there for artificial intelligence"

response = openai.Completion.create(
    engine = 'text-davinci-002',
    prompt = prompt,
    temperature = 1,
    max_tokens = 2048,
    top_p = 1,
    frequency_penalty = 0,
    presence_penalty = 0
)

print(response['choices'][0]['text'])
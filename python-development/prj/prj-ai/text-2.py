import os 
import openai

openai.api_key = "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"

prompt = "create an outline for a research paper on the threats of artificial intelligence"

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
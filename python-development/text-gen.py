import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  engine="text-davinci-002",
  prompt="answer this question in spanish: ¿Que recuerdas de la pelicula 'birdwatchers'?",

  #Fui a nuestra cabina con mi familia
  
  temperature=0,
  max_tokens=2048,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response['choices'][0]['text'])
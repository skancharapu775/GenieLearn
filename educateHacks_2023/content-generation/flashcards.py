import openai
import os
import keys

# Starting Steps
'''
Important Notes:
    pip install openai
    Set Max Tokens
    Flashcard APIs

pricing: https://openai.com/pricing#language-models
models: https://platform.openai.com/docs/models/gpt-3-5
'''

'''
Flashcard format:

'''

openai.api_key = keys.API_KEY
chat_models = ["gpt-3.5-turbo"]
completion_models = ["davinci", "curie", "babbage", "ada"]


def generate_response(topic, num):
    beg = "Create" + str(num) + " flash cards about "
    end = ",format of Concept : Definiton"
    prompt = beg + topic + end
    model = completion_models[2]

    '''
    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.6,
        max_tokens=200,
        messages = [{"role":"user", "content": prompt}]
    )
    '''
    
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.6,
        max_tokens=50,
    )
    
    return response

def parse(text):
    text = text.lstrip(" ")
    #for i in range(3):
        #p = "\n" + str(i + 1)
        #text.strip()

    final_text = text.strip()

    flashcards = {}

    return text

response = generate_response("Spanish Vocab", 3)
print(response)
# raw_text = response["choices"][0]["content"] 
# text instead of content for gpt-3.0 models
# raw_text = "1. Concept: Hola\nDefinition: Hello\n\n2. Concept: Adi\u00f3s\nDefinition: Goodbye\n\n3. Concept: Gracias\nDefinition: Thank you"
# print(parse(raw_text))
#print(parse(raw_text))




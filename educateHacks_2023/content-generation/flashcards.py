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
completion_models = ["davinci", "curie", "babbage", "ada", "babbage:ft-personal:babbage-4-2023-04-08-13-57-22"]


def generate_response(topic, num, max_tokens):
    beg = "Create" + str(num) + " flash cards about "
    end = "in the format of Vocab word -> Answer"
    prompt = beg + topic + end
    model = chat_models[0]

    
    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.6,
        max_tokens=max_tokens,
        messages = [{"role":"user", "content": prompt}]
    )
    
    '''
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0.6,
        max_tokens=300,
    )
    '''

    return response

def parse(text, num):
    text = text.replace('\n','')
    text = text.lstrip("1. ")
    
    flashcards = []
    for i in range(2, num + 1):
        seperator = str(i) + ". "
        if (i != num + 1):
            texts = text.split(seperator)
            text = texts[1]
            phrase = texts[0]
        else:
            phrase = texts[1]

        card = phrase.split(" -> ")
        if len(card) != 0:
            flashcards.append(card)
        
    return flashcards

response = generate_response("Spanish School Vocab", 6, 200)
raw_text = response["choices"][0]["message"]["content"] 
# text instead of content for gpt-3.0 models
# raw_text = "1. Profesor -> Teacher\n2. Estudiante -> Student\n3. Clase -> Class\n4. Tarea -> Homework\n5. Examen -> Exam\n6. Escuela -> School"
print(parse(raw_text, 6))
#print(parse(raw_text))




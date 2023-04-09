import openai
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


openai.api_key = keys.API_KEY
chat_models = ["gpt-3.5-turbo"]
completion_models = ["davinci", "curie", "babbage", "ada", "babbage:ft-personal:babbage-4-2023-04-08-13-57-22"]


def generate_card_response(topic, num, max_tokens):
    beg = "Create" + str(num) + " flash cards about "
    end = "in the format of Vocab Word -> Answer"
    prompt = beg + topic + end
    model = chat_models[0]
    
    response = openai.ChatCompletion.create(
        model=model,
        temperature=1, #0.6
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

def card_scraper(text, num):
    text = text.replace('\n','')
    if "Vocab Word: " not in text:    
        char_sep = text[1]
        text = text.lstrip("1" + char_sep + " ")
    else:
        char_sep = "Vocab Word: "
        text = text.lstrip(char_sep)
    
    if "Answer: " in text:
        divider = "Answer: "
    elif " -> " in text:
        divider = " -> "
        
    flashcards = []
    for i in range(2, (num + 1)):
        if char_sep == "Vocab Word: ":
            seperator = "Vocab Word: "
        else: 
            seperator = str(i) + char_sep + " "

        texts = text.split(seperator)
        print(texts)
        text = texts[1]
        phrase = texts[0]

        card = phrase.split(divider)
        if len(card) != 0:
            flashcards.append(card)
        
        if i == num:
            phrase = texts[1]
            card = phrase.split(divider)
            if len(card) != 0:
                flashcards.append(card)
        
    return flashcards


# TESTING CODE

# response = generate_card_response("American Revolution", 10, 600)
# raw_text = response["choices"][0]["message"]["content"] 
# print(raw_text)
# print(card_scraper(raw_text, 10))
# text instead of content for gpt-3.0 models
# raw_text = "1. Profesor -> Teacher\n2. Estudiante -> Student\n3. Clase -> Class\n4. Tarea -> Homework\n5. Examen -> Exam\n6. Escuela -> School"
#print(card_scraper(raw_text, 10))
#print(card_scraper(raw_text))

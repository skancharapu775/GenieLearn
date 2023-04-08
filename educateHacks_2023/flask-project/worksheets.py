import openai
import keys

openai.api_key = keys.API_KEY
chat_models = ["gpt-3.5-turbo"]
completion_models = ["davinci", "curie", "babbage", "ada", "babbage:ft-personal:babbage-4-2023-04-08-13-57-22"]

def pdf_writer(problems):
    return

def generate_response(topic, num, max_tokens):
    beg = "Create" + str(num) + " practice problems on "
    end = "in the format of Question -> Answer"
    prompt = beg + topic + end
    model = chat_models[0]

    
    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.6,
        max_tokens=max_tokens,
        messages = [{"role":"user", "content": prompt}]
    )

    return response

def parse(text, num):
    text = text.replace('\n','')
    text = text.lstrip("1. ")
    
    problem_pairs = []
    for i in range(2, (num + 1)):
        seperator = str(i) + ". "

        texts = text.split(seperator)
        text = texts[1]
        phrase = texts[0]

        pair = phrase.split("Answer: ")
        
        if len(pair) != 0:
            problem_pairs.append(pair)
        
        if i == num:
            phrase = texts[1]
            pair = phrase.split("Answer: ")
            if len(pair) != 0:
                problem_pairs.append(pair)
        
    return problem_pairs

response = generate_response("Hyperbola", 3, 300)
raw_text = response["choices"][0]["message"]["content"] 

print(parse(raw_text, 3))
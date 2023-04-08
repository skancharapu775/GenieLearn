import openai
import keys

openai.api_key = keys.API_KEY
chat_models = ["gpt-3.5-turbo"]
completion_models = ["davinci", "curie", "babbage", "ada", "babbage:ft-personal:babbage-4-2023-04-08-13-57-22"]


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
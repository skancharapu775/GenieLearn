import openai
import keys
import pdfkit

openai.api_key = keys.API_KEY
chat_models = ["gpt-3.5-turbo"]
completion_models = ["davinci", "curie", "babbage", "ada", "babbage:ft-personal:babbage-4-2023-04-08-13-57-22"]


def createpdf(problems, answers, topic):
    '''
    sudo apt-get update
    sudo apt-get install xvfb libfontconfig wkhtmltopdf
    pip install pdfkit
    pip install wkhtmltopdf
    '''
    title = topic
    
    html_string = """<h1><b></b></h1>
       <p>1st line ...</p>
       <p>2nd line ...</p>
       <p>3rd line ...</p>
       <p>4th line ...</p>
       """

    # for i in range(len(problems)):
    pdfname = "Practice_Worksheet.pdf"
    pdfkit.from_string(html_string, output_path = pdfname)

    return pdfname

def generate_sheet_response(topic, num, max_tokens):
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

def problem_scraper(text, num):
    text = text.replace('\n','')
    char_sep = text[1]
    
    text.lstrip("1" + char_sep + " ")
    text = text.lstrip("1. ")

    problem_pairs = []
    for i in range(2, (num + 1)):
        seperator = str(i) + char_sep + " "

        texts = text.split(seperator)
        print(text)
        text = texts[1]
        phrase = texts[0]

        pair = phrase.split("Answer: ")
        
        if len(pair) != 0:
            print(pair)
            pair[0] = pair[0].rstrip(" ")
            pair[0] = pair[0].rstrip(".")
            pair[1] = pair[1].rstrip(" ")
            pair[1] = pair[1].rstrip(".")

            problem_pairs.append(pair)
        
        if i == num:
            phrase = texts[1]
            pair = phrase.split("Answer: ")
            if len(pair) != 0:
                pair[0] = pair[0].rstrip(" ")
                pair[0] = pair[0].rstrip(".")
                pair[1] = pair[1].rstrip(" ")
                pair[1] = pair[1].rstrip(".")

                problem_pairs.append(pair)
        
    return problem_pairs

print(createpdf("problem", "answer", "Spanish Food"))

'''
response = generate_sheet_response("Math", 2, 100)
text = response["choices"][0]["message"]["content"]
print(text)
cards = problem_scraper(text, 2)
'''

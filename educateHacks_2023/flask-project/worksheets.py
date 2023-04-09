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
    brew install wkhtmltopdf
    '''
    title = topic.title()
    
    
    new_line = "<br>"
    html_string = """<h1 style="text-align:center"><b>""" + title + " Practice Worksheet </b></h1>"
    info_field = """<h3 style="text-align:center">Name: _____________________   Date: _____________</h3>"""
    html_string += info_field + new_line * 2

    for i in range(len(problems)):
        line = "<h3>" + str(i+1) + ") " + problems[i]["question"] + "</h3>"
        html_string += line + new_line * 2

    html_string += new_line * 2
    answer_title = """<h2 style="text-align:center">Answer Key</h2>"""
    html_string += answer_title + new_line
    for i in range(len(answers)):
        line = """<h3 style="text-align:center">""" + str(i+1) + ": " + problems[i]["answer"] + "</h3>"
        html_string += line

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
        temperature=1,
        max_tokens=max_tokens,
        messages = [{"role":"user", "content": prompt}]
    )

    return response

def problem_scraper(text, num):
    if "Q: " in text and "A: " in text:
        text = text.lstrip("Q: ")
        texts = text.split("Q: ")

        problem_pairs = []
        for QA_com in texts:
            pair = QA_com.split("A: ")

            if len(pair) != 0:
                    pair[0] = pair[0].rstrip(" ")
                    pair[0] = pair[0].rstrip(".")
                    pair[1] = pair[1].rstrip(" ")
                    pair[1] = pair[1].rstrip(".")

                    problem_pairs.append(pair)
        return problem_pairs
        
        
    else:
        text = text.replace('\n','')
        char_sep = text[1]
        
        text = text.lstrip("1" + char_sep + " ")

        if " -> " in text:
            divider = " -> "
        elif "Answer: " in text:
            divider = "Answer: "

        problem_pairs = []
        for i in range(2, (num + 1)):
            
            seperator = str(i) + char_sep + " "

            texts = text.split(seperator)
            print(text)
            text = texts[1]
            phrase = texts[0]


            pair = phrase.split(divider) # Answer: + " "
            
            if len(pair) != 0:
                # print(pair)
                pair[0] = pair[0].rstrip(" ")
                pair[0] = pair[0].rstrip(".")
                pair[1] = pair[1].rstrip(" ")
                pair[1] = pair[1].rstrip(".")
                # print("No error")

                problem_pairs.append(pair)
            
            if i == num:
                phrase = texts[1]
                pair = phrase.split(divider) # Answer: + " "
                if len(pair) != 0:
                    pair[0] = pair[0].rstrip(" ")
                    pair[0] = pair[0].rstrip(".")
                    pair[1] = pair[1].rstrip(" ")
                    pair[1] = pair[1].rstrip(".")

                    problem_pairs.append(pair)
            
        return problem_pairs


#problems = ["1+1", "2+2", "5 x 4", "10/2", "1/0"]
#answers = ["2", "4", "20", "5", "undefined"]
#print("Successful: " + createpdf(problems, answers, "Spanish Food"))


'''
response = generate_sheet_response("Hyperbola", 5, 500)
text = response["choices"][0]["message"]["content"]
print(text)
print(problem_scraper(text, 5))
'''



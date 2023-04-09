#boilerplate for testing
from flask import Flask, request
from flask_cors import CORS
import json
from flashcards import *
from worksheets import *
# from deepai import *

app = Flask(__name__)
CORS(app)

flashcard_number = 0
flashcard_topic = ''
number_problems = 0
worksheet_topic = ''

# flask function that SENDS data to the client
@app.route('/members')
def members ():
    return {"members": ["Member1", "Member2", "Member3"]}

# flask function that RECEIVES data from the client
@app.route('/flashcards', methods=['GET', 'POST'])
def flashcards ():
    # incoming data is in a JSON format, it looks like this: {'name': 'qweqweqweqwe', 'topic': '123123123123'}
    # we can access the data like this: request.json['name']
    # use this function for now, and put the ML stuff in the == 'POST' block
    #I can work on sending the data back to the client when we meet up tommorow
    global flashcard_number
    global flashcard_topic

    if request.method == 'POST':
        # runs when data is sent
        flashcard_number = int(request.json['number'])
        flashcard_topic = request.json['topic']

        return ('', 204)

    if request.method == 'GET':
        """
        --SAMPLE FLASHCARD STRUCTURE--
        flashcard = {
            "id": 1,
            "question": 'What is 2 + 2?',
            "answer": '4',
            "options": [
                '2',
                '3',
                '4',
                '5'
            ]
        }

        return function like this
        
        FLASHCARDS = {'response_code': 0,'results': [ flashcard1 , flashcard2, etc]}
        return(json.dumps(FLASHCARDS))
        """
        
        num = flashcard_number
        topic = flashcard_topic
        
        response = generate_card_response(topic, num, num * 100)
        text = response["choices"][0]["message"]["content"]
        cards = card_scraper(text, num)

        ALLCARDS = []

        for i in range(0, len(cards)):
            pair = cards[i]
            card = {}
            card["id"] = i + 1
            card["question"] = pair[0]
            card["answer"] = pair[1]
            card["options"] = []
        
            ALLCARDS.append(card)

        '''
        Generate image
        json_response = generate_image(topic)

        response format = {
        'id': 'e1a85509-1386-4f8d-9005-5d8f2ba659c9'
        'output_url': 'https://api.deepai.org/job-view-file/e1a85509-1386-4f8d-9005-5d8f2ba659c9/outputs/output.jpg'
        }
        '''

        FLASHCARDS = {'response_code': 0, 'results': ALLCARDS}
        return (json.dumps(FLASHCARDS)) 

# worksheet requests
@app.route('/worksheets', methods=['GET', 'POST'])
def worksheets ():

    global number_problems 
    global worksheet_topic

    if request.method == "POST":

        """
            -- SAMPLE PROBLEM STRUCTURE --
            PROBLEM AND ANSWER ID MATCH
            {
                problem = {
                "id": 1,
                "question": 'What is 2 + 2?',
                "answer_id": '1',
                "options": []
                }
            }
            
            -- SAMPLE ANSWER STRUCTURE
            PROBLEM AND ANSWER ID MATCH
            {
                answer = {
                "id": 1,
                "question_id": '1',
                "answer": '5',
                "options": []
                }
            }
        """

        number_problems = int(request.json['number'])
        worksheet_topic = request.json['topic']

        return ('', 204)
      
    if request.method == "GET":
        num = number_problems
        topic = worksheet_topic
        

        response = generate_sheet_response(topic, num, num * 100)
        text = response["choices"][0]["message"]["content"] 
        problem_pairs = problem_scraper(text, num)

        PROBLEMS = []
        ANSWERS = []

        for i in range(0, len(problem_pairs)):
            pair = problem_pairs[i]
            problem = {}
            problem["id"] = i + 1
            problem["question"] = pair[0]
            problem["answer_id"] = i + 1
            problem["options"]= []
        
            PROBLEMS.append(problem)

            answer = {}
            answer["id"] = i + 1
            answer["question_id"] = i + 1
            problem["answer"] = pair[1]
            problem["options"] = []

            ANSWERS.append(answer)

        PAIRS = {'response_code': 0, 'results': [PROBLEMS, ANSWERS]}
        print(PAIRS)
        return (json.dumps(PAIRS)) 

if __name__ == '__main__':
    app.run(debug=True)
#boilerplate for testing
from flask import Flask, request
from flask_cors import CORS
import json
from flashcards import *

app = Flask(__name__)
CORS(app)

flashcard_number = 0
flashcard_topic = ''

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
        
        response = generate_response(topic, num, 200)
        text = response["choices"][0]["message"]["content"]
        cards = parse(text, num)

        ALLCARDS = []

        for i in range(0, len(cards)):
            pair = cards[i]
            card = {}
            card["id"] = i + 1
            card["question"] = pair[0]
            card["answer"] = pair[1]
            card["options"] = []
        
            ALLCARDS.append(card)
        
        FLASHCARDS = {'response_code': 0, 'results': ALLCARDS}
        return (json.dumps(FLASHCARDS)) 
        
        '''one = {
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
        two = {
            "id": 2,
            "question": 'questions',
            "answer": 'yes',
            "options": [
                'yes',
                'no',
            ]
        }

        #this is the format for rendering the flashcards
        FLASHCARDS = {'response_code': 0,'results': []}
        if flashcard_number == 1:
            FLASHCARDS = {'response_code': 0,'results': [one]}
        elif flashcard_number == 2:
            FLASHCARDS = {'response_code': 0,'results': [one, two]}
        print(FLASHCARDS)
        flashcard_number = 0
        return(json.dumps(FLASHCARDS))'''


    

if __name__ == '__main__':
    app.run(debug=True)
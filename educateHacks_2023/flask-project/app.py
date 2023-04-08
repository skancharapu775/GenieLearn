#boilerplate for testing
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    
    
    if request.method == 'POST':
        # runs when data is sent
        print(request.json)
        
        one = {
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
            "answer": 'no',
            "options": [
                'yes',
                'no',
            ]
        }
        FLASHCARDS = [one, two]
        print(FLASHCARDS)
        return(FLASHCARDS)

        # return {"message": "data received"} # input data 

    if request.method == 'GET':
        one = {
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
            "answer": 'no',
            "options": [
                'yes',
                'no',
            ]
        }
        FLASHCARDS = [one, two]
        print(FLASHCARDS)
        return(FLASHCARDS)

    

if __name__ == '__main__':
    app.run(debug=True)
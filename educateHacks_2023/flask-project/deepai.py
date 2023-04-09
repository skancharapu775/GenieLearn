import requests

def generate_image(input_text):
    r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': input_text,
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    return r.json()
    

# print(generate_image("Hi"))
''' 
response format = {
 'id': 'e1a85509-1386-4f8d-9005-5d8f2ba659c9'
 'output_url': 'https://api.deepai.org/job-view-file/e1a85509-1386-4f8d-9005-5d8f2ba659c9/outputs/output.jpg'
}
'''
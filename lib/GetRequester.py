import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        pass

    def load_json(self):
        response = json.loads(self.get_response_body())



    get_requester =('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')


    response_json = get_requester.load_json()
    print (response_json)

    response_content = get_requester.get_response_body()
    print(response_content) 
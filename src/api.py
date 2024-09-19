import requests

class WordApi:
    def __init__(self):
        self.chosen_word = ""
        self.api_ulr = "https://random-word-api.herokuapp.com/word"

        self.get_word()

    @staticmethod
    def fetch_api(api_url):
        response = requests.get(api_url)

        if not response.status_code == requests.codes.ok:
            print("Error during fetching the API", response.status_code, response.text)
            return

        return response.text

    @staticmethod
    def clean_string(string):
        filtered_string = string.replace('[', '').replace(']', '').replace('"', '').upper()
        return filtered_string

    def get_word(self):
        response = self.fetch_api(self.api_ulr)

        if response:
            clean_string = self.clean_string(response)
            self.chosen_word = clean_string
            return self.chosen_word
        return
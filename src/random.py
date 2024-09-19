import requests

class Random:
    def __init__(self):
        self.word = ""

        self.get_word()

    def get_word(self):
        url = "https://random-word-api.herokuapp.com/word"
        response = requests.get(url)

        if response.status_code == requests.codes.ok:
            string = response.text
            filtered_string = string.replace('[', '').replace(']', '').replace('"', '')
            self.word = filtered_string.upper()
            print(self.word)
        else:
            print("Error during fetching the API", response.status_code, response.text)

        return self.word
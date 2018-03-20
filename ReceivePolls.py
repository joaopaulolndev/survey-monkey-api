import json
from Config import *


class ReceivePolls(Config):

    def __init__(self, survey_monkey_id):
        super().__init__(survey_monkey_id)

    def get_polls(self):
        return self.client.get(self.uri, headers=self.headers).json()

    def get_all_questions_per_poll(self):
        survey_finish_string = "/" + self.survey_id + "/responses/bulk"
        response = self.client.get(self.uri + survey_finish_string, headers=self.headers)
        response = response.json()
        if not 'error' in response.keys():
            self.get_question(response)

    def get_question(self, data):
        for p in data['data']:
            for page in p['pages']:
                page_id = page['id']
                for question in page['questions']:
                    question_id = question['id']
                    survey_finish_string = "/" + self.survey_id + "/pages/" + page_id + "/questions/" + question_id
                    # survey_finish_string = "/" + survey_id + "/pages/" + page_id + "/questions/" + question_id
                    response = self.client.get(self.uri + survey_finish_string, headers=self.headers)
                    response_questions = response.json()
                    print(json.dumps(response_questions))


try:
    survey_id = 129925673
    sm = ReceivePolls(survey_id)
    # polls = sm.get_polls()
    sm.get_all_questions_per_poll()
except NameError:
    print("Ocorreu um erro durante a execução: " + str(NameError))

import requests


class Config:

    def __init__(self, survey_id):
        self.client = requests.session()
        self.ACCESS_TOKEN = "09qPXWqFCMBh5nrgYL8-VPgLu58G7h8C8-ReTBZngVI7BwG2CvBeO7OCVU4Y7n5UCdJfk2cJB5DscY.tMiXejm3-erWr1rtI0h5l4op61NX8pLWQNl5UlUlJTFvtGzRW"
        self.headers = {
            "Authorization": "bearer %s" % self.ACCESS_TOKEN,
            "Content-Type": "application/json"
        }
        self.HOST = "https://api.surveymonkey.net"
        self.SURVEY_LIST_ENDPOINT = "/v3/surveys"
        self.uri = "%s%s" % (self.HOST, self.SURVEY_LIST_ENDPOINT)
        self.survey_id = str(survey_id)

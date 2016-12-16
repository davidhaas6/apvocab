from flask import url_for, request
import requests
import views


class StudySet:
    def __init__(self, access_token):
        self.title = ''
        self.vocab = []
        self.access_token = access_token

    def add_term(self, term):
        self.vocab += [term]

    def set_title(self, title):
        self.title = title

    def create_set(self):
        set_endpoint_url = 'https://api.quizlet.com/2.0/sets'
        terms = [x[0] for x in self.vocab]
        definitions = [x[1] for x in self.vocab]

        if len(self.vocab) < 2:
            raise Exception('Must have at least two terms!')
        if len(self.title) == 0:
            raise Exception('Must have a title!')

        header = {'Authorization': 'Bearer ' + self.access_token}
        set_info = \
            {'terms[]': terms, 'definitions[]': definitions, 'title': self.title, 'lang_terms': 'en',
             'lang_definitions': 'en'}
        new_set = requests.post(set_endpoint_url, headers=header, params=set_info)

        return "https://quizlet.com" + new_set['url']


def get_params():
    secret_token = 'VB3bgNCj3b86NEZDkD6Gfa'
    code = request.args.get('code')
    prev_page = request.args.get('state')

    pars = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': request.url_root[:-1] + url_for('quizlet_redirect')}
    response = requests.post('https://api.quizlet.com/oauth/token', params=pars, auth=(views.client_id, secret_token))
    print response.json()
    return [response.json()['access_token'], prev_page]

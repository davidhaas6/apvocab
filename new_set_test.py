import requests


# SETS MUST CONTAIN AT LEAST 2 TERMS AND DEFS
def make_set(title, vocab_set, token):
    terms = [x[0] for x in vocab_set]
    definitions = [x[1] for x in vocab_set]
    url = 'https://api.quizlet.com/2.0/sets'

    header = {'Authorization': 'Bearer ' + token}

    set_info = \
        {'terms[]': terms, 'definitions[]': definitions, 'title': title, 'lang_terms': 'en',
         'lang_definitions': 'en'}
    return requests.post(url, headers=header, params=set_info)


secret_token = 'VB3bgNCj3b86NEZDkD6Gfa'
client_id = 'nMPK85cZxV'

redirect = 'https://quizlet.com/authorize?response_type=code&client_id=' + client_id + '&scope=write_set&state=xd'

print redirect
# http://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url
# GET THE STUFF FROM THE URL PARAMETERS WHEN UR REDIRECTED
code = raw_input('code=')
pars = {'grant_type': 'authorization_code', 'code': code, 'redirect_uri': 'http://search.apvocab.com/'}
r = requests.post('https://api.quizlet.com/oauth/token', params=pars, auth=(client_id, secret_token))
print r.json()
access_token = r.json()['access_token']

sets = make_set('hi123123', [('t1', 'd1'), ('t2', 'd2')], access_token)
print sets.json()

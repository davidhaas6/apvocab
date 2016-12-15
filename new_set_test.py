import requests


def api_get(url): return requests.get(url + 'client_id=nMPK85cZxV&whitespace=0').json()


def make_set(title, vocab_set):
    terms = [x[0] for x in vocab_set]
    definitions = [x[1] for x in vocab_set]
    # "lang_terms=fr"
    # "lang_definitions=fr"
    return api_get('https://api.quizlet.com/2.0/sets/')


# https://api.quizlet.com/2.0/sets

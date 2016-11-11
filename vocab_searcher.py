import pickle
import re


class VocabSearch:
    def __init__(self, database_path):
        with open(database_path, 'rb') as handle:
            self.defs = pickle.load(handle)

    def search(self, word):
        answers = []
        num_results = 25
        if ':' in word:
            num_results = int(re.search('(\d+)$', word).group(0))
            word = word[:word.find(':')]
        if word.startswith('"') and word.endswith('"'):
            for key in self.defs:
                if word[1:-1].lower() == key.lower().strip():
                    answers += [(unicode(key.strip().capitalize()),
                                 unicode(self.defs[key].strip().capitalize()).replace('\n', ''))]
        else:
            for key in self.defs:
                if word.lower() in key.lower().strip():
                    answers += [(unicode(key.strip().capitalize()),
                                 unicode(self.defs[key].strip().capitalize()).replace('\n', ''))]

        if len(answers) is 0:
                return [('Term not found', ':( Sorry')]
        return answers[:num_results]

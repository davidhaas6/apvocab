from difflib import SequenceMatcher
import pickle
import re


class VocabSearch:
    def __init__(self, database_path):
        with open(database_path, 'rb') as handle:
            self.defs = pickle.load(handle)

    def search(self, word):
        answers = []
        num_results = 35
        if ':' in word:
            num_results = int(re.search('(\d+)$', word).group(0))
            word = word[:word.find(':')]

        if word.startswith('"') and word.endswith('"'):
            for term in self.defs:
                if word[1:-1].lower() == term.lower().strip():
                    answers += [(unicode((self.clean_term(term))),
                                 unicode(self.clean_definition(self.defs[term])))]

        else:
            for term in self.defs:
                if word.lower() in term.lower().strip():
                    answers += [(unicode((self.clean_term(term))),
                                 unicode(self.clean_definition(self.defs[term])))]

        not_found_statement = [('No results found for "' + word + '"', ':( Sorry')]
        if len(answers) is 0:
            if word.strip() != word:
                new_answers = self.search(word.strip())
                if len(new_answers) > 0:
                    return not_found_statement + [('Results were found when we searched "' + word.strip() + '", however',
                                                   'Here ya go :)'), ('', '')] + new_answers
            return not_found_statement

        # If you remove_similar for all of the results, it can take a long time if there's a lot of results, so i do
        # 1.25 times the amount of desired results just to have a little bit of a buffer space
        answers = self.remove_similar(self.sort_results(answers)[:int(num_results*1.25)])
        return answers

    # Cleans junk off of the end of terms and capitalizes it
    def clean_term(self, term):
        if term[-1] in ['-', ':', '*']:
            return term[:-1]
        return term.title().strip()

    def clean_definition(self, definition):
        definition = ' '.join(definition.split())
        try:
            # Chop off beginning characters that aren't letters/numbers and aren't those exceptions listed below
            while not str(definition[0]).isalnum() and definition[0] not in ['(', '\"', '\'']:
                definition = definition[1:]
        except UnicodeEncodeError:
            definition = definition[1:].strip()
            while not str(definition[0]).isalnum() and definition[0] not in ['(', '\"', '\'']:
                definition = definition[1:]

        return definition.strip().capitalize()

    # Sorts the results so that results with the shortest term appear first -- meant to improve accuracy of results
    def sort_results(self, results):
        # Creates an array of the results with the format: [(len(term1), (term1, definition1)), ...]
        len_arr = [(len(term), (term, definition)) for term, definition in results]

        # Sorts the above array by the length of the term from least to greatest
        len_arr.sort(key=lambda x: x[0])

        # Removes the len(term) element to the array returns to the format: [(term1, definition1), ...]
        return [(elem[1]) for elem in len_arr]

    def similar(self, a, b):
        return SequenceMatcher(None, a, b).ratio()

    # Takes a while for long lists b/c similar() is a bit resource intensive
    def remove_similar(self, results):
        ratio_threshold = .95
        new_results = results[:]
        for i in range(0, len(results)):
            for j in range(i+1, len(results)):
                if self.similar(results[i][1], results[j][1]) >= ratio_threshold:
                    if results[j] in new_results:
                        new_results.remove(results[j])

        return new_results

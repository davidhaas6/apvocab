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
                    cleaned_def = self.clean_definition(self.defs[term])
                    if len(cleaned_def) > 1:
                        answers += [(unicode((self.clean_term(term))), cleaned_def)]

        else:
            for term in self.defs:
                if word.lower() in term.lower().strip():
                    cleaned_def = self.clean_definition(self.defs[term])
                    if len(cleaned_def) > 1:
                        answers += [(unicode((self.clean_term(term))), cleaned_def)]

        not_found_statement = [('No results found for "' + word + '"', ':( Sorry')]
        if len(answers) is 0:
            if word.strip() != word:
                new_answers = self.search(word.strip())
                if len(new_answers) > 0:
                    return not_found_statement + [('Results were found when we searched "' + word.strip() + '", however',
                                                   'Here ya go :)'), ('', '')] + new_answers
            return not_found_statement

        return self.sort_results(answers)[:num_results]

    @staticmethod
    def remove_non_ascii(string):
        return "".join(i for i in string if ord(i) < 128)

    # Cleans junk off of the end of terms and capitalizes it
    def clean_term(self, term):
        term = self.remove_non_ascii(term)
        if term[-1] in ['-', ':', '*']:
            return term[:-1]
        return term.title().strip()

    def clean_definition(self, definition):
        definition = ' '.join(definition.split())
        definition = self.remove_non_ascii(definition)
        # Chop off beginning characters that aren't letters/numbers and aren't those exceptions listed below
        while len(definition) > 0 and not str(definition[0]).isalnum() and definition[0] not in ['(', '\"', '\'']:
            definition = definition[1:]

        return definition.strip().capitalize()

    # Sorts the results so that results with the shortest term appear first -- meant to improve accuracy of results
    @staticmethod
    def sort_results(results):
        # Creates an array of the results with the format: [(len(term1), (term1, definition1)), ...]
        len_arr = [(len(term), (term, definition)) for term, definition in results]

        # Sorts the above array by the length of the term from least to greatest
        len_arr.sort(key=lambda x: x[0])

        # Removes the len(term) element to the array returns to the format: [(term1, definition1), ...]
        return [(elem[1]) for elem in len_arr]

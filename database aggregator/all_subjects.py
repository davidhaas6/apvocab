from quizlet_aggregator import Filler
from difflib import SequenceMatcher
import pickle

'''
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# Takes a while for long lists b/c similar() is a bit resource intensive
def remove_similar(results):
    ratio_threshold = .95
    new_results = results[:]
    for i in range(0, len(results)):
        for j in range(i + 1, len(results)):
            if similar(results[i][1], results[j][1]) >= ratio_threshold:
                if results[j] in new_results:
                    new_results.remove(results[j])

    return new_results
'''


def make_def((subject_name, subject_terms)):
    max_num_terms = 30000
    print 'Starting', subject_terms[0] + '...'
    vocab = Filler().get_vocab(subject_terms, max_num_terms)
    # print 'Finished!'
    # print 'Removing similar results...'
    # vocab = remove_similar(vocab)
    print 'Finished!\n'
    with open('../static/defs/' + subject_name + '_defs.pickle', 'wb') as handle:
        pickle.dump(vocab, handle)

'''
subjects = [('enviro', ['AP Enviro', 'APES']), ('gov', ['AP Gov', 'APGOV']), ('bio', ['AP Biology', 'AP Bio']),
            ('econ', ['AP Micro macro']), ('world', ['AP World History', 'AP World']),
            ('ushistory', ['AP US History', 'APUSH']), ('lang', ['AP Lang']), ('humangeo', ['AP Human Geography']),
            ('euro', ['AP Euro']), ('psych', ['AP Psychology'])]
'''

subjects = [('physics-c', ['AP Physics C']), ('physics1', ['AP Physics 1']), ('physics2', ['AP Physics 2']),
            ('compgov', ['AP Comparative Government']), ('lit', ['AP Lit']), ('stat', ['AP Statistics'])]

for subject in subjects:
    try:
        make_def(subject)
    except Exception as e:
        print e

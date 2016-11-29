import pickle
from quizlet_aggregator import Filler


def make_def((subject_name, subject_terms)):
    max_num_terms = 30000
    print 'Starting', subject_terms[0] + '...'
    vocab = Filler().get_vocab(subject_terms, max_num_terms)
    print 'Finished!\n'
    with open('../static/defs/' + subject_name + '_defs.pickle', 'wb') as handle:
        pickle.dump(vocab, handle)


subjects = [('enviro', ['AP Enviro', 'APES']), ('gov', ['AP Gov', 'APGOV']), ('bio', ['AP Biology', 'AP Bio']),
            ('econ', ['AP Micro macro']), ('world', ['AP World History', 'AP World']),
            ('ushistory', ['AP US History', 'APUSH']), ('lang', ['AP Lang']), ('humangeo', ['AP Human Geography']),
            ('euro', ['AP Euro']), ('psych', ['AP Psychology'])]

for subject in subjects:
    try:
        make_def(subject)
    except Exception as e:
        print e

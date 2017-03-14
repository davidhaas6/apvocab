from flask import render_template, flash, session
from forms import SearchForm
import vocab_searcher
import views
import os


class TopicSearch:
    def __init__(self, def_name, subject, shorthand, description):
        def_path = os.path.join(os.path.dirname(__file__) + '/static/defs/', def_name) + '_defs.pickle'
        self.vocab = vocab_searcher.VocabSearch(def_path)
        self.subject = subject
        self.def_name = def_name
        self.shorthand = shorthand
        self.description = description

    def search(self):
        search_topic = "Search " + self.subject
        search_form = SearchForm()
        if search_form.validate_on_submit():
            term = search_form.term.data
            flash(self.vocab.search(term), 'definitions')
            views.num_searches += 1
            print term, views.num_searches
        return render_template('search.html',
                               title='Search a term',
                               form=search_form,
                               search_topic=search_topic,
                               current={self.def_name: True},
                               topics=views.main_topics,
                               creating_set=session['study_set'] is not None)

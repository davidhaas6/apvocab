import os
from flask import render_template, flash
import vocab_searcher
from forms import SearchForm


class TopicSearch:
    def __init__(self, def_name, topic):
        def_path = os.path.join(os.path.dirname(__file__) + '/static/defs/', def_name) + '_defs.pickle'
        self.vocab = vocab_searcher.VocabSearch(def_path)
        self.topic = topic
        self.def_name = def_name

    def search(self):
        form = SearchForm()
        search_topic = "Search " + self.topic
        if form.validate_on_submit():
            term = form.term.data
            print term
            flash(self.vocab.search(term))
        return render_template('search.html',
                               title='Search a term',
                               form=form,
                               search_topic=search_topic,
                               current={self.def_name: True})

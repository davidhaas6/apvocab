from datetime import datetime

import pytz
from flask import render_template

from TopicSearch import TopicSearch
from init import app

gov = TopicSearch(
    def_name='gov', subject='AP Government', shorthand='AP Government', description='mr. dolan turnip')
enviro = TopicSearch(
    def_name='enviro', subject='AP Environmental Sciences', shorthand='AP Enviro', description='rip earth')
psych = TopicSearch(
    def_name='psych', subject='AP Psychology', shorthand='AP Psych', description='also a good tv show')
bio = TopicSearch(
    def_name='bio', subject='AP Biology', shorthand='AP Biology', description='biolology')
econ = TopicSearch(
    def_name='econ', subject='AP Micro/macroeconomics', shorthand='AP Micro/Macro',
    description='grades lower than the peso')
world = TopicSearch(
    def_name='world', subject='AP World History', shorthand='AP World', description='i can show u the world')
ushistory = TopicSearch(
    def_name='ushistory', subject='AP US History', shorthand='AP US History', description='apush 2 far')
lang = TopicSearch(
    def_name='lang', subject='AP English Language', shorthand='AP Lang', description='lang gang')
euro = TopicSearch(
    def_name='euro', subject='AP European History', shorthand='AP Euro History', description='ur a\'peein')
humangeo = TopicSearch(
    def_name='humangeo', subject='AP Human Geography', shorthand='AP Human Geo', description='dis Ghana be good')

chem = TopicSearch(
    def_name='chem', subject='AP Chemistry', shorthand='AP Chemistry', description='idek dood')
calc = TopicSearch(
    def_name='calc', subject='AP Calculus', shorthand='AP Calculus', description='dont forget +c')

# This determines the order they appear on the site
main_topics = [world, enviro,
               humangeo, bio,
               gov, econ,
               ushistory, psych,
               euro, lang]
all_topics = main_topics + [chem, calc, ]

num_searches = 0
est = pytz.timezone('US/Eastern')
i = datetime.now(est)
boot_time = i.strftime('%b %d, %I:%M %p')


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", current={}, topics=main_topics)


@app.route('/about')
def about():
    return render_template("about.html", current={}, topics=main_topics, search_count=num_searches, boot_time=boot_time)


@app.route('/tips')
def tips():
    return render_template("tips.html", current={}, topics=main_topics)


for t in all_topics:
    app.add_url_rule(rule='/' + t.def_name, endpoint=t.def_name, view_func=t.search, methods=['GET', 'POST'])

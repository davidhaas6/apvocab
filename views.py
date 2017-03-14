from datetime import datetime

import pytz
from flask import render_template, redirect, url_for, request, jsonify, session

from TopicSearch import TopicSearch
from init import app
import quizlet_set


gov = TopicSearch(
    def_name='gov', subject='AP Government', shorthand='AP Government', description='mr. dolan turnip')
enviro = TopicSearch(
    def_name='enviro', subject='AP Environmental Sciences', shorthand='AP Enviro', description='rip earth')
psych = TopicSearch(
    def_name='psych', subject='AP Psychology', shorthand='AP Psych', description='syyyke')
bio = TopicSearch(
    def_name='bio', subject='AP Biology', shorthand='AP Biology', description='biolology')
econ = TopicSearch(
    def_name='econ', subject='AP Micro/macroeconomics', shorthand='AP Micro/Macro',
    description='dont waste-o ur peso')
world = TopicSearch(
    def_name='world', subject='AP World History', shorthand='AP World', description='i can show u the world')
ushistory = TopicSearch(
    def_name='ushistory', subject='AP US History', shorthand='AP US History', description='apush 2 far')
lang = TopicSearch(
    def_name='lang', subject='AP English Language', shorthand='AP Lang', description='lang gang')
euro = TopicSearch(
    def_name='euro', subject='AP European History', shorthand='AP Euro History', description='[insert quality pun]')
humangeo = TopicSearch(
    def_name='humangeo', subject='AP Human Geography', shorthand='AP Human Geo', description='dis Ghana be good')

chem = TopicSearch(
    def_name='chem', subject='AP Chemistry', shorthand='AP Chemistry', description='idek dood')
calc = TopicSearch(
    def_name='calc', subject='AP Calculus', shorthand='AP Calculus', description='dont forget +c')
physics_c = TopicSearch(
    def_name='physics-c', subject='AP Physics C', shorthand='AP Physics C', description='i c thru the matrix')
physics1 = TopicSearch(
    def_name='physics1', subject='AP Physics 1', shorthand='AP Physics 1', description='11111')
physics2 = TopicSearch(
    def_name='physics2', subject='AP Physics 2', shorthand='AP Physics 2', description='22222')
compgov = TopicSearch(
    def_name='compgov', subject='AP Comparative Government', shorthand='AP Comp-Gov', description='comp this')
lit = TopicSearch(
    def_name='lit', subject='AP Literature', shorthand='AP Lit', description='shit\'s lit')
stat = TopicSearch(
    def_name='stat', subject='AP Statistics', shorthand='AP Statistics', description='stat my rat')

# This determines the order they appear on the site
main_topics = [world, enviro,
               humangeo, bio,
               gov, econ,
               ushistory, psych,
               euro, lang]
side_topics = [chem, calc, stat, physics_c, physics1, physics2, lit, compgov]
all_topics = main_topics + side_topics

num_searches = 0
est = pytz.timezone('US/Eastern')
i = datetime.now(est)
boot_time = i.strftime('%b %d, %I:%M %p')

client_id = 'nMPK85cZxV'
access_token = ''
session['study_set'] = None


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", current={}, topics=main_topics, more_topics=side_topics)


@app.route('/about')
def about():
    return render_template("about.html", current={}, topics=main_topics, search_count=num_searches, boot_time=boot_time)


@app.route('/tips')
def tips():
    return render_template("tips.html", current={}, topics=main_topics)


for t in all_topics:
    app.add_url_rule(rule='/' + t.def_name, endpoint=t.def_name, view_func=t.search, methods=['GET', 'POST'])


@app.route('/secret')
def secret():
    return render_template("secret_tests.html", current={}, topics=main_topics,
                           creating_set=session['study_set'] is not None, terms=session['study_set'].vocab)


@app.route('/new-set', methods=['GET', 'POST'])
def new_set():
    referral = request.referrer
    print referral
    return_url = request.url_root[:-1] + url_for('quizlet_redirect')
    print return_url
    redirect_url = 'https://quizlet.com/authorize?response_type=code&client_id=' + client_id + \
                   '&scope=write_set&state=' + referral + '&redirect_uri=' + return_url
    return redirect(redirect_url, code=302)


@app.route('/quizlet_redirect')
def quizlet_redirect():
    global access_token
    params = quizlet_set.get_params()
    access_token = params[0]
    prev = params[1]
    session['study_set'] = quizlet_set.StudySet(access_token=access_token)
    return redirect(prev)


@app.route('/_add_term')
def add_term():
    term = request.args.get('term')
    definition = request.args.get('def')
    if session['study_set'] is not None:
        session['study_set'].add_term(term)
    else:
        return 'ERROR: Cannot add term - no set created'
    return jsonify(session['study_set'].add_term((term, definition)))

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

topics = [world, enviro,
          humangeo, bio,
          gov, econ,
          ushistory, psych,
          euro, lang]


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", current={}, topics=topics)


@app.route('/about')
def about():
    return render_template("about.html", current={}, topics=topics)


@app.route('/tips')
def tips():
    return render_template("tips.html", current={}, topics=topics)


@app.route('/gov', methods=['GET', 'POST'])
def gov_page():
    return gov.search()


@app.route('/enviro', methods=['GET', 'POST'])
def enviro_page():
    return enviro.search()


@app.route('/psych', methods=['GET', 'POST'])
def psych_page():
    return psych.search()


@app.route('/bio', methods=['GET', 'POST'])
def bio_page():
    return bio.search()


@app.route('/econ', methods=['GET', 'POST'])
def econ_page():
    return econ.search()


@app.route('/world', methods=['GET', 'POST'])
def world_page():
    return world.search()


@app.route('/ushistory', methods=['GET', 'POST'])
def ushistory_page():
    return ushistory.search()


@app.route('/lang', methods=['GET', 'POST'])
def lang_page():
    return lang.search()


@app.route('/euro', methods=['GET', 'POST'])
def euro_page():
    return euro.search()


@app.route('/humangeo', methods=['GET', 'POST'])
def humangeo_page():
    return humangeo.search()

from flask import render_template
from TopicSearch import TopicSearch
from init import app

gov = TopicSearch('gov', 'AP Government')
enviro = TopicSearch('enviro', 'AP Environmental Sciences')
psych = TopicSearch('psych', 'AP Psychology')
bio = TopicSearch('bio', 'AP Biology')
econ = TopicSearch('econ', 'AP Micro/macroeconomics')
world = TopicSearch('world', 'AP World History')
ushistory = TopicSearch('ushistory', 'AP US History')
lang = TopicSearch('lang', 'AP English Language')
euro = TopicSearch('euro', 'AP European History')
humangeo = TopicSearch('humangeo', 'AP Human Geography')


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", current={})


@app.route('/about')
def about():
    return render_template("about.html", current={})


@app.route('/tips')
def tips():
    return render_template("tips.html", current={})


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

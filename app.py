# imports
from flask import Flask, request, render_template
from utils import *
import os
app = Flask(__name__)

# home page view, list of all candidates
@app.route('/')
def index():
    candidates = json_load_candidates()
    candidates_names_num = list(map(lambda item: {'num': item['id'], 'name': item['name']}, candidates))
    return render_template('list.html', names_num=candidates_names_num)

# individual candidate page view, listing data about him
@app.route('/candidate/<int:id_candidate>')
def page_candidate(id_candidate):
    candidate = get_candidate(id_candidate)
    name = candidate['name']
    position = candidate['position']
    src_image = candidate['picture']
    skills = candidate['skills']
    return render_template('card.html',
                           name=name,
                           position=position,
                           image=src_image,
                           skills=skills)

# search for candidates by name
@app.route('/search/<candidate_name>')
def search_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    candidates_names_num = list(map(lambda item: {'num': item['id'], 'name': item['name']}, candidates))
    len_candidates = len(candidates_names_num)
    return render_template('search.html', candidates_names_num=candidates_names_num, len_candidates=len_candidates)

# search for candidates by skill
@app.route('/skill/<skill_name>')
def search_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    candidates_names_num = list(map(lambda item: {'num': item['id'], 'name': item['name']}, candidates))
    len_candidates = len(candidates)
    return render_template('skill.html', candidates_names_num=candidates_names_num, len_candidates=len_candidates, skill_name=skill_name)
app.run()
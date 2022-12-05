import json
import os


def json_load_candidates():
    '''
    :return: returns a list of dictionaries loaded from json file
    '''
    with open(os.path.join('candidates.json'), 'r', encoding='utf-8') as candidates_file:
        candidates = json.load(candidates_file)
    return candidates


def get_candidate(candidate_id):
    '''
    :param candidate_id: number candidate at list candidates
    :return: returns a list candidates by candidate_id
    '''
    candidates = json_load_candidates()
    candidate = list(filter(lambda item: item['id'] == candidate_id, candidates))[0]
    return candidate


def get_candidates_by_name(candidate_name):
    '''
    :param candidate_name: name of candidate
    :return: returns a list candidates by name
    '''
    candidates = json_load_candidates()
    candidates_for_names = list(filter(lambda item: item['name'] == candidate_name, candidates))
    return candidates_for_names


def get_candidates_by_skill(skill_name):
    '''
    :param skill_name: skills of candidates
    :return: returns a list candidates by skill
    '''
    candidates = json_load_candidates()
    candidates_for_skills = list(filter(lambda item: skill_name.lower() in item['skills'].lower(), candidates))
    return candidates_for_skills






# http://127.0.0.1:5000/skill/python
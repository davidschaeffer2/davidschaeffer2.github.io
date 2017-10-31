# app/views.py
# David Schaeffer
# 10/23/2017

import csv
from flask import render_template, request
import os

from flask_app.app import app
from flask_app.forms import PartyInformationForm
from flask_app.models import PartyInformationLogic


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')


@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/finntools.html', methods=['GET', 'POST'])
def finntools():
    if request.method == 'POST':
        party_form = process_party_info_form()
        return render_template('finntools.html', party_form=party_form,
                               num_characters=party_form.number_of_characters.
                               data, available_creatures=
                               get_creatures_for_budget(
                                   party_form.exp_budget.data,
                                   party_form.filter_field.data))
    party_form = PartyInformationForm()
    return render_template('finntools.html', party_form=party_form)


def process_party_form_get(args):
    for arg in args.items():
        print(arg)
    party_form = PartyInformationForm()
    if args['number_of_characters']:
        party_form.number_of_characters.process_data(
            args['number_of_characters'])
        for field, data in args.items():
            if 'character_level' in field:
                party_form.character_level.append_entry(data)
        while party_form.number_of_characters.data > \
                len(party_form.character_level.entries):
            party_form.character_level.append_entry(1)
        while party_form.number_of_characters.data < \
                len(party_form.character_level.entries):
            party_form.character_level.pop_entry()
        party_form.difficulty.process_data(args['difficulty'])
        apl = round(
            PartyInformationLogic.get_apl(party_form.number_of_characters.data,
                                          party_form.character_level.data,
                                          party_form.difficulty.data))
        print('APL: %d' % apl)
        party_form.average_party_level.process_data(apl)
        exp_budget = PartyInformationLogic.get_cr_exp_budget(apl)
        party_form.exp_budget.process_data(exp_budget)
        party_form.filter_field.process_data(args['filter_field'])
    return party_form


def get_creatures_for_budget(exp_budget, filter_char):
    available_creatures = []
    with open('flask_app/bestiary.csv', 'r') as bestiary:
        dict_reader = csv.DictReader(bestiary)
        for creature in dict_reader:
            creature['XP'] = int(creature['XP'].replace(',', ''))
            if creature['XP'] <= exp_budget and \
                    creature['Name'].startswith(filter_char):
                available_creatures.append(creature)
    return available_creatures


# Below function is for POST, which doesn't work on gh-pages
def process_party_info_form():
    party_form = PartyInformationForm(request.form)
    while party_form.number_of_characters.data > \
            len(party_form.character_level.entries):
        party_form.character_level.append_entry(1)
    while party_form.number_of_characters.data < \
            len(party_form.character_level.entries):
        party_form.character_level.pop_entry()
    apl = round(
        PartyInformationLogic.get_apl(party_form.number_of_characters.data,
                                      party_form.character_level.data,
                                      party_form.difficulty.data))
    party_form.average_party_level.process_data(apl)
    exp_budget = PartyInformationLogic.get_cr_exp_budget(apl)
    party_form.exp_budget.process_data(exp_budget)
    return party_form

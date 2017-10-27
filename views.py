# app/views.py
# David Schaeffer
# 10/23/2017


import csv

from forms import PartyInformationForm
from flask import render_template, request

from app import app
from models import PartyInformationLogic


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/finntools/', methods=['GET', 'POST'])
def finntools():
    if request.method == 'GET':
        party_form = PartyInformationForm()
        return render_template('finntools.html', party_form=party_form)
    party_form = process_party_info_form()
    filter_char = party_form.filter_field.data or 'A'
    available_creatures = get_creatures_for_budget(party_form.exp_budget.data,
                                                   filter_char)
    return render_template('finntools.html', party_form=party_form,
                           num_characters=party_form.number_of_characters.data,
                           alphabet=PartyInformationLogic.get_alphabet(),
                           available_creatures=available_creatures)


def process_party_info_form():
    party_form = PartyInformationForm(request.form)
    print('Party_form object: {}'.format(party_form.data))
    while party_form.number_of_characters.data > \
            len(party_form.character_level.entries):
        party_form.character_level.append_entry(1)
    while party_form.number_of_characters.data < \
            len(party_form.character_level.entries):
        party_form.character_level.pop_entry()
    print('Num entries: %d' % len(party_form.character_level.entries))
    print(party_form.character_level.entries)
    print(party_form.character_level.data)
    apl = round(
        PartyInformationLogic.get_apl(party_form.number_of_characters.data,
                                      party_form.character_level.data,
                                      party_form.difficulty.data))
    print(apl)
    party_form.average_party_level.process_data(apl)
    exp_budget = PartyInformationLogic.get_cr_exp_budget(apl)
    print(exp_budget)
    party_form.exp_budget.process_data(exp_budget)
    return party_form


def get_creatures_for_budget(exp_budget, filter_char):
    available_creatures = []
    with open('./storage/bestiary.csv', 'r') as bestiary:
        dict_reader = csv.DictReader(bestiary)
        for creature in dict_reader:
            creature['XP'] = int(creature['XP'].replace(',', ''))
            if creature['XP'] <= exp_budget and \
                    creature['Name'].startswith(filter_char):
                available_creatures.append(creature)
    return available_creatures

from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FieldList, StringField

from models import PartyInformationLogic


class PartyInformationForm(FlaskForm):
    number_of_characters = SelectField('Number of Characters: ',
                                       choices=PartyInformationLogic.
                                       get_num_character_choices(),
                                       coerce=int, default=1)
    character_level = FieldList(SelectField(choices=PartyInformationLogic.
                                            get_player_level_choices(),
                                            coerce=int, default=1))
    average_party_level = IntegerField('Average Party Level (APL): ')
    difficulty = SelectField('Difficulty: ',
                             choices=PartyInformationLogic.
                             get_difficulty_choices(),
                             default='average')
    exp_budget = IntegerField('Experience Budget :', default=0)
    search_field = StringField('Search: ')
    filter_field = SelectField('Filter: ', choices=PartyInformationLogic.
                               get_alphabet(), default='A')

    @staticmethod
    def process_data(data):
        return data

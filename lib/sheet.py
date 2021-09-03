from enum import Enum

import openpyxl


class Sheet:
    def __init__(self):
        self.workbook = openpyxl.Workbook()
        self.sheet = self.workbook.active
        self.debug = False

    def __getitem__(self, key):
        # TODO: Debug logging
        if self.debug:
            print(f'[Debug] Get {key} ({self.sheet[key].value})')
        return self.sheet[key].value

    def __setitem__(self, key, value):
        # TODO: Debug logging
        if key in cell_map.keys():
            key = cell_map[key]

        if self.debug:
            print(f'[Debug] Set {key} = {value}')
        self.sheet[key] = value

    def save(self):
        self.workbook.save('output.xlsx')

    def set_by_section(self, section, key, value):
        self[section_map[section][key]] = value

    def get_by_section(self, section, key):
        return self[section_map[section][key]]


class Section(Enum):
    Stats = 1
    Bonds = 2
    BondScores = 3
    Skills = 4
    OtherSkills = 5
    Motivations = 6


section_map = {
    Section.Stats: {
        'STR': 'C8',
        'CON': 'C9',
        'DEX': 'C10',
        'INT': 'C11',
        'POW': 'C12',
        'CHA': 'C13',
    },
    Section.Bonds: {
        1: 'F9',
        2: 'F10',
        3: 'F11',
        4: 'F12',
        5: 'F13',
        6: 'F14',
    },
    Section.BondScores: {
        1: 'H9',
        2: 'H10',
        3: 'H11',
        4: 'H12',
        5: 'H13',
        6: 'H14',
    },
    Section.Skills: {
        'Accounting': 'C23',
        'Alertness': 'C24',
        'Anthropology': 'C25',
        'Archeology': 'C26',
        'Art': 'C27',
        'Artillery': 'C29',
        'Athletics': 'C30',
        'Bureaucracy': 'C31',
        'Computer Science': 'C32',
        'Craft': 'C33',
        'Criminology': 'C35',
        'Demolitions': 'C36',
        'Disguise': 'C37',
        'Dodge': 'C38',
        'Drive': 'C39',
        'Firearms': 'C40',
        'First Aid': 'E23',
        'Forensics': 'E24',
        'Heavy Machinery': 'E25',
        'Heavy Weapons': 'E26',
        'History': 'E27',
        'HUMINT': 'E28',
        'Law': 'E29',
        'Medicine': 'E30',
        'Melee Weapons': 'E31',
        'Military Science': 'E32',
        'Navigate': 'E34',
        'Occult': 'E35',
        'Persuade': 'E36',
        'Pharmacy': 'E37',
        'Pilot': 'E38',
        'Psychotherapy': 'E40',
        'Ride': 'G23',
        'Science': 'G24',
        'Search': 'G26',
        'SIGINT': 'G27',
        'Stealth': 'G28',
        'Surgery': 'G29',
        'Survival': 'G30',
        'Swim': 'G31',
        'Unarmed Combat': 'G32',
        'Unnatural': 'G33',
    },
    Section.OtherSkills: {
        1: 'G35',
        2: 'G36',
        3: 'G37',
        4: 'G38',
        5: 'G39',
        6: 'G40'
    },
    Section.Motivations: {
        0: 'E16',
        1: 'E17',
        2: 'E18',
        3: 'E19',
        4: 'E20',
    }
}


class Cell(Enum):
    Age = 1
    Birthday = 2
    Profession = 3
    RealName = 4
    Alias = 5
    School = 6
    Bio = 7
    Employer = 8
    Disorder = 9
    STR = 10
    CON = 11
    DEX = 12
    INT = 13
    POW = 14
    CHA = 15


cell_map = {
    Cell.Profession: 'C4',
    Cell.RealName: 'E1',
    Cell.Alias: 'D3',
    Cell.School: 'B3',
    Cell.Bio: 'J40',
    Cell.Employer: 'C5',
    Cell.Disorder: 'E21',
    Cell.STR: section_map[Section.Stats]['STR'],
    Cell.CON: section_map[Section.Stats]['CON'],
    Cell.DEX: section_map[Section.Stats]['DEX'],
    Cell.INT: section_map[Section.Stats]['INT'],
    Cell.POW: section_map[Section.Stats]['POW'],
    Cell.CHA: section_map[Section.Stats]['CHA'],
    Cell.Occult: section_map[Section.Skills]['Occult'],
}

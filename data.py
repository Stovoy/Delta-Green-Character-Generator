stat_list = ['STR', 'CON', 'DEX', 'INT', 'POW', 'CHA']

stat_dict = {
    'STR': 'C8',
    'CON': 'C9',
    'DEX': 'C10',
    'INT': 'C11',
    'POW': 'C12',
    'CHA': 'C13'
}

skill_packages = {
    'Artist': ['Alertness', 'Craft (Choose One)', 'Disguise',
               'Persuade', 'Art (Choose One)', 'Art (Choose Another)',
               'Art (Choose one more)', 'HUMINT'],
    'Actor': ['Alertness', 'Craft (Choose One)', 'Disguise',
              'Persuade', 'Art (Choose One)', 'Art (Choose Another)',
              'Art (Choose one more)', 'HUMINT'],
    'Musician': ['Alertness', 'Craft (Choose One)', 'Disguise',
                 'Persuade', 'Art (Choose One)', 'Art (Choose Another)',
                 'Art (Choose one more)', 'HUMINT'],
    'Athlete': ['Alertness', 'Athletics', 'Dodge', 'First Aid',
                'HUMINT', 'Persuade', 'Swim', 'Unarmed Combat'],
    'Author': ['Anthropology', 'Art (Choose One)', 'Bureaucracy', 'History',
               'Law', 'Occult', 'Persuade', 'HUMINT'],
    'Editor': ['Anthropology', 'Art (Choose One)', 'Bureaucracy', 'History',
               'Law', 'Occult', 'Persuade', 'HUMINT'],
    'Journalist': ['Anthropology', 'Art (Choose One)', 'Bureaucracy', 'History',
                   'Law', 'Occult', 'Persuade', 'HUMINT'],
    '"Black Bag" Training': ['Alertness', 'Craft (Choose One)', 'Craft (Electrician)',
                             'Craft (Locksmithing)', 'Criminology', 'Disguise',
                             'Search', 'Stealth'],
    'Blue-Collar Worker': ['Alertness', 'Craft (choose one)', 'Craft (choose another)',
                           'Drive', 'First Aid', 'Heavy Machinery', 'Navigate', 'Search'],
    'Bureaucrat': ['Accounting', 'Bureaucracy', 'Computer Science',
                   'Criminology', 'HUMINT', 'Law', 'Persuade', 'Personal Specialty'],
    'Clergy': ['Foreign Languages (choose three)', 'History',
               'HUMINT', 'Occult', 'Persuade', 'Psychotherapy'],
    'Combat Veteran': ['Alertness', 'Dodge', 'Firearms', 'First Aid',
                       'Heavy Weapons', 'Melee Weapons', 'Stealth', 'Unarmed Combat.'],
    'Computer Enthusiast': ['Computer Science', 'Craft (Microelectronics)', 'Science (Mathematics)',
                            'SIGINT', 'Personal Specialty'],
    'Hacker': ['Computer Science', 'Craft (Microelectronics)', 'Science (Mathematics)',
               'SIGINT', 'Personal Specialty'],
    'Counselor': ['Bureaucracy', 'First Aid', 'Foreign Language (choose one)',
                  'HUMINT', 'Law', 'Persuade', 'Psychotherapy', 'Search'],
    'Criminalist': ['Accounting', 'Bureaucracy', 'Computer Science',
                    'Criminology', 'Forensics', 'Law', 'Pharmacy', 'Search'],
    'Firefighter': ['Alertness', 'Demolitions', 'Drive', 'First Aid',
                    'Forensics', 'Heavy Machinery', 'Navigate', 'Search.'],
    'Gangster': ['Alertness', 'Criminology', 'Dodge', 'Drive', 'Persuade', 'Stealth',
                 'Athletics', 'Foreign Language', 'Firearms', 'HUMINT',
                 'Melee Weapons', 'Pharmacy', 'Unarmed Combat'],
    'Deep Cover': ['Alertness', 'Criminology', 'Dodge', 'Drive', 'Persuade', 'Stealth',
                   'Athletics', 'Foreign Language', 'Firearms', 'HUMINT',
                   'Melee Weapons', 'Pharmacy', 'Unarmed Combat'],
    'Interrogator': ['Criminology', 'Foreign Language (choose one)',
                     'Foreign Language (choose another)', 'HUMINT',
                     'Law', 'Persuade', 'Pharmacy', 'Search'],
    'Liberal Arts Degree': ['Anthropology or Archeology', 'Art (choose one)', 'Foreign Language (choose one)',
                            'History', 'Persuade', 'Personal Specialty'],
    'Military officer': ['Bureaucracy', 'Firearms', 'History', 'Military Science (choose one)',
                         'Navigate', 'Persuade', 'Unarmed Combat', 'Artillery',
                         'Heavy Machinery', 'Heavy Weapons', 'HUMINT', 'Pilot (choose one)', 'SIGINT'],
    'MBA': ['Accounting', 'Bureaucracy', 'HUMINT', 'Law', 'Persuade', 'Personal Specialty'],
    'Nurse': ['Alertness', 'First Aid', 'Medicine', 'Persuade', 'Pharmacy',
              'Psychotherapy', 'Science (Biology)', 'Search.'],
    'Paramedic': ['Alertness', 'First Aid', 'Medicine', 'Persuade', 'Pharmacy',
                  'Psychotherapy', 'Science (Biology)', 'Search.'],
    'Pre-Med': ['Alertness', 'First Aid', 'Medicine', 'Persuade', 'Pharmacy',
                'Psychotherapy', 'Science (Biology)', 'Search.'],
    'Occult Investigator': ['Anthropology', 'Archeology', 'Computer Science', 'Criminology',
                            'History', 'Occult', 'Persuade', 'Search'],
    'Conspiracy Theorist': ['Anthropology', 'Archeology', 'Computer Science', 'Criminology',
                            'History', 'Occult', 'Persuade', 'Search'],
    'Outdoorsman': ['Alertness', 'Athletics', 'Firearms',
                    'Navigate', 'Ride', 'Search', 'Stealth', 'Survival.'],
    'Photographer': ['Alertness', 'Art (Photography)', 'Computer Science', 'Persuade',
                     'Search', 'Stealth', 'Personal Specialty'],
    'Pilot': ['Alertness', 'Craft (Mechanic)', 'First Aid', 'Foreign Language (choose one)', 'Navigate',
              'Pilot (choose one)', 'Survival', 'Swim'],
    'Sailor': ['Alertness', 'Craft (Mechanic)', 'First Aid', 'Foreign Language (choose one)', 'Navigate',
               'Pilot (choose one)', 'Survival', 'Swim'],
    'Police Officer': ['Alertness', 'Criminology', 'Drive', 'Firearms',
                       'HUMINT', 'Law', 'Melee Weapons', 'Unarmed Combat'],
    'Science Grad Student': ['Bureaucracy', 'Computer Use', 'Craft (choose one)', 'Foreign Language (choose one)',
                             'Science (choose one)',
                             'Science (choose another)', 'Science (choose another)', 'Accounting', 'Forensics', 'Law',
                             'Pharmacy'],
    'Social Worker': ['Bureaucracy', 'Criminology', 'Forensics', 'Foreign Language (choose one)',
                      'HUMINT', 'Law', 'Persuade', 'Search'],
    'Criminal Justice Degree': ['Bureaucracy', 'Criminology', 'Forensics', 'Foreign Language (choose one)',
                                'HUMINT', 'Law', 'Persuade', 'Search'],
    'Soldier': ['Alertness', 'Artillery', 'Athletics', 'Drive', 'Firearms',
                'Heavy Weapons', 'Military Science (Land)', 'Unarmed Combat'],
    'Marine': ['Alertness', 'Artillery', 'Athletics', 'Drive', 'Firearms',
               'Heavy Weapons', 'Military Science (Land)', 'Unarmed Combat'],
    'Translator': ['Anthropology', 'Foreign Language (choose one)', 'Foreign Language (choose another)',
                   'Foreign Language (choose another)',
                   'History', 'HUMINT', 'Persuade', 'Personal Specialty'],
    'Urban explorer': ['Alertness', 'Athletics', 'Craft (choose one)', 'Law',
                       'Navigate', 'Persuade', 'Search', 'Stealth']
}

bonds_dict = {
    'Bond 1': 'F9',
    'Bond 2': 'F10',
    'Bond 3': 'F11',
    'Bond 4': 'F12',
    'Bond 5': 'F13',
    'Bond 6': 'F114'
}

bonds_score_dict = {
    'Score 1': 'H9',
    'Score 2': 'H10',
    'Score 3': 'H11',
    'Score 4': 'H12',
    'Score 5': 'H13',
    'Score 6': 'H114'
}

skill_dict = {
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
    'Other Skill 1': 'G35',
    'Other Skill 2': 'G36',
    'Other Skill 3': 'G37',
    'Other Skill 4': 'G38',
    'Other Skill 5': 'G39',
    'Other Skill 6': 'G40'
}

default_skills = {
    'Accounting': '10',
    'Alertness': '20',
    'Anthropology': '0',
    'Archeology': '0',
    'Art': '0',
    'Artillery': '0',
    'Athletics': '30',
    'Bureaucracy': '10',
    'Computer Science': '0',
    'Craft': '0',
    'Criminology': '10',
    'Demolitions': '0',
    'Disguise': '10',
    'Dodge': '30',
    'Drive': '20',
    'Firearms': '20',
    'First Aid': '10',
    'Forensics': '0',
    'Heavy Machinery': '10',
    'Heavy Weapons': '0',
    'History': '10',
    'HUMINT': '10',
    'Law': '0',
    'Medicine': '0',
    'Melee Weapons': '30',
    'Military Science': '0',
    'Navigate': '10',
    'Occult': '10',
    'Persuade': '20',
    'Pharmacy': '0',
    'Pilot': '0',
    'Psychotherapy': '0',
    'Ride': '10',
    'Science': '0',
    'Search': '20',
    'SIGINT': '0',
    'Stealth': '10',
    'Surgery': '0',
    'Survival': '10',
    'Swim': '20',
    'Unarmed Combat': '40',
    'Unnatural': '0',
    'Other Skill 1': '0',
    'Other Skill 2': '0',
    'Other Skill 3': '0',
    'Other Skill 4': '0',
    'Other Skill 5': '0',
    'Other Skill 6': '0'
}

anthropologist_historian_skills = {
    'choices': [{
        'Archeology': '50',
        'Anthropology': '50'
    }],
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '40'
    },
    'prof_skills': {
        'Bureaucracy': '40',
        'History': '60',
        'Occult': '40',
        'Persuade': '40'
    },
    'choose_skills': {
        'Anthropology': '40',
        'Archeology': '40',
        'HUMINT': '50',
        'Navigate': '50',
        'Ride': '50',
        'Search': '60',
        'Survival': '50'
    }
}

computer_science_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Computer Science': '60',
        'Craft (Electrician)': '60',
        'Craft (Mechanic)': '40',
        'Craft (Microelectronics)': '40',
        'Science (Mathematics)': '40',
        'SIGINT': '40'
    },
    'choose_skills': {
        'Accounting': '50',
        'Bureaucracy': '50',
        'Craft': '40',
        'Foreign Language': '40',
        'Heavy Machinery': '50',
        'Law': '40',
        'Science': '40'
    }
}

federal_agent_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '50',
        'Bureaucracy': '40',
        'Criminology': '50',
        'Drive': '50',
        'Firearms': '50',
        'Forensics': '30',
        'HUMINT': '60',
        'Law': '30',
        'Persuade': '50',
        'Search': '50',
        'Unarmed Combat': '60'
    },
    'choose_skills': {
        'Accounting': '60',
        'Computer Science': '50',
        'Foreign Language': '50',
        'Heavy Weapons': '50',
        'Pharmacy': '50'
    }
}

criminal_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '50',
        'Criminology': '60',
        'Dodge': '40',
        'Drive': '50',
        'Firearms': '40',
        'Law': '40',
        'Melee Weapons': '40',
        'Persuade': '50',
        'Stealth': '50',
        'Unarmed Combat': '50'
    },
    'choose_skills': {
        'Craft (Locksmithing)': '40',
        'Demolitions': '40',
        'Disguise': '50',
        'Foreign Language (Choose One)': '40',
        'Forensics': '40',
        'HUMINT': '50',
        'Navigate': '50',
        'Occult': '50',
        'Pharmacy': '40'
    }
}

physician_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Bureaucracy': '50',
        'First Aid': '60',
        'Medicine': '60',
        'Persuade': '40',
        'Pharmacy': '50',
        'Science (Biology)': '60',
        'Search': '40'
    },
    'choose_skills': {
        'Forensics': '50',
        'Psychotherapy': '60',
        'Science (Choose One)': '50',
        'Surgery': '50'
    }
}

scientist_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Bureaucracy': '40',
        'Computer Science': '40',
        'Science (choose one)': '60',
        'Science (choose another)': '50',
        'Science (choose one more)': '50',
    },
    'choose_skills': {
        'Accounting': '60',
        'Craft (choose one)': '40',
        'Foreign Language (choose one)': '40',
        'Forensics': '40',
        'Law': '40',
        'Pharmacy': '40'
    }
}

special_operator_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '60',
        'Athletics': '60',
        'Demolitions': '40',
        'Firearms': '60',
        'Heavy Weapons': '50',
        'Melee Weapons': '50',
        'Military Science (Land)': '60',
        'Navigate': '50',
        'Stealth': '50',
        'Survival': '50',
        'Swim': '50',
        'Unarmed Combat': '60',
    },
    'choose_skills': {
    }
}

firefighter_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '50',
        'Athletics': '60',
        'Craft (Electrician)': '40',
        'Craft (Mechanic)': '40',
        'Demolitions': '50',
        'Drive': '50',
        'First Aid': '50',
        'Forensics': '40',
        'Heavy Machinery': '50',
        'Navigate': '50',
        'Search': '40',
    },
    'choose_skills': {
    }
}

foreign_service_officer_skills = {
    'choices': [
    ],
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '50',
        'Foreign Language (choose one more)': '40',
    },
    'prof_skills': {
        'Accounting': '50',
        'Anthropology': '40',
        'Bureaucracy': '60',
        'History': '40',
        'HUMINT': '50',
        'Law': '40',
        'Persuade': '50',
    },
    'choose_skills': {
    }
}

intelligence_analyst_skills = {
    'choices': [
    ],
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '50',
        'Foreign Language (choose one more)': '40',
    },
    'prof_skills': {
        'Anthropology': '40',
        'Bureaucracy': '50',
        'Computer Science': '40',
        'Criminology': '50',
        'History': '40',
        'HUMINT': '50',
        'SIGINT': '40',
    },
    'choose_skills': {
    }
}

lawyer_business_executive_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Accounting': '40',
        'Bureaucracy': '50',
        'HUMINT': '50',
        'Persuade': '40',
    },
    'choose_skills': {
        'Computer Science': '50',
        'Criminology': '60',
        'Foreign Language (choose one)': '50',
        'Law': '50',
        'Pharmacy': '50',
    }
}

intelligence_case_officer_skills = {
    'choices': [
    ],
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '40',
    },
    'prof_skills': {
        'Alertness': '50',
        'Bureaucracy': '40',
        'Criminology': '50',
        'Disguise': '50',
        'Drive': '40',
        'Firearms': '40',
        'HUMINT': '60',
        'Persuade': '60',
        'SIGINT': '40',
        'Stealth': '50',
        'Unarmed Combat': '50',
    },
    'choose_skills': {
    }
}

media_specialist_skills = {
    'choices': [{
        'Art (Creative Writing)': '60',
        'Art (Journalism)': '60',
        'Art (Poetry)': '60',
        'Art (Scriptwriting)': '60',
    }],
    'languages': {
    },
    'prof_skills': {
        'History': '40',
        'HUMINT': '40',
        'Persuade': '50',
    },
    'choose_skills': {
        'Anthropology': '40',
        'Archeology': '40',
        'Art (choose one)': '40',
        'Bureaucracy': '50',
        'Computer Science': '40',
        'Criminology': '50',
        'Foreign Language (choose one)': '40',
        'Law': '40',
        'Military Science (choose one)': '40',
        'Occult': '50',
        'Science (choose one)': '40',
    }
}

nurse_paramedic_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '40',
        'Bureaucracy': '40',
        'First Aid': '60',
        'HUMINT': '40',
        'Medicine': '40',
        'Persuade': '40',
        'Pharmacy': '40',
        'Science (Biology)': '40',
    },
    'choose_skills': {
        'Drive': '60',
        'Forensics': '40',
        'Navigate': '50',
        'Psychotherapy': '50',
        'Search': '60',
    }
}

pilot_sailor_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '60',
        'Bureaucracy': '30',
        'Craft (Electrician)': '40',
        'Craft (Mechanic)': '40',
        'Navigate': '50',
        'Pilot (choose one)': '60',
        'Science (Meteorology)': '40',
        'Swim': '40',
    },
    'choose_skills': {
        'Foreign Language (choose one)': '50',
        'Pilot (choose another one)': '50',
        'Heavy Weapons': '50',
        'Military Science (choose one)': '50',
    }
}

police_officer_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '60',
        'Bureaucracy': '40',
        'Criminology': '40',
        'Drive': '50',
        'Firearms': '40',
        'First Aid': '30',
        'HUMINT': '50',
        'Law': '30',
        'Melee Weapons': '50',
        'Navigate': '40',
        'Persuade': '40',
        'Search': '40',
        'Unarmed Combat': '60',
    },
    'choose_skills': {
        'Forensics': '50',
        'Heavy Machinery': '60',
        'Heavy Weapons': '50',
        'Ride': '60',
    }
}

program_manager_skills = {
    'choices': [
    ],
    'languages': {
        'Foreign Language (choose one)': '50'
    },
    'prof_skills': {
        'Accounting': '60',
        'Bureaucracy': '60',
        'Computer Science': '50',
        'History': '40',
        'Law': '40',
        'Persuade': '50'
    },
    'choose_skills': {
        'Anthropology': '30',
        'Art (choose one)': '30',
        'Craft (choose one)': '30',
        'Science (choose one)': '30'
    }
}

soldier_marine_skills = {
    'choices': [
    ],
    'languages': {
    },
    'prof_skills': {
        'Alertness': '50',
        'Athletics': '50',
        'Bureaucracy': '30',
        'Drive': '40',
        'Firearms': '40',
        'First Aid': '40',
        'Military Science (Land)': '40',
        'Navigate': '40',
        'Persuade': '30',
        'Unarmed Combat': '50',
    },
    'choose_skills': {
        'Artillery': '40',
        'Computer Science': '40',
        'Craft (choose one)': '40',
        'Demolitions': '40',
        'Foreign Language (choose one)': '40',
        'Heavy Machinery': '50',
        'Heavy Weapons': '40',
        'Search': '60',
        'SIGINT': '40',
        'Swim': '60',
    }
}

anthro_histo = {
    'prof_skill': anthropologist_historian_skills,
    'num_of_choices': 2,
    'bonds': 4,
    'rec_stat': 'INT'
}

comp_sci_hack = {
    'prof_skill': computer_science_skills,
    'num_of_choices': 4,
    'bonds': 3,
    'rec_stat': 'INT'
}

fed_agent = {
    'prof_skill': federal_agent_skills,
    'num_of_choices': 1,
    'bonds': 3,
    'rec_stat': 'CON, POW, CHA'
}

physician = {
    'prof_skill': physician_skills,
    'num_of_choices': 2,
    'bonds': 3,
    'rec_stat': 'INT, POW, CON'
}

scientist = {
    'prof_skill': scientist_skills,
    'num_of_choices': 3,
    'bonds': 4,
    'rec_stat': 'INT'
}

spec_op = {
    'prof_skill': special_operator_skills,
    'num_of_choices': 0,
    'bonds': 2,
    'rec_stat': 'STR, CON, POW'
}

criminal = {
    'prof_skill': criminal_skills,
    'num_of_choices': 2,
    'bonds': 4,
    'rec_stat': 'STR, DEX'
}

firefighter = {
    'prof_skill': firefighter_skills,
    'num_of_choices': 0,
    'bonds': 3,
    'rec_stat': 'STR, DEX, CON'
}

fso = {
    'prof_skill': foreign_service_officer_skills,
    'num_of_choices': 0,
    'bonds': 3,
    'rec_stat': 'INT, CHA'
}

intel_anal = {
    'prof_skill': intelligence_analyst_skills,
    'num_of_choices': 0,
    'bonds': 3,
    'rec_stat': 'INT'
}

law_exec = {
    'prof_skill': lawyer_business_executive_skills,
    'num_of_choices': 4,
    'bonds': 4,
    'rec_stat': 'INT, CHA'
}

ico = {
    'prof_skill': intelligence_case_officer_skills,
    'num_of_choices': 0,
    'bonds': 2,
    'rec_stat': 'INT, POW, CHA'
}

med_spec = {
    'prof_skill': media_specialist_skills,
    'num_of_choices': 5,
    'bonds': 4,
    'rec_stat': 'INT, CHA'
}

nurse_para = {
    'prof_skill': nurse_paramedic_skills,
    'num_of_choices': 2,
    'bonds': 4,
    'rec_stat': 'INT, POW, CHA'
}

pilo_sail = {
    'prof_skill': pilot_sailor_skills,
    'num_of_choices': 2,
    'bonds': 3,
    'rec_stat': 'DEX, INT'
}

police = {
    'prof_skill': police_officer_skills,
    'num_of_choices': 1,
    'bonds': 3,
    'rec_stat': 'STR, CON, POW'
}

prog_mana = {
    'prof_skill': program_manager_skills,
    'num_of_choices': 1,
    'bonds': 4,
    'rec_stat': 'INT, CHA'
}

soldier = {
    'prof_skill': soldier_marine_skills,
    'num_of_choices': 3,
    'bonds': 4,
    'rec_stat': 'STR, CON'
}

inventory = ['Glock 19 (Medium Pistol)', 'First Aid Kit', 'Self-Applying Tourniquet',
             'Hemostatic Gel', 'Clothes', 'Boxes of Ammunition', 'S&W Model 36 (Light Pistol)',
             'Extra Pistol Magazines', 'Flashlight', 'Folding Knife (Knife)', 'Basic Tools',
             'Doorstops', 'Chalk', 'Bottled Water', 'Energy Bars', 'Batteries', 'Sunscreen',
             'Antibacterial Gel', 'Dufflebag or Backpack']

list_of_motivations = ['Exploiting the unnatural', 'Recognition for achievements',
                       'Showing others how its done', 'Correcting past mistakes',
                       'Success despite obstacles', 'Proving my worth', 'Getting the job done',
                       'Living up to expectations', 'Doing a job no one else can do',
                       'Constant improvement', 'Conspiracy theorizing',
                       'Making sense of a past tragedy', 'The thrill of discovery',
                       'Exploration', 'Solving a particular mystery', 'Understanding the unnatural',
                       'Learning a groups secrets', 'Expanding human knowledge',
                       'Solving hard problems', 'Survival at all costs',
                       'Professionalism', 'Doing whats right', 'Following the law',
                       'Healing', 'Faith', 'Patriotism', 'Personal integrity', 'Atonement',
                       'Protect a bond', 'Protect my family', 'Protect my friends/colleagues',
                       'Protect an organization', 'Protect a community', 'Protect my country',
                       'Protect humanity', 'Protect innocents',
                       'Figuring out what people want to hear', 'Telling lies from the turth',
                       'Communication', 'Diplomacy', 'Family obligations',
                       'Knowing what makes people tick', 'We can fix this',
                       'Never letting a particular bond down', 'New romance',
                       'Recruiting new agents and friendlies', 'Investigating...',
                       'Revenge against...', 'Staying one step ahead of...', 'Stopping...',
                       'A beloved pet', 'Favorite academic pursuit', 'Favorite art form',
                       'Favorite hobby', 'Favorite bad habit', 'Finding true meaning',
                       'Home', 'Sports', 'Intimacy', 'Anything for a sense of control']

list_of_bonds = ['Spouse', 'Ex-Spouse', 'Son', 'Daughter',
                 'Parent', 'Grandparent', 'Best Friend',
                 'Coworker', 'Partner', 'Psychologist',
                 'Therapist', 'Spouse & Children', 'Parents',
                 'Siblings', 'Colleagues in an intense job',
                 'Church', 'Support Group', 'Survivors of a shared trauma',
                 'Brother', 'Sister']

list_of_employers = ['Federal Bureau of Investigation', 'Drug Enforcement Administration',
                     'Immigration & Customs Enforcement', 'U.S. Marshal',
                     'U.S. Army', 'U.S. Airforce', 'U.S. Navy', 'U.S. Marines',
                     'U.S. Special Operations Command', 'Central Intelligence Agency',
                     'Department of State', 'Centre for Disease Control', 'None']

list_of_professions = ['Anthropologist', 'Historian', 'Computer Scientist',
                       'Engineer', 'Federal Agent', 'Physician',
                       'Scientist', 'Special Operator', 'Criminal',
                       'Firefighter', 'Foreign Service Officer',
                       'Intelligence Analyst', 'Lawyer', 'Business Executive',
                       'Intelligence Case Officer', 'Media Specialist', 'Nurse',
                       'Paramedic', 'Police Officer', 'Pilot', 'Sailor',
                       'Program Manager', 'Soldier', 'Marine']

list_of_disorders = ['Amnesia', 'Depersonalization Disorder', 'Depression',
                     'Dissociative Identity Disorder', 'Fugues', 'Megalomania',
                     'Paranoia', 'Sleep Disorder']

stats = ['STR', 'CON', 'DEX', 'INT', 'POW', 'CHA']

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

historian_skills = {
    'choices': [{
        'Archeology': '50',
        'Anthropology': '50'
    }],
    'languages': {
        'Foreign Language (choose one)': '50',
        'Foreign Language (choose another)': '40'
    },
    'skills': {
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

engineer_skills = {
    'choices': [
    ],
    'languages': {
    },
    'skills': {
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
    'skills': {
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
    'skills': {
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
    'skills': {
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
    'skills': {
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
    'skills': {
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
    'skills': {
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
    'skills': {
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
    'skills': {
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

business_executive_skills = {
    'choices': [
    ],
    'languages': {
    },
    'skills': {
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
    'skills': {
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
    'skills': {
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

paramedic_skills = {
    'choices': [
    ],
    'languages': {
    },
    'skills': {
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

pilot_skills = {
    'choices': [
    ],
    'languages': {
    },
    'skills': {
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
    'skills': {
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
    'skills': {
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

soldier_skills = {
    'choices': [
    ],
    'languages': {
    },
    'skills': {
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

items = [
    'Glock 19 (Medium Pistol)', 'First Aid Kit', 'Self-Applying Tourniquet',
    'Hemostatic Gel', 'Clothes', 'Boxes of Ammunition', 'S&W Model 36 (Light Pistol)',
    'Extra Pistol Magazines', 'Flashlight', 'Folding Knife (Knife)', 'Basic Tools',
    'Doorstops', 'Chalk', 'Bottled Water', 'Energy Bars', 'Batteries', 'Sunscreen',
    'Antibacterial Gel', 'Dufflebag or Backpack'
]

motivations = [
    'Exploiting the unnatural', 'Recognition for achievements',
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
    'Home', 'Sports', 'Intimacy', 'Anything for a sense of control'
]

bonds = [
    'Spouse', 'Ex-Spouse', 'Son', 'Daughter',
    'Parent', 'Grandparent', 'Best Friend',
    'Coworker', 'Partner', 'Psychologist',
    'Therapist', 'Spouse & Children', 'Parents',
    'Siblings', 'Colleagues in an intense job',
    'Church', 'Support Group', 'Survivors of a shared trauma',
    'Brother', 'Sister'
]

employers = [
    'Federal Bureau of Investigation', 'Drug Enforcement Administration',
    'Immigration & Customs Enforcement', 'U.S. Marshal',
    'U.S. Army', 'U.S. Airforce', 'U.S. Navy', 'U.S. Marines',
    'U.S. Special Operations Command', 'Central Intelligence Agency',
    'Department of State', 'Centre for Disease Control', 'None'
]

disorders = [
    'Amnesia', 'Depersonalization Disorder', 'Depression',
    'Dissociative Identity Disorder', 'Fugues', 'Megalomania',
    'Paranoia', 'Sleep Disorder'
]

veterans = {
    'Extreme Violence': {
        'description': (
            'For experiencing extreme violence: '
            'Add +10% to your Agent’s Occult skill. Reduce SAN '
            'by 5. Subtract 3 from your Agent’s CHA and each '
            'Bond. Your Agent is Adapted to Violence.'
        ),
    },
    'Captivity or Imprisonment': {
        'description': (
            'Add +10% to your Agent’s Occult skill. Reduce SAN '
            'by 5. Subtract 3 from your Agent’s POW. Your Agent '
            'is Adapted to Helplessness.'
        )

    },
    'Hard Experience': {
        'description': (
            'Add +10% to your Agent’s Occult and +10% to any '
            'four skills other than Unnatural. This can bring skills '
            'higher than 80%. Reduce your Agent’s SAN by 5. '
            'Remove one Bond.'
        ),
    },
    'Things Man Was Not Meant To Know': {
        'description': (
            'Your Agent gains 10% in the Unnatural skill and adds '
            '+20% to Occult. Reduce your Agent’s SAN by their POW. '
            'Your Agent gains a new disorder caused by '
            'the Unnatural. Reset your Agent’s Breaking '
            'Point to their new SAN minus POW.'
        ),
    },
}

historian_description = (
    "You study humanity. You're concerned with the "
    'patterns that emerge over time, across land masses, '
    'cultures, and language groups. You might be a number- '
    'cruncher, a field worker trudging through the jungle, '
    'a consultant in a war zone, or a think-tank analyst '
    'sifting myth from history in studies of the Tcho-Tcho '
    'peoples. '
)
engineer_description = (
    'Computers and machinery are the backbone of '
    'modern industry. You are a craftsman with data or '
    'machinery, possibly for the government and most '
    'definitely for profit. However you use your skills, '
    'the overlap between information technology and '
    'awareness of the unnatural could make this the most '
    'dangerous job on the planet.'
)

federal_agent_description = (
    'Many Delta Green Agents are federal law enforcement '
    'officers, mostly from the FBI. Delta Green decided '
    'long ago that federal agents have the optimum balance '
    'of skills and mental stability needed to confront '
    'the unnatural.'
)

physician_description = (
    'Doctors are often the first to uncover signs of an unnatural '
    'incursion, and the most valuable investigators '
    'of its disastrous effects on humanity.'
)
scientist_description = (
    'You expand human knowledge in a field such as '
    'biology, physics, or chemistry. When certain forms of '
    "knowledge cause insanity and death, it's easy to conclude "
    'that some hypotheses should not be tested.'
)
special_operator_description = (
    'As part of a force like the U.S. Army Rangers, you '
    'volunteered for a more difficult path than other soldiers. '
    "You've spent years in the most grueling training "
    'on the planet, and now serve on the most dangerous '
    'missions around.'
)
criminal_description = (
    'So much is illegal that there are broad economies of crime. '
    'This profile fits a hardened militant or a traditional “black '
    'collar” criminal: pimp, burglar, extortionist, or thug. If you '
    'want a white-collar criminal, choose Computer Scientist or '
    'Business Executive and make very risky decisions.'
)

firefighter_description = (
    'Your job oscillates between the tedium of maintaining your '
    'gear, exhilaration when the alarm finally comes, and the '
    'work of investigating a scene after the smoke has cleared. If '
    "you're involved with Delta Green, you clearly stumbled into "
    'something worse than a house fire.'
)

foreign_service_officer_description = (
    'You travel to strange lands, meet interesting people, and '
    'try to get along with them. Odds are you work for the State '
    'Department, though USAID, the Commercial Service and '
    'the Foreign Agriculture Service also have FSOs. Either way, '
    "you've had every opportunity to learn exotic and deadly "
    'things; the kinds of things that qualify you for Delta Green '
    'clearance.'
)
intelligence_analyst_description = (
    'In the FBI, NSA and CIA, there are those who gather '
    'information and those who decide what it means. You '
    'take information from disparate sources—newspapers, '
    'websites, informants, ELINT, and the assets developed by '
    'Case Officers—and figure out what it means. In short, '
    'your job is the piecing together of unrelated knowledge, a '
    'dangerous endeavor in the world of Delta Green.'
)

business_executive_description = (
    'Your tools are a computer and smartphone. You might '
    'be moving millions of dollars, or bits of data, or both. '
    'Or you might be a prosecutor, a defense attorney, or '
    'judge.'
)

intelligence_case_officer_description = (
    'You recruit people to spy on their own countries for your '
    'agency, probably the CIA. Your job is to develop foreign '
    "intelligence sources ('assets'), communicate with them, "
    "and keep them under control, productive, and alive. It's "
    'a hard business because you must view everyone as a '
    'potential threat, liar, or tool to further your agenda. If your '
    'name came to the attention of Delta Green, congratulations; '
    "you are now someone else's asset."
)

media_specialist_description = (
    'You might be an author, an editor, a researcher for a '
    'company or any branch of the government, a blogger, '
    'a TV reporter, or a scholar of rare texts. With the '
    "unnatural, you've uncovered the story of a lifetime."
    # TODO: With the unnatural?
)

medicine_description = (
    'Medical professionals are on the front line when awful '
    "things happen. Is that what brought you to the group's "
    'attention?'
)

pilot_description = (
    'Air or sea, commercial or military, your duty is to keep your '
    'passengers alive and craft intact. This can lead to hard '
    'choices when your passengers put the vehicle in danger. Or '
    'are you a drone operator, flying a Predator from a thousand '
    'miles away? Either way, what op brought you to the attention '
    'of Delta Green?'
)

police_officer_description = (
    'You serve and protect. Police officers walk the beat in uniform. '
    'Deputy sheriffs answer to an elected law enforcer and '
    'have jurisdiction over an entire county. Detectives come in '
    'after the fact and put the pieces together.'
)

program_manager_description = (
    'You run an organization. Someone has to secure funding, move '
    "resources, and make connections—and that's you. You control "
    'a budget and are responsible for how your program is maintained '
    'and where the money goes. Organizations discover the '
    'most startling things in their pursuit of profit or the public good.'
)
military_description = (
    'Governments will always need boots on the ground and '
    'steady hands holding rifles. When war begins, civilization '
    'gets out of the way. With the social contract void, unnatural '
    "things creep in at the edges. There's a reason Delta Green "
    'began in the military.'
)

professions = {
    'Historian': {
        'description': historian_description,
        'number_of_choices': 2,
        'number_of_bonds': 4,
        'recommended_stats': 'INT',
        **historian_skills,
    },
    'Engineer': {
        'description': engineer_description,
        'number_of_choices': 4,
        'number_of_bonds': 3,
        'recommended_stats': 'INT',
        **engineer_skills,
    },
    'Federal Agent': {
        'description': federal_agent_description,
        'number_of_choices': 1,
        'number_of_bonds': 3,
        'recommended_stats': 'CON, POW, CHA',
        **federal_agent_skills,
    },
    'Physician': {
        'description': physician_description,
        'number_of_choices': 2,
        'number_of_bonds': 3,
        'recommended_stats': 'INT, POW, CON',
        **physician_skills,
    },
    'Scientist': {
        'description': scientist_description,
        'number_of_choices': 3,
        'number_of_bonds': 4,
        'recommended_stats': 'INT',
        **scientist_skills,
    },
    'Special Operator': {
        'description': special_operator_description,
        'number_of_choices': 0,
        'number_of_bonds': 2,
        'recommended_stats': 'STR, CON, POW',
        **special_operator_skills,
    },
    'Criminal': {
        'description': criminal_description,
        'number_of_choices': 2,
        'number_of_bonds': 4,
        'recommended_stats': 'STR, DEX',
        **criminal_skills,
    },
    'Firefighter': {
        'description': firefighter_description,
        'number_of_choices': 0,
        'number_of_bonds': 3,
        'recommended_stats': 'STR, DEX, CON',
        **firefighter_skills,
    },
    'Foreign Service Officer': {
        'description': foreign_service_officer_description,
        'number_of_choices': 0,
        'number_of_bonds': 3,
        'recommended_stats': 'INT, CHA',
        **foreign_service_officer_skills,
    },
    'Intelligence Analyst': {
        'description': intelligence_analyst_description,
        'number_of_choices': 0,
        'number_of_bonds': 3,
        'recommended_stats': 'INT',
        **intelligence_analyst_skills
    },
    'Business Executive': {
        'description': business_executive_description,
        'number_of_choices': 4,
        'number_of_bonds': 4,
        'recommended_stats': 'INT, CHA',
        **business_executive_skills,
    },
    'Intelligence Case Officer': {
        'description': intelligence_case_officer_description,
        'number_of_choices': 0,
        'number_of_bonds': 2,
        'recommended_stats': 'INT, POW, CHA',
        **intelligence_case_officer_skills,
    },
    'Media Specialist': {
        'description': media_specialist_description,
        'number_of_choices': 5,
        'number_of_bonds': 4,
        'recommended_stats': 'INT, CHA',
        **media_specialist_skills,
    },
    'Paramedic': {
        'description': medicine_description,
        'number_of_choices': 2,
        'number_of_bonds': 4,
        'recommended_stats': 'INT, POW, CHA',
        **paramedic_skills,
    },
    'Pilot': {
        'description': pilot_description,
        'number_of_choices': 2,
        'number_of_bonds': 3,
        'recommended_stats': 'DEX, INT',
        **pilot_skills,
    },
    'Police Officer': {
        'description': police_officer_description,
        'number_of_choices': 1,
        'number_of_bonds': 3,
        'recommended_stats': 'STR, CON, POW',
        **police_officer_skills,
    },
    'Program Manager': {
        'description': program_manager_description,
        'number_of_choices': 1,
        'number_of_bonds': 4,
        'recommended_stats': 'INT, CHA',
        **program_manager_skills,
    },
    'Soldier': {
        'description': military_description,
        'number_of_choices': 3,
        'number_of_bonds': 4,
        'recommended_stats': 'STR, CON',
        **soldier_skills,
    },
}

for profession, copy_of in (
        # TODO: Anthro and historian might not be the exact same
        ('Anthropologist', 'Historian'),
        ('Computer Scientist', 'Engineer'),
        ('Lawyer', 'Business Executive'),
        ('Nurse', 'Paramedic'),
        ('Sailor', 'Pilot'),
        ('Marine', 'Soldier')):
    professions[profession] = professions[copy_of]

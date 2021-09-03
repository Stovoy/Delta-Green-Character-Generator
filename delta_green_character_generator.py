import datetime
import random
import textwrap

from lib import data, util
from lib.cli import CLI
from lib.sheet import Sheet, Cell, Section


def merge_dicts_replace(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict2[key] = int(dict1[key])
            del dict1[key]
    dict2.update(dict1)
    return dict2


def merge_dicts(dict1, dict2):
    for key in dict2:
        if key in dict1:
            dict2[key] = int(dict2[key]) + int(dict1[key])
            del dict1[key]
    dict2.update(dict1)
    return dict2


def spend_bonus_points(list_of_skills):
    starting_points = 160
    spent_points = 20
    current_points = starting_points
    skills_dict = {}
    for item in list_of_skills:
        if item not in data.skill_dict.keys():
            skills_dict[item] = 0

    print_from_list(list_of_skills)
    print('\nPlease select a skill to put ' + str(spent_points) + ' points into.')
    while current_points > 0:
        print('You have ' + str(current_points) + ' remaining.')
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print('Please input at number.')
            continue

        choice -= 1

        if choice < len(list_of_skills):
            chosen_skill = list_of_skills[choice]
        else:
            print('Please input a smaller number.')
            continue

        if chosen_skill in skills_dict.keys():
            special_skill = skills_dict[chosen_skill] + spent_points
            if special_skill <= 80:
                skills_dict.update({chosen_skill: int(skills_dict[chosen_skill]) + spent_points})
                print('\nYour ' + chosen_skill + ' stat is: ' + str(skills_dict[chosen_skill]))
                current_points = current_points - spent_points
                continue
            if skills_dict[chosen_skill] > 80:
                print("Please choose a different skill. Can't exceed 80% right now.")
                continue

        stat_value = int(sheet[skill_dict[chosen_skill]].replace('%', ''))
        stat_value = stat_value + spent_points

        if stat_value <= 80:
            sheet[skill_dict[chosen_skill]] = str(stat_value) + '%'
            print('\nYour ' + chosen_skill + ' stat is: ' + str(stat_value))
            current_points = current_points - spent_points
            continue
        if stat_value > 80:
            print("\nPlease choose a different skill. Can't exceed 80% right now.")
            continue

    removal_list = []
    for key in skills_dict.keys():
        if skills_dict[key] == 0:
            removal_list.append(key)

    for item in removal_list:
        skills_dict.pop(item)

    return skills_dict


def print_from_list(input_list):
    i = 1
    for item in input_list:
        print(str(i) + '. ' + item)
        i += 1


def print_bonus_skills(skill_packages):
    i = 1
    for key in skill_packages.keys():
        print(str(i) + '. ' + key + ': \n' + ', '.join([str(elem) for elem in skill_packages[key]]) + '\n')
        i += 1


def print_skills(chosen_skills):
    i = 1
    for skill in chosen_skills:
        print(str(i) + '. ' + skill)
        i += 1


def set_bonus_skills(skill_packages):
    print('\nSelect a bonus skill package to put points into\n')
    print_bonus_skills(skill_packages)
    print('Please select a skill package by number:')
    while True:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print('Please enter a number')
            continue
        try:
            choice -= 1
            _ = list(skill_packages.keys())[choice]
        except IndexError:
            print('Please use a different number')
            continue
        break

    return list(skill_packages.keys())[choice]


def get_package_skills(skill_packages, choice):
    print(f"You've chosen {choice}")
    return skill_packages[choice]


def random_stat():
    return sum(sorted([random.randint(1, 6) for x in range(4)])[1:])


def set_stat_array():
    stat_array = []
    for loops in range(6):
        stat_array.append(random_stat())
    stat_array.sort(reverse=True)
    return stat_array


def compare_dicts_and_set_sheet_values(skill_dict, prof_dict):
    list_of_skills = []
    for key in skill_dict.keys():
        if key not in prof_dict.keys():
            list_of_skills.append(key)

        set_sheet_value(skill_dict, key, str(prof_dict[key]) + '%')


def set_sheet_value(dictionary, key, value):
    sheet[dictionary[key]] = value


def set_skills(skill_dict, prof_dict):
    iterator = 1
    cell_iterator = 35
    for key in prof_dict.keys():
        if key in skill_dict:
            set_sheet_value(skill_dict, key, str(prof_dict[key]) + '%')
        if key not in skill_dict:
            value = key
            key = 'Other Skill ' + str(iterator)
            cell_key = 'F' + str(cell_iterator)
            iterator += 1
            cell_iterator += 1
            self.sheet[cell_key] = value
            set_sheet_value(skill_dict, key, str(prof_dict[value]) + '%')

    cell_iterator += 1


def set_spent_points(amount):
    # TODO Remove this global and use a class variable instead
    global stat_points
    stat_points -= amount


def update_stat_list(choice):
    if choice in stat_list:
        stat_list.remove(choice)


def set_stat_value(stat_name, amount):
    if stat_name in stat_list:
        sheet[stat_dict[stat_name]] = amount
    if stat_name not in stat_list:
        choice = input('Please choose from: ' + str(stat_list) + '!\n')
        set_stat_value(choice, amount)


def print_listed_professions():
    i = 0
    while i < len(list_of_professions):
        print(str(i + 1) + '. ' + list_of_professions[i])
        i += 1


def confirm():
    print('\nAre you sure? Y/N')
    choice = input()
    if choice.lower() == 'y':
        return True
    elif choice.lower() == 'n':
        return False
    else:
        print('Please input Y or N')


def set_profession_stats(prof_choice):
    print('You have chosen: ' + prof_choice)


def point_buy(points):
    spent_points = get_spent_points(points)
    chosen_stat = get_chosen_stat(spent_points)
    set_stat_value(chosen_stat, spent_points)
    update_stat_list(chosen_stat)
    set_spent_points(int(spent_points))
    return int(spent_points)


def handle_point_buy(stat_points):
    current_points = stat_points
    while current_points > 0:
        points = point_buy(current_points)
        current_points -= points


def get_spent_points(points):
    print('You have ' + str(points) + ' points. How many would you like to spend?\n')
    while True:
        spent_points = input()
        try:
            spent_points = int(spent_points)
        except ValueError:
            print('Please input a number')
            continue

        if spent_points > 0 and (points - spent_points) >= 0:
            return spent_points
        else:
            print('Please try again')


def handle_stats_array():
    choices = (
        ('Well Rounded', [13, 13, 12, 12, 11, 11]),
        ('Focused', [15, 14, 12, 11, 10, 10]),
        ('Highly Focused', [17, 14, 12, 10, 10, 9]),
    )
    chosen_stats = self.ui.prompt_choice('Select from the following', [choice[0] for choice in choices])
    for choice in choices:
        if choice[0] == chosen_stats:
            self.stat_array = choice[1]

    self.set_stat_distribution()


def get_chosen_stat(points):
    print('What stat would you like to put ' + str(points) + ' into?\nPlease choose from ' + str(stat_list) + '\n')
    chosen_stat = input()
    return chosen_stat


def print_bonds(prof_name, prof_dict):
    print('\nAs a ' + prof_name + ' you have ' + str(prof_dict['number_of_bonds']) + ' bonds.')


class Generator:
    def __init__(self):
        self.sheet = Sheet()
        self.ui = CLI()
        self.stat_array = []
        self.stat_points = 72

        self.profession = None
        self.background = None
        self.veteran_status = None

    def run(self):
        self.step(1, 'Determine Stats', self.step_stats)
        self.step(2, 'Calculate Derived Attributes', self.step_derived_stats)
        self.step(3, 'Select Profession & Skills', self.step_profession_and_skills)
        self.step(4, 'Define Bonds', self.step_define_bonds)
        self.step(5, 'Finalizing Your Character', self.step_finalize)

    def step(self, index, name, fn):
        self.ui.display_step(index, name)
        fn()

    def step_stats(self):
        self.ui.prompt_choice_with_fns('Choose your stats', (
            ('Roll', self.set_random_stats),
            ('Point buy', lambda: handle_point_buy(stat_points)),
            ('Array', handle_stats_array),
        ))

    def set_random_stats(self):
        while True:
            self.stat_array = set_stat_array()
            print(f'Your stats are {self.stat_array} which totals {sum(self.stat_array)}')
            if self.ui.prompt_yes_no('Are you satisfied with these stats?'):
                break
        self.set_stat_distribution()

    def set_stat_distribution(self):
        stat_list = data.stats

        while self.stat_array:
            value = self.stat_array.pop(0)
            stat_choice = self.ui.prompt_choice(f'Choose where to place {value} stat points', stat_list)
            self.ui.info(f'Placed {value} points into {stat_choice}')
            self.sheet[data.stat_dict[stat_choice]] = value
            stat_list.remove(stat_choice)

    def step_derived_stats(self):
        get_str_con = int(self.sheet['C8']) + int(self.sheet['C9'])
        divided_str_con = float(get_str_con / 2)
        multiplied_pow = int(self.sheet['C12'] * 5)
        get_san_pow = int(multiplied_pow - int(self.sheet['C12']))
        self.ui.info((textwrap.dedent(f"""
            This is handled by the sheet but we will double check.

            HP is equal to STR + CON ({get_str_con}) divided by 2 and rounded up ({round(divided_str_con)})
            WP is equal to POW ({self.sheet['C12']})
            SAN is equal to POW * 5 ({multiplied_pow})
            BP is equal to SAN - POW ({get_san_pow})""")))

        self.ui.prompt_continue()

    def step_profession_and_skills(self):
        while True:
            self.profession = self.ui.prompt_choice('Select your profession', list(data.professions.keys()))
            self.profession = {'name': self.profession, **data.professions[self.profession]}
            self.ui.info(f'You have chosen {self.profession}')
            skills_dict = self.confirm_profession()
            if skills_dict is not None:
                break
        master_skills = merge_dicts_replace(skills_dict, data.default_skills)
        set_skills(data.skill_dict, master_skills)
        self.background = set_bonus_skills(data.skill_packages)
        bonus_skills_dict = spend_bonus_points(get_package_skills(data.skill_packages, self.background))
        set_skills(data.skill_dict, bonus_skills_dict)

    def confirm_profession(self):
        self.ui.info(self.profession['description'])
        self.ui.prompt_continue()

        self.ui.info('Your professional skills:')
        self.ui.display_dict({k: f'{v}%' for k, v in self.profession['skills'].items()})
        self.ui.prompt_continue()

        if self.profession['number_of_choices'] == 0:
            self.ui.info(f"You can't choose any skills with this profession.")
        else:
            self.ui.info(f"You'll be able to choose {self.profession['number_of_choices']} skills from:")
            self.ui.display_dict({k: f'{v}%' for k, v in self.profession['choose_skills'].items()})
        self.ui.prompt_continue()

        self.ui.info(f"You'll have {self.profession['number_of_bonds']} bonds.")
        self.ui.info(f"This profession's recommended stats are {self.profession['recommended_stats']}")
        if self.ui.prompt_yes_no('Are you sure?'):
            return self.set_profession_skills()

    def set_profession_skills(self):
        result = {}

        for choices in self.profession['skills']['choices']:
            self.ui.display_list(list(choices.keys()))
            choice = self.ui.prompt_choice('Select a skill', choices)
            self.ui.info(f"You've chosen {choice}: {choices[choice]}")
            result.update({choice: choices[choice]})

        for language in list(self.profession['skills']['languages'].items()):
            choice = input(f'Please choose {language[0]}: ')
            self.ui.info(f"You've chosen {choice} {language[1]}")
            result.update({f'Foreign Language ({choice})': language[1]})

        for skill in self.profession['skills'].items():
            result.update({skill[0]: skill[1]})

        if self.profession['number_of_choices'] > 0:
            n = self.profession['number_of_choices']
            while n > 0:
                self.ui.info(f"You can select {n} more skills that you don't already have")
                # TODO: Display list with percentages?
                # TODO: Check that they don't already have them, remove them from the list,
                # TODO: Display which ones were removed (already had)
                # TODO: self.ui.info('You already have:')
                choice = self.ui.prompt_choice(
                    f"Please choose a skill from this list that you don't already have: ",
                    self.profession['skills']['choose_skills'].keys())
                result.update({choice: self.profession['skills']['choose_skills'][choice]})

        return result

    def step_define_bonds(self):
        self.get_bonds_choice()

    def get_bonds_choice(self):
        self.ui.info(f'As a {self.profession["name"]}, you have {self.profession["bonds"]} bonds.')
        self.ui.prompt_choice_with_fns(
            'Would you like to choose your bonds or create random bonds?', (
                ('Choose your bonds', self.choose_random_bonds),
                ('Random bonds', self.choose_bonds)
            ))

    def choose_bonds(self):
        key_iterator = 1
        score = self.sheet['C13']
        bond_choices = self.profession['number_of_bonds']
        while bond_choices > 0:
            self.ui.info(f'You have {bond_choices} bonds remaining.')
            choice = input('Please enter a bond name or bond type: ')
            bond_key = f'Bond {key_iterator}'
            score_key = f'Score {key_iterator}'
            set_sheet_value(data.bonds_dict, bond_key, choice)
            set_sheet_value(data.bonds_score_dict, score_key, score)
            key_iterator += 1
            bond_choices -= 1

    def choose_random_bonds(self):
        key_iterator = 1
        score = self.sheet['C13']
        bond_choices = self.profession['number_of_bonds']
        while bond_choices > 0:
            bond_key = f'Bond {key_iterator}'
            score_key = f'Score {key_iterator}'
            set_sheet_value(data.bonds_dict, bond_key, self.get_random_bond())
            set_sheet_value(data.bonds_score_dict, score_key, score)
            key_iterator += 1
            bond_choices -= 1

    def get_random_bond(self):
        return random.choice(data.bonds)

    def increase_n_skill_values(self, n, amount):
        for _ in range(n):
            choice = self.ui.prompt_choice(
                'Select a skill',
                data.default_skills)

            stat = util.percent_to_int(self.sheet.get_by_section(Section.Skills, choice))
            stat += amount
            self.sheet.set_by_section(Section.Skills, choice, self.int_to_percent(stat))

    def step_finalize(self):
        self.set_veteran_status()
        self.handle_finalizing()
        self.set_loadout()
        self.ui.info('Congratulations, you have finished character creation!')
        self.sheet.save()
        self.ui.info('Saved as output.xlsx')

    def set_veteran_status(self):
        while True:
            choice = self.ui.prompt_yes_no('Is your character a tramautized veteran?')
            if choice:
                veteran_status_name = self.ui.prompt_choice(
                    'What kind of trauma did you experience?', data.veterans.keys())
                self.veteran_status = data.veterans[veteran_status_name]
                self.veteran_status['name'] = veteran_status_name
                self.ui.info(choice['description'])
                if not self.ui.prompt_yes_no('Are you sure?'):
                    self.ui.info('Okay, select your veteran status again.')
                    continue
                else:
                    self.apply_veteran_status_effects()
                    break
            else:
                self.veteran_status = 'None'
                break

    def apply_veteran_status_effects(self):
        name = self.veteran_status['name']
        if name == 'Extreme Violence':
            occult = util.percent_to_int(self.sheet[Cell.Occult])
            self.sheet[Cell.Occult] = util.int_to_percent(occult + 10)
            # TODO what is SAN
            self.sheet['D18'] = self.sheet['C18'] - 5
            self.sheet[Cell.CHA] -= 3
            # TODO Bonds
        elif name == 'Captivity or Imprisonment':
            occult = util.percent_to_int(self.sheet[Cell.Occult])
            self.sheet[Cell.Occult] = util.int_to_percent(occult + 10)
            # TODO: This doesn't reduce SAN?
            self.sheet[Cell.POW] -= 3
        elif name == 'Hard Experience':
            occult = util.percent_to_int(self.sheet[Cell.Occult])
            self.sheet[Cell.Occult] = util.int_to_percent(occult + 10)
            self.sheet['D18'] = int(self.sheet['C18']) - 5
            self.increase_n_skill_values(4, 10)
            # TODO: Remove a bond?
        elif name == 'Things Man Was Not Meant To Know':
            # TODO: Should this set it to 10% or increase it by 10%?
            self.sheet.set_by_section(Section.Skills, 'Unnatural', '10%')
            occult = util.percent_to_int(self.sheet[Cell.Occult])
            self.sheet[Cell.Occult] = util.int_to_percent(occult + 20)
            # TODO: What the heck is going on here. What value is which?
            # self.sheet['D18'] = self.sheet['C18'] - self.sheet[Cell.POW]
            # self.sheet['D19'] = self.sheet['D18'] - self.sheet[Cell.POW]
            self.sheet[Cell.Disorder] = random.choice(data.disorders)

    def handle_finalizing(self):
        self.sheet[Cell.Profession] = self.profession['name']
        self.sheet[Cell.RealName] = self.ui.prompt_text("What's your character's real name?")
        self.sheet[Cell.Alias] = self.ui.prompt_text("What is your character's alias or code name?")
        self.sheet[Cell.School] = self.ui.prompt_text('Where did your character attend school?')
        self.ui.info('You will be given a series of random motivations for inspiration.')
        self.set_random_motivations()
        self.sheet[Cell.Employer] = self.ui.prompt_choice('Select an employer', data.employers)
        self.set_date_of_birth()
        self.set_bio()

    def set_loadout(self):
        self.ui.info('Do you want a default loadout? It includes:')
        self.ui.display_list(data.items)
        choice = self.ui.prompt_yes_no('Include the default loadout?')
        if not choice:
            return

        for index_iterator in range(11):
            key = f'J{index_iterator + 28}'
            self.sheet[key] = data.items[index_iterator]

        key_iterator = 28
        for index_iterator in range(11, len(data.items)):
            key = f'M{key_iterator}'
            self.sheet[key] = data.items[index_iterator]

        self.sheet['J3'] = 'Medium Pistol'
        self.sheet['J4'] = 'Light Pistol'
        self.sheet['J5'] = 'Knife'

    def set_random_motivations(self):
        for i, motivation in enumerate(random.sample(data.motivations, 5)):
            self.ui.info(f'Motivation {i + 1}: {motivation}')
            self.sheet.set_by_section(Section.Motivations, i, motivation)

    def set_employer(self):
        self.sheet[Cell.Employer] = self.ui.prompt_choice('Select an employer', data.employers)

    def set_date_of_birth(self):
        age = self.ui.prompt_int('Enter your age', 1, 150)
        self.sheet[Cell.Age] = age
        birth_time = (datetime.datetime.now() - age) - (
            datetime.timedelta(days=random.randint(0, 364))
        )
        birthday = f'{birth_time.month}/{birth_time.day}/{birth_time.year}'
        self.ui.info(f'Your date of birth is {birthday}.')
        self.sheet[Cell.Birthday] = birthday

    def set_bio(self):
        stat_str = int(self.sheet[Cell.STR])
        stat_con = int(self.sheet[Cell.CON])
        stat_dex = int(self.sheet[Cell.DEX])
        stat_int = int(self.sheet[Cell.INT])
        stat_pow = int(self.sheet[Cell.POW])
        stat_cha = int(self.sheet[Cell.CHA])

        parts = [
            'At a glance, people notice your ',
            (stat_str < 4, 'feeble and '),
            (stat_str < 9, 'weak body.'),
            (9 <= stat_str <= 12, 'completely forgettable, unremarkably-average build.'),
            (stat_str > 12, 'muscles are rippling'),
            (stat_str > 17, ' and huge.'),
            ' Your physical health ',
            (stat_con < 4, 'leaves you bedridden and '),
            (stat_con < 9, 'feels sickly.'),
            (9 <= stat_con <= 12,
             'meets the standards of an average adult. Heartbeat, breathing, most limbs, and all that.'),
            (stat_con > 12, 'is in perfect shape'),
            (stat_con > 17, ' and indefatigable.'),
            ' Your coordination is ',
            (stat_dex < 4, 'barely mobile and '),
            (stat_dex < 9, 'clumsy.'),
            (9 <= stat_dex <= 12,
             "on par with most folks your age. You probably shouldn't bend over too fast though."),
            (stat_dex > 12, 'nimble'),
            (stat_dex > 17, ' and acrobatic.'),
            " Your mind's thoughts are ",
            (stat_int < 4, 'imbecilic and '),
            (stat_int < 9, 'slow.'),
            (9 <= stat_int <= 12,
             "the result of public schooling. Y'know, average. Take +10% on Firearms if it's American "
             "schooling."),
            (stat_int > 12, 'perceptive'),
            (stat_int > 17, ' and brilliant.'),
            ' Your composure manifests as ',
            (stat_pow < 4, 'spineless and '),
            (stat_pow < 9, 'nervous.'),
            (9 <= stat_pow <= 12,
             "tempered and quite normal. You're not a leader of men but you're not a bitch."),
            (stat_pow > 12, 'strong-willed'),
            (stat_pow > 17, ' and indomitable.'),
            ' Your personality comes off as ',
            (stat_cha < 4, 'unbearable and '),
            (stat_cha < 9, 'awkward.'),
            (9 <= stat_cha <= 12, "normal. You don't stand out but you're not boring."),
            (stat_cha > 12, 'charming'),
            (stat_cha > 17, ' and magnetic.'),
            f' You spent some years working as a {self.background}.',
            f' After a while, you transitioned into becoming a {self.profession["name"]}. ',
            (self.veteran_status == 'None', (
                "Some time recently, you were contacted to join Delta Green. You're not a damaged veteran but "
                "don't be fueled, time in the field is measured in trauma, not hours.")),
            (self.veteran_status == 'Extreme Violence', (
                "You've experienced a lot of violence in the field. It doesn't phase you much. You're a bit "
                "abrasive now. Violence is always on the table when you're not bound by pesky morals.")),
            (self.veteran_status == 'Captivity or Imprisonment', (
                "You've spent some time in a cell, alone with your thoughts. It's not so bad being confined. The "
                "narcissist in your head insists that you're the most interesting person to be around.")),
            (self.veteran_status == 'Hard Experience', (
                "You've had a rough experience that changed you for the better. A small part of your soul was the "
                'price you paid. Not like you had anything better to spend it on.')),
            (self.veteran_status == 'Things Man Was Not Meant To Know', (
                "You've experienced things that most normal people never do. You've seen the edges of reality. It "
                "could've been Eldritch, but it was probably LSD."))
        ]

        bio = ""
        for part in parts:
            if type(part) == tuple:
                if part[0]:
                    bio += part[1]
            else:
                bio += part[0]
        self.ui.info(f'Your bio is: {bio}')
        self.sheet[Cell.Bio] = bio


if __name__ == '__main__':
    generator = Generator()
    generator.run()

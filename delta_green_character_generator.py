import datetime
import random
import textwrap

from lib import data, util
from lib.cli import CLI
from lib.sheet import Sheet, Cell, Section


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
            ('Point buy', lambda: self.handle_point_buy()),
            ('Array', self.handle_stats_array),
        ))

    def set_random_stats(self):
        while True:
            self.stat_array = self.random_stat_array()
            print(f'Your stats are {self.stat_array} which totals {sum(self.stat_array)}')
            if self.ui.prompt_yes_no('Are you satisfied with these stats?'):
                break
        self.set_stat_distribution()

    def set_stat_distribution(self):
        stat_list = data.stats

        while self.stat_array:
            value = self.stat_array.pop(0)
            choice = self.ui.prompt_choice(f'Choose where to place {value} stat points', stat_list)
            self.ui.info(f'Placed {value} points into {choice}')
            self.sheet.set_by_section(Section.Stats, choice, value)
            stat_list.remove(choice)

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
            skills = self.confirm_profession()
            if skills is not None:
                break
        self.set_skills({**skills, **data.default_skills})
        self.background = self.ui.prompt_choice(
            'Select a bonus skill package to put points into',
            list(data.skill_packages.keys()))
        self.set_skills(self.spend_bonus_points(data.skill_packages[self.background]))

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

        for choices in self.profession['choices']:
            self.ui.display_list(list(choices.keys()))
            choice = self.ui.prompt_choice('Select a skill', choices)
            self.ui.info(f"You've chosen {choice}: {choices[choice]}")
            result.update({choice: choices[choice]})

        for language in list(self.profession['languages'].items()):
            choice = self.ui.prompt_text(f'Choose {language[0]}:')
            self.ui.info(f"You've chosen: {choice} - {language[1]}%")
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
                    list(self.profession['choose_skills'].keys()))
                result.update({choice: self.profession['skills']['choose_skills'][choice]})

        return result

    def step_define_bonds(self):
        self.get_bonds_choice()

    def get_bonds_choice(self):
        self.ui.info(f'As a {self.profession["name"]}, you have {self.profession["bonds"]} bonds.')
        self.ui.prompt_choice_with_fns(
            'Would you like to choose your bonds or create random bonds?', (
                ('Choose your bonds',
                 lambda: self.choose_bonds(lambda: input('Please enter a bond name or bond type: '), interactive=True)),
                ('Random bonds', lambda: self.choose_bonds(lambda: random.choice(data.bonds))),
            ),
        )

    def choose_bonds(self, bond_getter, interactive=False):
        score = self.sheet[Cell.Score]
        bond_choices = self.profession['number_of_bonds']
        for i in range(1, self.profession['number_of_bonds'] + 1):
            if interactive:
                self.ui.info(f'You have {bond_choices} bonds remaining.')
            self.sheet.set_by_section(Section.Bonds, i, bond_getter())
            self.sheet.set_by_section(Section.BondScores, i, score)
            i += 1
            bond_choices -= 1

    def increase_n_skill_values(self, n, amount):
        for _ in range(n):
            choice = self.ui.prompt_choice(
                'Select a skill',
                data.default_skills)

            stat = util.percent_to_int(self.sheet.get_by_section(Section.Skills, choice))
            stat += amount
            self.sheet.set_by_section(Section.Skills, choice, util.int_to_percent(stat))

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
                    'What kind of trauma did you experience?', list(data.veterans.keys()))
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

    def spend_bonus_points(self, skills):
        # TODO: I messed something up here
        starting_points = 160
        points_to_spend = 20
        current_points = starting_points
        special_skills = {k: 0 for k in skills if k in Section.Skills.has(k)}
        while current_points > 0:
            self.ui.info(f'You have {current_points} remaining.')
            choice = self.ui.prompt_choice(f'Please select a skill to put {points_to_spend} points into.', skills)

            if choice in special_skills:
                special_skill = skills[choice] + points_to_spend
                if special_skill <= 80:
                    special_skills.update({choice: skills[choice] + points_to_spend})
                    self.ui.info(f'Your {choice} stat is: {special_skills[choice]}')
                    current_points -= points_to_spend
                else:
                    self.ui.info("Please choose a different skill. Can't exceed 80% right now.")
            else:
                stat_value = util.percent_to_int(self.sheet.get_by_section(Section.Skills, choice)) + points_to_spend

                if stat_value <= 80:
                    self.sheet.set_by_section(Section.Skills, choice, util.int_to_percent(stat_value))
                    self.ui.info(f'Your {choice} stat is: {stat_value}')
                    current_points -= points_to_spend
                else:
                    self.ui.info("Please choose a different skill. Can't exceed 80% right now.")

        return {k: v for k, v in special_skills.items() if v != 0}

    def random_stat(self):
        return sum(sorted([random.randint(1, 6) for _ in range(4)])[1:])

    def random_stat_array(self):
        stat_array = []
        for loops in range(6):
            stat_array.append(self.random_stat())
        stat_array.sort(reverse=True)
        return stat_array

    def compare_dicts_and_set_sheet_values(self, skill_dict, prof_dict):
        list_of_skills = []
        for key in skill_dict.keys():
            if key not in prof_dict.keys():
                list_of_skills.append(key)

            self.sheet[skill_dict[key]] = str(prof_dict[key]) + '%'

    def set_skills(self, skills):
        other_skill = 1
        for i, (skill, value) in enumerate(skills.items()):
            if Section.Skills.has(skill):
                self.sheet.set_by_section(Section.Skills, skill, util.int_to_percent(value))
            elif Section.OtherSkills.has(skill):
                self.sheet.set_by_section(Section.OtherSkills, skill, util.int_to_percent(value))
            else:
                print(i, skill, value, other_skill)
                skill = f'Other Skill {other_skill}'
                cell_key = f'F{other_skill + 34}'
                self.sheet[cell_key] = skill
                self.sheet.set_by_section(Section.OtherSkills, skill, util.int_to_percent(value))
                other_skill += 1

    def handle_point_buy(self):
        stat_list = data.stats[:]
        while self.stat_points > 0:
            spent_points = self.ui.prompt_int(
                f'You have {self.stat_points}. '
                f'How many would you like to spend?', 1,
                self.stat_points)
            choice = self.ui.prompt_choice(f'What stat would you like to put {spent_points} into?', stat_list)
            self.sheet.set_by_section(Section.Stats, choice, spent_points)
            stat_list.remove(choice)
            self.stat_points -= spent_points

    def handle_stats_array(self):
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


if __name__ == '__main__':
    generator = Generator()
    generator.run()

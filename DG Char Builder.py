import random
import openpyxl
from data import *
workbook = openpyxl.Workbook()
sheet = workbook.active


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
        if item not in skill_dict.keys():
            skills_dict[item] = 0

    print_from_list(list_of_skills)
    print("\nPlease select a skill to put " + str(spent_points) + " points into.")
    while current_points > 0:
        print("You have " + str(current_points) + " remaining.")
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Please input at number.")
            continue

        choice = choice - 1

        if choice < len(list_of_skills):
            chosen_skill = list_of_skills[choice]
        else:
            print("Please input a smaller number.")
            continue

        if chosen_skill in skills_dict.keys():
            special_skill = skills_dict[chosen_skill] + spent_points
            if special_skill <= 80:
                skills_dict.update({chosen_skill: int(skills_dict[chosen_skill]) + spent_points})
                print("\nYour " + chosen_skill + " stat is: " + str(skills_dict[chosen_skill]))
                current_points = current_points - spent_points
                continue
            if skills_dict[chosen_skill] > 80:
                print("Please choose a different skill. Can't exceed 80% right now.")
                continue

        stat_value = int(sheet[skill_dict[chosen_skill]].value.replace('%', ''))
        stat_value = stat_value + spent_points

        if stat_value <= 80:
            sheet[skill_dict[chosen_skill]] = str(stat_value) + "%"
            print("\nYour " + chosen_skill + " stat is: " + str(stat_value))
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
        print(str(i) + ". " + item)
        i += 1


def print_bonus_skills(skill_packages):
    i = 1
    for key in skill_packages.keys():
        print(str(i) + ". " + key + ': \n' + ', '.join([str(elem) for elem in skill_packages[key]]) + '\n')
        i += 1


def print_skills(chosen_skills):
    i = 1
    for skill in chosen_skills:
        print(str(i) + ". " + skill)
        i += 1


def set_bonus_skills(skill_packages):
    print("\nSelect a bonus skill package to put points into\n")
    print_bonus_skills(skill_packages)
    print("Please select a skill package by number:")
    while True:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number")
            continue
        try:
            choice -= 1
            _ = list(skill_packages.keys())[choice]
        except IndexError:
            print("Please use a different number")
            continue
        break

    return list(skill_packages.keys())[choice]


def get_package_skills(skill_packages, choice):
    print("You've chosen: " + choice)
    return skill_packages[choice]


def random_stat():
    return sum(sorted([random.randint(1, 6) for x in range(4)])[1:])


def set_skill_value(skill_dict, amount):
    iterator = 4
    skills = list(skill_dict.keys())
    while iterator > 0:
        print("Please select a skill:")
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Enter a number.")
            continue

        if choice < len(skills):
            choice = choice - 1
            chosen_skill = skills[choice]
            chosen_stat = skill_dict[chosen_skill]
            stat = int(sheet[chosen_stat].value.replace('%', ''))
            stat = stat + amount
            sheet[chosen_stat] = str(stat) + "%"
            iterator -= 1
            continue
        else:
            print("Please try again!")
            continue


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

        set_sheet_value(skill_dict, key, str(prof_dict[key]) + "%")


def set_sheet_value(dictionary, key, value):
    sheet[dictionary[key]] = value


def set_sheet_name(cell, value):
    sheet[cell] = value


def set_skills(skill_dict, prof_dict):
    iterator = 1
    cell_iterator = 35
    for key in prof_dict.keys():
        if key in skill_dict:
            set_sheet_value(skill_dict, key, str(prof_dict[key]) + '%')
        if key not in skill_dict:
            value = key
            key = 'Other Skill ' + str(iterator)
            cell_key = "F" + str(cell_iterator)
            iterator += 1
            cell_iterator += 1
            set_sheet_name(cell_key, value)
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
        choice = input("Please choose from: " + str(stat_list) + "!\n")
        set_stat_value(choice, amount)


def set_sheet_stat_value(stat_array):
    while True:
        choice = input("\nWhere would you like to place: " + str(stat_array[0]) + "?\n")
        try:
            choice = int(choice)
        except ValueError:
            print("Please input a number.")
            continue
        stat_index = choice - 1
        try:
            stat_choice = stat_list[stat_index]
            print(stat_choice)
        except IndexError:
            print("\nYour number isn't on the list. Try again")
            continue

        sheet[stat_dict[stat_choice]] = stat_array[0]
        update_stat_list(stat_choice)
        break


def set_stat_distribution(stat_array):
    while len(stat_array) > 0:
        print("\nPlease choose from the following:")
        i = 1
        for item in stat_list:
            print(str(i) + ". " + item)
            i += 1
        set_sheet_stat_value(stat_array)
        stat_array.pop(0)


def handle_random_stats():
    stat_array = set_stat_array()
    print('Your stats are: ' + str(stat_array) + " which totals " + str(sum(stat_array)))
    print('Are you satisfied? Y to continue, N to reroll\n')
    while True:
        choice = input()
        if choice.lower() == "y":
            set_stat_distribution(stat_array)
            break
        if choice.lower() == "n":
            return handle_random_stats()

    return stat_array


def print_listed_professions():
    i = 0
    while i < len(list_of_professions):
        print(str(i + 1) + ". " + list_of_professions[i])
        i += 1


def confirm():
    print("\nAre you sure? Y/N")
    choice = input()
    if choice.lower() == "y":
        return True
    elif choice.lower() == "n":
        return False
    else:
        print("Please input Y or N")


def print_profession_info(prof_skill, num_of_choices, bonds, rec_stat):
    iterator = 1
    print("\nYour professional skills:")
    for key in prof_skill["prof_skills"]:
        print(str(iterator) + ". " + key + ": " + prof_skill["prof_skills"][key] + "%")
        iterator += 1
    print("\nYou'll be able to choose " + str(num_of_choices) + " skills from:")
    iterator = 1
    for key in prof_skill["choose_skills"]:
        print(str(iterator) + ". " + key + ": " + prof_skill["choose_skills"][key] + "%")
        iterator += 1
    print("\nYou'll have " + str(bonds) + " bonds")
    print("\nThis profession's recommended stats are: " + rec_stat)


def confirm_selection(user_choice):
    if user_choice == "Anthropologist" or user_choice == "Historian":
        print('''\nDescription:\nYou study humanity. You’re concerned with the
patterns that emerge over time, across land masses,
cultures, and language groups. You might be a number-
cruncher, a field worker trudging through the jungle,
a consultant in a war zone, or a think-tank analyst
sifting myth from history in studies of the Tcho-Tcho
peoples.''')
        print_profession_info(**anthro_histo)
        if confirm():
            return set_profession_skills(**anthro_histo)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Computer Scientist" or user_choice == "Engineer":
        print('''Computers and machinery are the backbone of
modern industry. You are a craftsman with data or
machinery, possibly for the government and most
definitely for profit. However you use your skills,
the overlap between information technology and
awareness of the unnatural could make this the most
dangerous job on the planet.''')
        print_profession_info(**comp_sci_hack)
        if confirm():
            return set_profession_skills(**comp_sci_hack)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Federal Agent":
        print('''Many Delta Green Agents are federal law enforcement
officers, mostly from the FBI. Delta Green decided
long ago that federal agents have the optimum balance
of skills and mental stability needed to confront
the unnatural.''')
        print_profession_info(**fed_agent)
        if confirm():
            return set_profession_skills(**fed_agent)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Physician":
        print('''Doctors are often the first to uncover signs of an unnatural
incursion, and the most valuable investigators
of its disastrous effects on humanity.''')
        print_profession_info(**physician)
        if confirm():
            return set_profession_skills(**physician)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Scientist":
        print('''You expand human knowledge in a field such as
biology, physics, or chemistry. When certain forms of
knowledge cause insanity and death, it’s easy to conclude
that some hypotheses should not be tested.''')
        print_profession_info(**scientist)
        if confirm():
            return set_profession_skills(**scientist)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Special Operator":
        print('''As part of a force like the U.S. Army Rangers, you
volunteered for a more difficult path than other soldiers.
You’ve spent years in the most grueling training
on the planet, and now serve on the most dangerous
missions around.''')
        print_profession_info(**spec_op)
        if confirm():
            return set_profession_skills(**spec_op)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Criminal":
        print('''So much is illegal that there are broad economies of crime.
This profile fits a hardened militant or a traditional “black
collar” criminal: pimp, burglar, extortionist, or thug. If you
want a white-collar criminal, choose Computer Scientist or
Business Executive and make very risky decisions.''')
        print_profession_info(**criminal)
        if confirm():
            return set_profession_skills(**criminal)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Firefighter":
        print('''Your job oscillates between the tedium of maintaining your
gear, exhilaration when the alarm finally comes, and the
work of investigating a scene after the smoke has cleared. If
you’re involved with Delta Green, you clearly stumbled into
something worse than a house fire.''')
        print_profession_info(**firefighter)
        if confirm():
            return set_profession_skills(**firefighter)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Foreign Service Officer":
        print('''You travel to strange lands, meet interesting people, and
try to get along with them. Odds are you work for the State
Department, though USAID, the Commercial Service and
the Foreign Agriculture Service also have FSOs. Either way,
you’ve had every opportunity to learn exotic and deadly
things; the kinds of things that qualify you for Delta Green
clearance.''')
        print_profession_info(**fso)
        if confirm():
            return set_profession_skills(**fso)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Intelligence Analyst":
        print('''In the FBI, NSA and CIA, there are those who gather
information and those who decide what it means. You
take information from disparate sources—newspapers,
websites, informants, ELINT, and the assets developed by
Case Officers—and figure out what it means. In short,
your job is the piecing together of unrelated knowledge, a
dangerous endeavor in the world of Delta Green.''')
        print_profession_info(**intel_anal)
        if confirm():
            return set_profession_skills(**intel_anal)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Lawyer" or user_choice == "Business Executive":
        print('''Your tools are a computer and smartphone. You might
be moving millions of dollars, or bits of data, or both.
Or you might be a prosecutor, a defense attorney, or
judge.''')
        print_profession_info(**law_exec)
        if confirm():
            return set_profession_skills(**law_exec)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Intelligence Case Officer":
        print('''You recruit people to spy on their own countries for your
agency, probably the CIA. Your job is to develop foreign
intelligence sources (‘assets’), communicate with them,
and keep them under control, productive, and alive. It’s
a hard business because you must view everyone as a
potential threat, liar, or tool to further your agenda. If your
name came to the attention of Delta Green, congratulations;
you are now someone else’s asset.''')
        print_profession_info(**ico)
        if confirm():
            return set_profession_skills(**ico)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Media Specialist":
        print('''You might be an author, an editor, a researcher for a
company or any branch of the government, a blogger,
a TV reporter, or a scholar of rare texts. With the
unnatural, you’ve uncovered the stor y of a lifetime.''')
        print_profession_info(**med_spec)
        if confirm():
            return set_profession_skills(**med_spec)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Nurse" or user_choice == "Paramedic":
        print('''Medical professionals are on the front line when awful
things happen. Is that what brought you to the group’s
attention?''')
        print_profession_info(**nurse_para)
        if confirm():
            return set_profession_skills(**nurse_para)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Pilot" or user_choice == "Sailor":
        print('''Air or sea, commercial or military, your duty is to keep your
passengers alive and craft intact. This can lead to hard
choices when your passengers put the vehicle in danger. Or
are you a drone operator, flying a Predator from a thousand
miles away? Either way, what op brought you to the attention
of Delta Green?''')
        print_profession_info(**pilo_sail)
        if confirm():
            return set_profession_skills(**pilo_sail)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Police Officer":
        print('''You serve and protect. Police officers walk the beat in uniform.
Deputy sheriffs answer to an elected law enforcer and
have jurisdiction over an entire county. Detectives come in
after the fact and put the pieces together.''')
        print_profession_info(**police)
        if confirm():
            return set_profession_skills(**police)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Program Manager":
        print('''You run an organization. Someone has to secure funding, move
resources, and make connections—and that’s you. You control
a budget and are responsible for how your program is maintained
and where the money goes. Organizations discover the
most startling things in their pursuit of profit or the public good.''')
        print_profession_info(**prog_mana)
        if confirm():
            return set_profession_skills(**prog_mana)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))

    elif user_choice == "Soldier" or user_choice == "Marine":
        print('''Governments will always need boots on the ground and
steady hands holding rifles. When war begins, civilization
gets out of the way. With the social contract void, unnatural
things creep in at the edges. There’s a reason Delta Green
began in the military.''')
        print_profession_info(**soldier)
        if confirm():
            return set_profession_skills(**soldier)
        else:
            return confirm_selection(get_profession_selection(list_of_professions))


def get_profession_selection(prof_list):
    print_listed_professions()
    print("\nPlease select a profession by number:")
    while True:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a number")
            continue
        try:
            choice -= 1
            user_choice = prof_list[choice]
        except ValueError:
            print("Please use a different number")
            continue
        break

    print("\nYou have chosen: " + user_choice)
    return user_choice


def set_profession_stats(prof_choice):
    print("You have chosen: " + prof_choice)


def set_profession_skills(prof_skill, num_of_choices, **kwargs):
    dict_of_skill_assigns = {}
    skills_list = []
    iterator = 1

    for choices in prof_skill.get('choices'):
        list_of_choices = list(choices.keys())

        for item in list_of_choices:
            print(str(iterator) + ". " + item)
            iterator += 1
        while True:
            choice = input()
            try:
                choice = int(choice)
            except ValueError:
                print("Please input a number.")
                continue
            try:
                choice -= 1
                user_choice = list_of_choices[choice]
            except ValueError:
                print("Please try a different number.")
                continue

            if choice < len(list_of_choices):
                print("You've chosen " + user_choice + ": " + choices[user_choice])
                dict_of_skill_assigns.update({user_choice: choices[user_choice]})
                break
            else:
                print('Please enter the correct skill name.')

    iterator = 1

    for language in list(prof_skill['languages'].items()):
        print('Please choose ' + language[0])
        choice = input()
        print("You've chosen " + choice + " " + language[1])
        dict_of_skill_assigns.update({"Foreign Language (" + choice + ")": language[1]})

    for skill in prof_skill['prof_skills'].items():
        dict_of_skill_assigns.update({skill[0]: skill[1]})

    if num_of_choices > 0:
        print("Please choose " + str(num_of_choices) + " skills from this list that you don't already have: ")
        for skill in prof_skill['choose_skills'].items():
            skills_list.append(skill[0])
            print(str(iterator) + ". " + skill[0] + ": " + skill[1])
            iterator += 1

    while num_of_choices > 0:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Please input a number.")
            continue
        try:
            choice -= 1
            user_choice = skills_list[choice]
        except IndexError:
            print("Please try a different number.")
            continue

        if choice < len(skills_list):
            dict_of_skill_assigns.update({user_choice: prof_skill['choose_skills'][user_choice]})
            num_of_choices -= 1
            if num_of_choices == 0:
                break
            print("You chose " + user_choice + " please select " + str(num_of_choices) + " more.")

        else:
            print("Please enter the correct skill number.")

    print("\nUpdating values on character sheet, please wait...")
    return dict_of_skill_assigns


def reset_skills():
    print("Resetting stats...")
    sheet['C8'] = "12"
    sheet['C9'] = "12"
    sheet['C10'] = "12"
    sheet['C11'] = "12"
    sheet['C12'] = "12"
    sheet['C13'] = "12"

    print("Resetting skills...")
    set_skills(skill_dict, default_skills)
    skill_reset = 6
    cell_iterator = 35
    iterator = 1
    while skill_reset > 0:
        key = 'Other Skill ' + str(iterator)
        cell_key = "F" + str(cell_iterator)
        iterator += 1
        cell_iterator += 1
        skill_reset -= 1
        set_sheet_name(cell_key, key)
        set_sheet_value(skill_dict, key, default_skills[key] + '%')
    skill_reset = 5
    cell_iterator = 9

    print("Resetting bonds...")
    while skill_reset > 0:
        key = ''
        cell_key = "F" + str(cell_iterator)
        iterator += 1
        cell_iterator += 1
        skill_reset -= 1
        set_sheet_name(cell_key, key)
    skill_reset = 5
    cell_iterator = 9
    while skill_reset > 0:
        key = ''
        cell_key = "H" + str(cell_iterator)
        iterator += 1
        cell_iterator += 1
        skill_reset -= 1
        set_sheet_name(cell_key, key)

    print("Resetting name, age, profession, etc..")
    sheet['E1'] = "John Doe"
    sheet['B3'] = ''
    sheet['C4'] = 'None'
    sheet['C5'] = ''
    sheet['G5'] = ''
    sheet['H5'] = ''
    sheet['J40'] = ''
    sheet['D3'] = ' '
    sheet['D18'] = ' '
    sheet['D19'] = ' '
    sheet['J3'] = 'None'
    sheet['J4'] = 'None'
    sheet['J5'] = 'None'

    print("Resetting motivations...")
    key_iterator = 16
    i = 6
    while i > 0:
        key = ("E" + str(key_iterator))
        sheet[key] = ' '
        key_iterator += 1
        i -= 1

    print("Resetting inventory...")
    key_iterator = 28
    index_iterator = 0

    while index_iterator < 11:
        key = "J" + str(key_iterator)
        item = ' '
        key_iterator += 1
        index_iterator += 1
        sheet[key] = item
    key_iterator = 28
    while index_iterator < 22:
        key = "M" + str(key_iterator)
        item = ' '
        key_iterator += 1
        index_iterator += 1
        sheet[key] = item


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
    print("You have " + str(points) + " points. How many would you like to spend?\n")
    while True:
        spent_points = input()
        try:
            spent_points = int(spent_points)
        except ValueError:
            print("Please input a number")
            continue

        if spent_points > 0 and (points - spent_points) >= 0:
            return spent_points
        else:
            print("Please try again")


def handle_standard_array():
    print("\nPlease select from the following arrays:")
    print("1. Well Rounded: 13, 13, 12, 12, 11, 11")
    print("2. Focused: 15, 14, 12, 11, 10, 10")
    print("3. Highly Focused: 17, 14, 12, 10, 10, 9")
    print("This choice cannot be modified.")
    stat_array = []
    while not stat_array:
        choice = input()
        if choice == "1":
            stat_array = [13, 13, 12, 12, 11, 11]
        elif choice == "2":
            stat_array = [15, 14, 12, 11, 10, 10]
        elif choice == "3":
            stat_array = [17, 14, 12, 10, 10, 9]
        else:
            print('Invalid input. Try again.')
            continue
    set_stat_distribution(stat_array)


def get_chosen_stat(points):
    print("What stat would you like to put " + str(points) + " into?\nPlease choose from " + str(stat_list) + "\n")
    chosen_stat = input()
    return chosen_stat


def handle_derived_stats():
    get_str_con = int(sheet['C8'].value) + int(sheet['C9'].value)
    divided_str_con = float(get_str_con / 2)
    multiplied_pow = int(sheet['C12'].value * 5)
    get_san_pow = int(multiplied_pow - int(sheet['C12'].value))
    print("This is handled by the sheet but we will double check.")
    print("HP is equal to STR + CON (" + str(get_str_con) + ") divided by 2 (" + str(
        divided_str_con) + ") rounded up (" + str(round(divided_str_con)) + ") ")
    print("WP is equal to POW (" + str(sheet['C12'].value) + ") ")
    print("SAN is equal to POW x 5 (" + str(multiplied_pow) + ") ")
    print("BP is equal to SAN - POW (" + str(get_san_pow) + ") ")


def handle_statistics():
    options = [1, 2, 3, 4]
    while True:
        choice = input("Choose an option:\n1.Roll\n2.Point buy\n3.Array\n4.Reset Sheet\n")
        try:
            choice = int(choice)
        except ValueError:
            print("Please input a number.")
            continue

        if choice in options:
            if choice == 1:
                handle_random_stats()
            elif choice == 2:
                handle_point_buy(stat_points)
            elif choice == 3:
                handle_standard_array()
            elif choice == 4:
                reset_skills()
                quit()
            break

        if choice not in options:
            print("Please input a number on the list")


def print_bonds(prof_name, prof_dict):
    print("\nAs a " + prof_name + " you have " + str(prof_dict['bonds']) + " bonds.")


def get_bonds_choice(user_choice, prof_dict):
    print_bonds(user_choice, prof_dict)

    print("\nWould you like to choose your bonds or create random bonds?")
    print("1. Random")
    print("2. Chosen")
    while True:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Please input 1 or 2.")
            continue

        if choice == 1:
            print("\nYou have chosen to have random bonds.")
            set_bonds_random(prof_dict['bonds'])
            break
        elif choice == 2:
            print("\nYou have chosen to have chosen bonds.")
            set_bonds_chosen(prof_dict['bonds'])
            break
        else:
            print("Please input 1 or 2")


def get_random_bond():
    return random.choice(list_of_bonds)


def set_random_motivations():
    key_iterator = 16
    i = 5
    while i > 0:
        key = ("E" + str(key_iterator))
        sheet[key] = random.choice(list_of_motivations)
        key_iterator += 1
        i -= 1


def set_bonds_chosen(bonds):
    key_iterator = 1
    score = sheet['C13']
    while bonds > 0:
        print("\nYou have " + str(bonds) + " bonds remaining.")
        print("\nPlease enter a bond name or bond type:")
        choice = input()
        bond_key = ("Bond " + str(key_iterator))
        score_key = ("Score " + str(key_iterator))
        set_sheet_value(bonds_dict, bond_key, choice)
        set_sheet_value(bonds_score_dict, score_key, score)
        key_iterator += 1
        bonds -= 1


def set_bonds_random(bonds):
    key_iterator = 1
    score = sheet['C13'].value
    while bonds > 0:
        bond_key = ("Bond " + str(key_iterator))
        score_key = ("Score " + str(key_iterator))
        set_sheet_value(bonds_dict, bond_key, get_random_bond())
        set_sheet_value(bonds_score_dict, score_key, score)
        key_iterator += 1
        bonds -= 1


def handle_bonds(user_choice):
    if user_choice == "Anthropologist" or user_choice == "Historian":
        get_bonds_choice(user_choice, anthro_histo)
    elif user_choice == "Computer Scientist" or user_choice == "Engineer":
        get_bonds_choice(user_choice, comp_sci_hack)
    elif user_choice == "Federal Agent":
        get_bonds_choice(user_choice, fed_agent)
    elif user_choice == "Physician":
        get_bonds_choice(user_choice, physician)
    elif user_choice == "Scientist":
        get_bonds_choice(user_choice, scientist)
    elif user_choice == "Special Operator":
        get_bonds_choice(user_choice, spec_op)
    elif user_choice == "Criminal":
        get_bonds_choice(user_choice, criminal)
    elif user_choice == "Firefighter":
        get_bonds_choice(user_choice, firefighter)
    elif user_choice == "Foreign Service Officer":
        get_bonds_choice(user_choice, fso)
    elif user_choice == "Intelligence Analyst":
        get_bonds_choice(user_choice, intel_anal)
    elif user_choice == "Lawyer" or user_choice == "Business Executive":
        get_bonds_choice(user_choice, law_exec)
    elif user_choice == "Intelligence Case Officer":
        get_bonds_choice(user_choice, ico)
    elif user_choice == "Media Specialist":
        get_bonds_choice(user_choice, med_spec)
    elif user_choice == "Nurse" or user_choice == "Paramedic":
        get_bonds_choice(user_choice, nurse_para)
    elif user_choice == "Pilot" or user_choice == "Sailor":
        get_bonds_choice(user_choice, pilo_sail)
    elif user_choice == "Police Officer":
        get_bonds_choice(user_choice, police)
    elif user_choice == "Program Manager":
        get_bonds_choice(user_choice, prog_mana)
    elif user_choice == "Soldier" or user_choice == "Marine":
        get_bonds_choice(user_choice, soldier)


def set_employer():
    print("\nPlease select an employer from this list:")
    iterator = 1
    for item in list_of_employers:
        print(str(iterator) + ". " + item)
        iterator += 1
    while True:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Enter a number!")
            continue
        choice = choice - 1
        if choice < len(list_of_employers):
            sheet['C5'] = list_of_employers[choice]
            break
        else:
            print("Your choice was not on the list!")
            continue


def handle_loadout():
    print("\nDo you want a default loadout? It includes:")
    iterator = 1
    for item in inventory:
        print(str(iterator) + ". " + item)
        iterator += 1
    print("\nPlease input Y/N:")
    choice = input()
    key_iterator = 28
    index_iterator = 0

    if choice.lower() == "y":
        while index_iterator < 11:
            key = "J" + str(key_iterator)
            item = inventory[index_iterator]
            key_iterator += 1
            index_iterator += 1
            sheet[key] = item
        key_iterator = 28
        while index_iterator < len(inventory):
            key = "M" + str(key_iterator)
            item = inventory[index_iterator]
            key_iterator += 1
            index_iterator += 1
            sheet[key] = item

        sheet['J3'] = "Medium Pistol"
        sheet['J4'] = "Light Pistol"
        sheet['J5'] = "Knife"

    if choice.lower() == "n":
        print("Congratulations, you have finished character creation!")


def set_dob():
    choice = input("\nHow old are you? Birthday will be randomly generated.\n")
    sheet['G5'] = choice
    birthday = str(random.randrange(1, 13)) + "/" + str(random.randrange(1, 31)) + "/" + str(2021 - int(choice))
    sheet['H5'] = birthday
    return birthday


def set_bio(background, profession, veteran_status):
    stat_str = int(sheet['C8'].value)
    stat_con = int(sheet['C9'].value)
    stat_dex = int(sheet['C10'].value)
    stat_int = int(sheet['C11'].value)
    stat_pow = int(sheet['C12'].value)
    stat_cha = int(sheet['C13'].value)

    bio = "At a glance, people notice your "

    if stat_str < 4:
        bio = bio + "feeble and "
    elif stat_str < 8:
        bio = bio + "weak body."
    elif 9 <= stat_str <= 12:
        bio = bio + "completely forgettable, unremarkably-average build."
    elif stat_str > 12:
        bio = bio + "muscles are rippling"
    elif stat_str > 17:
        bio = bio + " and huge."

    bio = bio + " Your physical health "

    if stat_con < 4:
        bio = bio + "leaves you bedridden and "
    elif stat_con < 8:
        bio = bio + "feels sickly."
    elif 9 <= stat_con <= 12:
        bio = bio + "meets the standards of an average adult. Heartbeat, breathing, most limbs, and all that."
    elif stat_con > 12:
        bio = bio + "is in perfect shape"
    elif stat_con > 17:
        bio = bio + " and indefatigable."

    bio = bio + " Your coordination is "

    if stat_dex < 4:
        bio = bio + "barely mobile and "
    elif stat_dex < 8:
        bio = bio + "clumsy."
    elif 9 <= stat_dex <= 12:
        bio = bio + "on par with most folks your age. You probably shouldn't bend over too fast though."
    elif stat_dex > 12:
        bio = bio + "nimble"
    elif stat_dex > 17:
        bio = bio + " and acrobatic."

    bio = bio + " Your mind's thoughts are "

    if stat_int < 4:
        bio = bio + "imbecilic and "
    elif stat_int < 8:
        bio = bio + "slow."
    elif 9 <= stat_int <= 12:
        bio = bio + "the result of public schooling. Y'know, average. Take +10% on Firearms if it's American schooling."
    elif stat_int > 12:
        bio = bio + "perceptive"
    elif stat_int > 17:
        bio = bio + " and brilliant."

    bio = bio + " Your composure manifests as "

    if stat_pow < 4:
        bio = bio + "spineless and "
    elif stat_pow < 8:
        bio = bio + "nervous."
    elif 9 <= stat_pow <= 12:
        bio = bio + "tempered and quite normal. You're not a leader of men but you're not a bitch."
    elif stat_pow > 12:
        bio = bio + "strong-willed"
    elif stat_pow > 17:
        bio = bio + " and indomitable."

    bio = bio + " Your personality comes off as "

    if stat_cha < 4:
        bio = bio + "unbearable and "
    elif stat_cha < 8:
        bio = bio + "awkward."
    elif 9 <= stat_cha <= 12:
        bio = bio + "normal. You don't stand out but you're not boring."
    elif stat_cha > 12:
        bio = bio + "charming"
    elif stat_cha > 17:
        bio = bio + " and magnetic."

    bio = bio + " You spent some years working as a " + background + "."
    bio = bio + " After a while, you transitioned into becoming a " + profession + "."

    if veteran_status == "None":
        bio = bio + "Some time recently, you were contacted to join Delta Green. You're not a damaged veteran but " \
                    "don't be fueled, time in the field is measured in trauma, not hours. "
    elif veteran_status == "Extreme Violence":
        bio = bio + "You've experienced a lot of violence in the field. It doesn't phase you much. You're a bit " \
                    "abrasive now. Violence is always on the table when you're not bound by pesky morals. "
    elif veteran_status == "Captivity or Imprisonment":
        bio = bio + "You've spent some time in a cell, alone with your thoughts. It's not so bad being confined. The " \
                    "narcissist in your head insists that you're the most interesting person to be around. "
    elif veteran_status == "Hard Experience":
        bio = bio + "You've had a rough experience that changed you for the better. A small part of your soul was the " \
                    "price you paid. Not like you had anything better to spend it on. "
    elif veteran_status == "Things Man Was Not Meant To Know":
        bio = bio + "You've experienced things that most normal people never do. You've seen the edges of reality. It " \
                    "could've been Eldritch, but it was probably LSD. "

    print("\nYour bio is:\n" + bio)
    return bio


def handle_finalizing(background, profession, veteran_status):
    sheet['C4'] = profession
    choice = input("\nWhat's your character's real name?\n")
    sheet['E1'] = choice
    choice = input("\nWhat is your character's alias or code name?\n")
    sheet['D3'] = choice
    choice = input("\nWhere did your character attend school?\n")
    sheet['B3'] = choice
    print("\nYou will be given a series of random motivations for inspiration.")
    set_random_motivations()
    set_employer()
    dob = set_dob()
    print("\nYour date of birth is: " + dob + " you may need to modify this a bit.\n")
    sheet['J40'] = set_bio(background, profession, veteran_status)


listOfVeterans = ['Extreme Violence', 'Captivity or Imprisonment',
                  'Hard Experience', 'Things Man Was Not Meant To Know']


def get_veteran_type():
    print("What kind of trauma did you experience?:")
    iterator = 1
    for item in listOfVeterans:
        print(str(iterator) + ". " + item)
        iterator += 1
    while True:
        choice = input()
        try:
            choice = int(choice)
        except ValueError:
            print("Enter a number!")
            continue
        choice = choice - 1
        if choice < len(listOfVeterans):
            trauma_choice = listOfVeterans[choice]
            return trauma_choice
        else:
            print("Your choice was not on the list!")
            continue


def handle_veteran_type(choice):
    if choice == "Extreme Violence":
        print('''\nFor experiencing extreme violence:
Add +10% to your Agent’s Occult skill. Reduce SAN
by 5. Subtract 3 from your Agent’s CHA and each
Bond. Your Agent is Adapted to Violence.''')
        if confirm():
            occult = int(sheet['E35'].value.replace('%', ''))
            sheet['E35'] = str(occult + 10) + "%"
            sheet['D18'] = int(sheet['C18'].value) - 5
            sheet['C13'] = int(sheet['C13'].value) - 3
            return choice
        else:
            handle_veteran_type(get_veteran_type())

    elif choice == "Captivity or Imprisonment":
        print('''\nAdd +10% to your Agent’s Occult skill. Reduce SAN
by 5. Subtract 3 from your Agent’s POW. Your Agent
is Adapted to Helplessness.''')
        if confirm():
            occult = int(sheet['E35'].value.replace('%', ''))
            sheet['E35'] = str(occult + 10) + "%"
            sheet['C12'] = int(sheet['C12'].value) - 3
            return choice
        else:
            handle_veteran_type(get_veteran_type())

    elif choice == "Hard Experience":
        print('''\nAdd +10% to your Agent’s Occult and +10% to any
four skills other than Unnatural. This can bring skills
higher than 80%. Reduce your Agent’s SAN by 5.
Remove one Bond.''')
        if confirm():
            occult = int(sheet['E35'].value.replace('%', ''))
            sheet['E35'] = str(occult + 10) + "%"
            sheet['D18'] = int(sheet['C18'].value) - 5
            print_skills(default_skills.keys())
            set_skill_value(skill_dict, choice, 10)
            return choice
        else:
            handle_veteran_type(get_veteran_type())

    elif choice == "Things Man Was Not Meant To Know":
        print('''\nYour Agent gains 10% in the Unnatural skill and adds
+20% to Occult. Reduce your Agent’s SAN by his or
her POW. Your Agent gains a new disorder caused by
the Unnatural (see page 72). Reset your Agent’s Breaking
Point to his or her new SAN minus POW..''')
        if confirm():
            sheet['G33'] = "10%"
            occult = int(sheet['E35'].value.replace('%', ''))
            sheet['E35'] = str(occult + 20) + "%"
            sheet['D18'] = int(sheet['C18'].value) - int(sheet['C12'].value)
            sheet['D19'] = int(sheet['D18'].value) - int(sheet['C12'].value)
            set_random_disorder()
            return choice
        else:
            handle_veteran_type(get_veteran_type())


def set_random_disorder():
    sheet['E21'] = random.choice(list_of_disorders)


def get_veteran_status():
    print("\nIs your character a damaged veteran? Y/N")
    while True:
        choice = input()
        if choice.lower() == "y":
            user_choice = get_veteran_type()
            handle_veteran_type(user_choice)
            return user_choice
        if choice.lower() == "n":
            break
        else:
            print("Please select Y or N")
            continue


if __name__ == "__main__":
    print("\nStep 1: Determine Statistics")
    handle_statistics()

    print("\nStep 2: Calculate Derived Attributes")
    handle_derived_stats()

    print("\nStep 3: Select Profession & Skills")
    profession_selection = get_profession_selection(list_of_professions)
    prof_skills_dict = confirm_selection(profession_selection)
    master_skills = merge_dicts_replace(prof_skills_dict, default_skills)
    set_skills(skill_dict, master_skills)
    background_selection = set_bonus_skills(skill_packages)
    bonus_skills_dict = spend_bonus_points(get_package_skills(skill_packages, background_selection))
    set_skills(skill_dict, bonus_skills_dict)

    print("\nStep 4: Define Bonds")
    handle_bonds(profession_selection)

    print("\nStep 5: Finalizing Your Character")
    veteran_status = get_veteran_status()
    handle_finalizing(background_selection, profession_selection, veteran_status)
    handle_loadout()
    workbook.save("output.xlsx")
    print("Saved as output.xlsx")

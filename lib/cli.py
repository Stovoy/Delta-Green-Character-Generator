class UX:
    def display_step(self, index, name):
        raise NotImplemented


class CLI(UX):
    def display_step(self, index, name):
        print()
        print(f'Step {index}: {name}')
        print()

    def display_dict(self, to_display):
        for i, (key, value) in enumerate(to_display.items()):
            print(f'  {i + 1}) {key}: {value}')
        print()

    def display_list(self, to_display):
        for i, item in enumerate(to_display):
            print(f'  {i + 1}) {item}')
        print()

    def prompt_text(self, prompt):
        return input(f'{prompt}\n')

    def prompt_int(self, prompt, min, max):
        valid_range = f'[{min}-{max}]'
        while True:
            try:
                choice = int(input(f'{prompt} {valid_range}: '))
            except ValueError:
                pass
            else:
                if min <= choice <= max:
                    return choice

            print()
            print(f'Invalid choice, choose from {valid_range}.')
            print()

    def prompt_choice(self, prompt, choices):
        valid_range = f'[1-{len(choices)}]'
        while True:
            print(f'{prompt}:')
            for i, choice in enumerate(choices):
                print(f'  {i + 1}) {choice}')

            choice = input(f'Choose {valid_range}: ')
            try:
                choice = int(choice)
            except ValueError:
                pass
            else:
                if 1 <= choice <= len(choices):
                    break

            print()
            print(f'Invalid choice, choose from {valid_range}.')
            print()
        print()
        return choices[choice - 1]

    def prompt_choice_with_fns(self, prompt, choices):
        selected_choice = self.prompt_choice(prompt, [choice[0] for choice in choices])
        for choice in choices:
            if choice[0] == selected_choice:
                choice[1]()
                return choice[0]

    def prompt_yes_no(self, prompt):
        while True:
            choice = input(f'{prompt} [y/n]: ').lower()
            if choice == 'y':
                print()
                return True
            elif choice == 'n':
                print()
                return False
            print('Please enter either y or n.')
            print()

    def prompt_continue(self):
        input('Press enter to continue...')
        print()

    def info(self, line):
        print(line)
        print()

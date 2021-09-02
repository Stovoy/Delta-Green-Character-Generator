class UX:
    def display_step(self, index, name):
        raise NotImplemented


class CLI(UX):
    def display_step(self, index, name):
        print(f'Step {index}: {name}')
        print()

    def prompt_choice(self, choices):
        print('Choose an option:')
        for i, choice in enumerate(choices):
            print(f'  {i + 1}) {choice[0]}')

        valid_range = f'[1-{len(choices)}]'
        while True:
            choice = input(f'Enter your choice {valid_range}: ')
            try:
                choice = int(choice)
            except ValueError:
                pass
            else:
                if 1 <= choice <= len(choices):
                    break
            print(f'Please enter a valid choice {valid_range}: ')
            print()
        choices[choice - 1][1]()

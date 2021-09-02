class UX:
    def display_step(self, index, name):
        raise NotImplemented


class CLI(UX):
    def display_step(self, index, name):
        print()
        print(f'Step {index}: {name}')
        print()

    def prompt_choice(self, prompt, choices):
        valid_range = f'[1-{len(choices)}]'
        while True:
            print(f'{prompt}:')
            for i, choice in enumerate(choices):
                print(f'  {i + 1}) {choice[0]}')

            choice = input(f'Choice {valid_range}: ')
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
        choices[choice - 1][1]()

    def prompt_yes_no(self, prompt, yes_fn, no_fn):
        while True:
            choice = input(f'{prompt} [y/n]: ').lower()
            if choice == "y":
                print()
                yes_fn()
                break
            elif choice == "n":
                print()
                no_fn()
                break
            print("Please enter either y or n.")
            print()

    def prompt_continue(self):
        input('Press enter to continue...')

    def info(self, line):
        print(line)
        print()

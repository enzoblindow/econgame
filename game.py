import logging
import click

from builder import Builder


class Game(object):
    def __init__(self, id):
        self.id = id
        self.active = True
        self.turn = 0
        self.money = 10
        self.builder = Builder(self)

    def end_turn(self):
        click.echo('Ending turn {}'.format(self.turn))
        self.builder.collect_return()
        self.turn += 1

    def print_game_state(self):
        click.echo('+----------------------------------------+')
        click.echo(' ECONGAME')
        click.echo(' ----------------------------------------')
        click.echo(' Turn: {}'.format(self.turn))
        click.echo(' Money: {}'.format(self.money))
        click.echo('+----------------------------------------+')
        click.echo(self.builder)


def run():
    game = Game(1)

    while game.active:
        click.clear()
        game.print_game_state()
        action = click.prompt('What do you want to do?\t\n* [B]uild\t\n* [E]nd Turn\t\n* [Q]uit game \n', type=str)

        if action.lower() == 'q':
            game.active = False
        elif action.lower() == 'e':
            game.end_turn()
        elif action.lower() == 'b':
            game.builder.build_menu()
        else:
            click.echo('Please provide a valid option. Moron!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    run()
    logging.info('Game ended.')


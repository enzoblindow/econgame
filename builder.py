import logging
import click


class Builder(object):
    def __init__(self, game):
        logging.getLogger('builder')
        self.game = game
        self.building_keys = {
            'f': Farm,
            'm': Mill,
            'b': Bakery,
        }
        self.buildings = dict()

    def build_menu(self):
        click.clear()
        self.game.print_game_state()
        action = click.prompt('What do you want to build?\t\n* [F]arm\t\n* [M]ill\t\n* [B]akery\n\t\n* [R]eturn\n', type=str)

        building = self.building_keys[action.lower()]

        if building.__cost__ > self.game.money:
            click.echo('You don\'t have enough money')
        else:
            l = self.buildings.get(building.__name__) or list()
            l.append(building())
            self.buildings.update({building.__name__: l})
            self.game.money -= building.__cost__

    def collect_return(self):
        print('Collecting moneyzzzz')
        for buildings in self.buildings.values():
            self.game.money += sum([r.__return__ for r in buildings])

    def __repr__(self):
        s = ''
        if self.buildings:
            for k, v in self.buildings.items():
                s += ' {}: {}\n'.format(k, len(v))
            s += '+----------------------------------------+'
        return s


class Building(object):
    __name__ = ''
    __cost__ = 0
    __return__ = 0

    def __init__(self):
        click.echo('{} created!'.format(self.__name__))


class Farm(Building):
    __name__ = 'Farm'
    __cost__ = 10
    __return__ = 1


class Mill(Building):
    __name__ = 'Mill'
    __cost__ = 25
    __return__ = 3


class Bakery(Building):
    __name__ = 'Bakery'
    __cost__ = 100
    __return__ = 7

import collections
import inspect
from collections.abc import Sequence


class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

    def __contains__(self, member):
        return member in self.__myTeam

    def __iter__(self):
        for x in self.__myTeam:
            print(x)


def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print(len(classmates))
    print(classmates.__contains__('Timo'))
    classmates.__iter__()
    print(isinstance(classmates, Teams))
    print(hasattr(classmates, '__len__'))


main()

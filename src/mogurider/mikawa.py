#!/usr/bin/env python3


class Mikawa(object):
    def __init__(self, sign, gender):
        self.sign = sign  # sign of zodiac
        self.gender = gender
        self.win_sign = False
        self.win_gender = False

    def sing(self):
        if self.win_sign and self.win_gender:  # win-win
            print('そうよ', end='')
        else:
            print('いいえ', end='')
        print('私は{}の{}'.format(self.sign, self.gender))

    def ask_sign(self, sign):
        result = self.sign == sign
        self.win_sign = result
        return result

    def ask_gender(self, gender):
        result = self.gender == gender
        self.win_gender = result
        return result


if __name__ == '__main__':
    m = Mikawa('さそり座', '女')
    m.sing()

    m.ask_sign('さそり座')
    m.ask_gender('女')
    m.sing()

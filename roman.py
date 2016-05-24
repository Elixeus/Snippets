#!/usr/bin/env python


def parser(roman):
    '''
    This function receives a Roman Numeral String and convert it to an
    Arabic Number.

    parameters:
    ---------------------------------
    roman: Roman Numearl string input'''
    roman_dic = {'M': 1000, 'C': 100, 'L': 50, 'D': 500,
                 'X': 10, 'V': 5, 'I': 1}
    if roman:
        if not all(numeral in roman_dic for numeral in roman):
            print 'Illegal letter(s).'
        else:
            num_ls = [roman_dic.get(numeral, None) for numeral in roman]
            prev = num_ls[0]
            total = 0
            for val in num_ls:
                if val <= prev:
                    total += val
                    prev = val
                else:
                    total = total + val - (2 * prev)
                    prev = val
            return total
    else:
        print 'Empty String!'


def main():
    roman = raw_input('Input the Roman Numeral:\n')
    print '{roman} is {arabic}.'.format(roman=roman,
                                        arabic=parser(roman))


if __name__ == '__main__':
    main()

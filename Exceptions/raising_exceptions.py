import sys


def main():
    try:
        for line in readfile('text.bla'):
            print(line.strip())
    except ValueError as error:
        print('Something wrong: ', error)


def readfile(file_name):
    if file_name.endswith('.txt'):
        try:
            fh = open(file_name)
            return fh
        except IOError as error:
            print('Cannot open file: ' , error)
            sys.exit()
    else:
        raise ValueError('Filename must ends with .txt')


if __name__ == '__main__':
    main()

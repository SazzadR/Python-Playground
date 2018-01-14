import re


def main():
    fh = open('revan.txt')

    for line in fh.readlines():
        if re.search('(Len|Neverm)ore', line):
            updated_string = re.sub('(Len|Neverm)ore', '###', line)
            print(updated_string, end = '')


if __name__ == '__main__':
    main()

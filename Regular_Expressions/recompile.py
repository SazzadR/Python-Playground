import re


def main():
    fh = open('revan.txt')
    pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)

    for line in fh.readlines():
        if re.search(pattern, line):
            print(line, end = '')
            print(pattern.sub('###', line), end = '')


if __name__ == '__main__':
    main()

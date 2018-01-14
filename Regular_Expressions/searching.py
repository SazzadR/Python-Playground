import re;


def main():
    fh = open('revan.txt');

    for line in fh.readlines():
        found = re.search('(Len|Neverm)ore', line)
        if found:
            print(found.group())
            print(line, end = '')


if __name__ == '__main__':
    main()

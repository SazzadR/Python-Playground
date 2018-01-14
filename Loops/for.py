def main():
    fh = open('text.txt', 'r')
#     print(fh)
    
    for line in fh.readlines():
        print(line, end = '')


if __name__ == '__main__':
    main()

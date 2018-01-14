def main():
    string = 'This is a string!'
    
    # Enumeration can be used in place of (key, value) pair in for loop
    for key, value in enumerate(string):
        if value == 's':
            print('s found in {} place'.format(key))


if __name__ == '__main__':
    main()

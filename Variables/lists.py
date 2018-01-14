def main():
    tuple = (1, 2, 3)
    print(type(tuple), tuple)
    # Tuple is immutable object so can not be changed
    # tuple.insert( 4 )

    for x in tuple:
        print( x )

    print('----------')

    s = 'string'
    print(type(s), s)
    print(s[2 : 4])

if __name__ == '__main__':
    main()

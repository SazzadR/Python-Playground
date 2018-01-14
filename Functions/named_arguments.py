def main():
    test_function(one = 1, two = 2, three = 3)


def test_function(**kwargs):
    print(kwargs)  # This will act like a dictionary
    
    for key in kwargs:
        print(key, ': ', kwargs[key])


if __name__ == '__main__':
    main()

def main():
    dictionary = { 'one': 1, 'two': 2, 'three': 3 }
    print(dictionary)

    # Add new item to the dictionary
    dictionary.update({ 'four': 4 })

    for key in sorted(dictionary.keys()):
        print(key, dictionary[key])

if __name__ == '__main__':
    main()

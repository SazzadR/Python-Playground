class Duck():

    def __init__(self, **kwargs):
        self._variables = kwargs

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck')

    def set(self, key, value):
        self._variables[key] = value

    def get(self, key):
        return self._variables.get(key, None)


def main():
    donald = Duck(color = 'red')  # Pass arguments via constructor
    print(donald.get('color'))
    donald.set('color', 'white')  # Update the value via setter method
    print(donald.get('color'))


if __name__ == '__main__':
    main()

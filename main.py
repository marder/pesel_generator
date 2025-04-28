from pesel import Pesel


def main():

    person = Pesel('1999', '990201', 'M')
    print(person.generate_number())
    print(person.is_valid('99020151665', 'M'))  # False
    print(person.is_valid('99020151665', 'F'))  # True
    print(person.is_valid('99020139551', 'M'))  # True
    print(person.is_valid('99020139551', 'F'))  # False


if __name__ == '__main__':
    main()

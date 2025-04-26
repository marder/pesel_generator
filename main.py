from pesel import Pesel


def main():

    person = Pesel('1999', '990201', 'M')
    print(person.generate_number())
    print(person.is_valid('99020101899', 'M'))
    print(person.is_valid(person.generate_number(), 'F'))


if __name__ == '__main__':
    main()

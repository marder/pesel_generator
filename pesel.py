import datetime
import babel.dates
import random


class Pesel:

    def __init__(self, year: str, birthday: str, gender: str):

        self.year = year
        self.birthday = birthday
        self.gender = gender

        self.wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def generate_number(self) -> str:

        if self.gender == 'M':
            random_number = random.randrange(1, 9999, 2)
            gender_number = (4 - len(str(random_number))) * \
                '0' + str(random_number)

        if self.gender == 'F':
            random_number = random.randrange(0, 9998, 2)
            gender_number = (4 - len(str(random_number))) * \
                '0' + str(random_number)

        if self.year[0:2] == '19':
            generate_date = self.birthday

        if self.year[0:2] == '18':
            generate_date = self.birthday[0:2] + '8' + self.birthday[3:6]

        if self.year[0:2] == '20':
            generate_date = self.birthday[0:2] + '2' + self.birthday[3:6]

        if self.year[0:2] == '21':
            generate_date = self.birthday[0:2] + '4' + self.birthday[3:6]

        if self.year[0:2] == '22':
            generate_date = self.birthday[0:2] + '6' + self.birthday[3:6]

        full_number = generate_date + gender_number

        check_digit = (
            10 - (sum([int(i)*int(j) for i, j in zip(full_number, self.wages)]) % 10)) % 10

        pesel = full_number + str(check_digit)

        return pesel

    def is_valid(self, number: str, gender: str):

        if number[-2] in [0, 2, 4, 6, 8]:
            number_gender = 'F'
        else:
            number_gender = 'M'

        century = number[2]

        to_check = number[0:10]
        last_digit = number[10]

        check_digit = (
            10 - (sum([int(i)*int(j) for i, j in zip(to_check, self.wages)]) % 10)) % 10

        is_valid = False

        if last_digit == str(check_digit) and gender == number_gender:
            is_valid = True

        return is_valid
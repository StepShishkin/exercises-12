class Date:
    '''
    Class of date.

    Attributes
    ----------
    months (dict): The dictionary with number of month (key) and its name (value).
    date (str): A string with a date in the format "dd.mm.yyyy"..

    Parameters
    ----------
    date (str): Date entered by user.

    Prints
    ------
    Date if it is correct or None if it is not correct.
    '''

    def __init__(self, date: str):
        self._date = None
        self.__months = {
            1: 'янв', 2: 'фев', 3: 'мар', 4: 'апр', 5: 'май', 6: 'июн',
            7: 'июл', 8: 'авг', 9: 'сен', 10: 'окт', 11: 'ноя', 12: 'дек'
        }
        self.check_date(date)

    def check_date(self, date: str):
        """
        Checking the correctness of the date and initializing the _date attribute.

        Args:
            date (str): A string with a date in the format "dd.mm.yyyy".
        """

        try:
            day, month, year = map(int, date.split('.'))
            if 1 <= month <= 12 and 1 <= day <= 31:
                self._date = (day, month, year)
            else:
                print("Ошибка: некорректная дата")
        except ValueError:
            print("Ошибка: некорректный формат даты")

    @property
    def date(self):
        """
        Getting the date in the format 'dd month yyyy'.

        Returns:
            str: Date in the format 'dd month yyyy' or 'Error' if the date is incorrect.
        """
        if self._date:
            day, month, year = self._date
            return f"{day} {self.__months[month]} {year} г."
        else:
            return "Ошибка"

    @date.setter
    def date(self, date_str):
        """
        Setting a new date with verification of correctness.

        Args:
        date_str (str): New date in the format "dd.mm.y
        """
        self.check_date(date_str)

    def to_timestamp(self):
        """
        Calculates amount of seconds from '01.01.1970' to current date.
        result (int): Amount of seconds from '01.01.1970' to current date.
        """
        from datetime import datetime
        dt = datetime(self._date[2], self._date[1], self._date[0])
        return int(dt.timestamp())

    def __lt__(self, other):
        return self.to_timestamp() < other.to_timestamp()

    def __le__(self, other):
        return self.to_timestamp() <= other.to_timestamp()

    def __eq__(self, other):
        return self.to_timestamp() == other.to_timestamp()

    def __ne__(self, other):
        return self.to_timestamp() != other.to_timestamp()

    def __gt__(self, other):
        return self.to_timestamp() > other.to_timestamp()

    def __ge__(self, other):
        return self.to_timestamp() >= other.to_timestamp()


d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)
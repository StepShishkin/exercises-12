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
        self.data = date
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

    def __str__(self):
        if self._date:
            return self.data
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
class Load:
    '''
    Class of loading files.
    '''
    @staticmethod
    def write(file_1, file_2, file_3):
        '''
        Reads 3 files and uploading data from it.
        '''

        with open(file_1, 'r', encoding='UTF-8') as f:
            for line in [line.strip() for line in f.readlines()][1:]:
                id, date, title = line.split(';')[:-1]
                Meeting.lst_meeting.append(Meeting(int(id), Date(date), title))

        with open(file_2, 'r', encoding='UTF-8') as f:
            for line in [line.strip() for line in f.readlines()][1:]:
                id, nick_name, first_name, last_name, middle_name, gender = line.split(';')[:-1]
                User.lst_user.append(User(int(id), nick_name, first_name, last_name, middle_name, gender))

        with open(file_3, 'r', encoding='UTF-8') as f:
            for line in [line for line in f.readlines()][1:]:
                id_meet, id_pers = line.split(';')[:-1]
                for meet in Meeting.lst_meeting:
                    if meet.id == int(id_meet):
                        for user in User.lst_user:
                            if user.id == int(id_pers):
                                meet.employees.append(user)


class User:
    '''
    Class of users.

    Attributes
    ----------
    lst_users (list): List of users.
    '''
    lst_user = []
    lst_id = []

    def __init__(self, id=None, nick_name=None, first_name=None, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __str__(self):

        str_gender = ''
        str_id = ''
        str_nick = ''
        str_name = ''

        if self.id != '':
            str_id = f'ID: {self.id}'
        if self.nick_name != '':
            str_nick = f' Login: {self.nick_name}'
        if self.first_name != '' and self.last_name != '' and self.middle_name != '':
            str_name = f' NAME: {self.first_name} {self.last_name} {self.middle_name}'
        if self.first_name != '' and self.last_name != '' and self.middle_name == '':
            str_name = f' NAME: {self.first_name} {self.last_name}'
        if self.first_name != '' and self.last_name == '' and self.middle_name != '':
            str_name = f' NAME: {self.first_name} {self.middle_name}'
        if self.first_name == '' and self.last_name != '' and self.middle_name != '':
            str_name = f' NAME: {self.last_name} {self.middle_name}'
        if self.first_name != '' and self.last_name == '' and self.middle_name == '':
            str_name = f' NAME: {self.first_name}'
        if self.first_name == '' and self.last_name != '' and self.middle_name == '':
            str_name = f' NAME: {self.last_name}'
        if self.first_name == '' and self.last_name == '' and self.middle_name != '':
            str_name = f' NAME: {self.middle_name}'
        if self.gender != '':
            str_gender = f' GENDER: {self.gender}'
        info = str_id + str_nick + str_name + str_gender
        return info


class Meeting:
    '''
    Class of Meeting.

    Attributes
    ----------
    lst_meeting (list): List of meetings.

    Parameters
    ----------
    id (str): Meetings id.
    date (str): Meetings date.
    title (str): Meetings title.

    Prints
    ------
    Information about meetings in special form.
    '''

    lst_meeting = []

    def __init__(self, id, date, title):
        self.id = id
        self.date = date
        self.title = title
        self.employees = []

    def add_person(self, person):
        '''
        Adds a person to list of employees for meeting.
        '''

        self.employees.append(person)

    def count(self):
        '''
        Returns number of employees on meeting.
        '''

        return len(self.employees)

    @staticmethod
    def count_meeting(date):
        '''
        Returns number of meetings.
        '''

        count = 0
        for meet in Meeting.lst_meeting:
            if meet.date == date:
                count += 1

        return count

    @staticmethod
    def total():
        '''
        Returns number of all employees.
        '''

        count = 0
        for meet in Meeting.lst_meeting:
            count += len(meet.employees)

        return count

    def __repr__(self):
        result = ''

        result += f'Рабочая встреча {Meeting.lst_meeting.index(self) + 1}\n'
        result += f'{self.date} {self.title}\n'
        for employee in self.employees:
            result += f'{employee}'
            result += '\n'

        return result

Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))

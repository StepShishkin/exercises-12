class AirTicket:
    """
    Class for presenting airline tickets.

    Attributes:
        passenger_name (str): Passenger's name.
        from_location (str): The place of departure.
        to (str): The destination.
        date_time (str): The date and time of the flight.
        flight (str): Flight number.
        seat (str): The place number.
        class_type (str): Class (economy, business, etc.).
        gate (str): The gate number.
    """

    def __init__(self, passenger_name, _from, to, date_time, flight, seat, _class, gate):
        self.passenger_name = passenger_name
        self.from_location = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self.class_type = _class
        self.gate = gate

    def __str__(self):
        """
        Returns a string representation of an instance of the class.

        Returns:
            str: String representation of the ticket.
        """
        return (f'Passenger: {self.passenger_name}, From: {self.from_location}, To: {self.to}, Date: {self.date_time},'
                f'Flight: {self.flight}, Seat: {self.seat}, Class: {self.class_type}, Gate: {self.gate}')

class Load:
    """
    A class for downloading data from a file and creating a list of instances of the Air ticket class.

    Attributes:
        data (list): A list of instances of the Air ticket class.
    """
    def __init__(self):
        self.data = []

    def write(self, name_file):
        """
        Loads data from a file and creates a list of instances of the Air ticket class.

        Args:
            name_file (str): The name of the data file.
        """
        with open(name_file, 'r') as file:
            date = file.readline().split(';')
            for line in file:
                data_values = line.split(';')
                AirTicket(data_values[0], data_values[1], data_values[2], data_values[3],
                          data_values[4], data_values[5], data_values[6], data_values[7])
                len_indent = [16, 4, 3, 16, 20, 4, 3, 4]
                info = ''
                for _ in range(8):
                    info = info + '|' + data_values[_] + ' ' * (len_indent[_] - len(data_values[_]))
                self.data.append(info)


tickets = Load()
tickets.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in tickets.data:
    print(item)
print('-' * 79)




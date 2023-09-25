class Station:
    def __init__(self, name, line_number, weight=None):
        self.__name = name
        self.__line_number = line_number
        self.__weight = weight
        self.__transportation = {}

        self.__station_next = None
        self.__station_prev = None

    def get_name(self):
        return self.__name

    def get_line_number(self):
        return self.__line_number

    def get_weight(self):
        return self.__weight

    def get_next_station(self):
        return self.__station_next

    def get_prev_station(self):
        return self.__station_prev

    def set_next_station(self, station_next):
        self.__station_next = station_next

    def set_prev_station(self, station_prev):
        self.__station_prev = station_prev

    def set_transport_line(self, line_number, station):
        self.__transportation[line_number] = station

    def transport_to_other_line(self, line_number):
        return self.__transportation[line_number]

class SungdongMetroLines:
    def __init__(self):
        self.__line_2 = self.init_metro_line(2, ["왕십리"])
        self.__line_3 = self.init_metro_line(3, [])
        self.__line_5 = self.init_metro_line(5, [])
        # Gyeong-ui Jung-ang Line
        self.__line_G = self.init_metro_line("G", ["왕십리"])
        # Soo-in Boon-dang Line
        self.__line_S = self.init_metro_line("S", [])

        self.init_transport_stations()

    @staticmethod
    def init_metro_line(line_number, station_list):
        metro_line = {}
        # Define Station List
        for i, station_name in enumerate(station_list):
            metro_line[station_name] = Station(station_name, line_number)

        # Link Stations Each Other
        station_prev = None
        for i, station_name in enumerate(station_list):
            if i == 0:
                station_prev = metro_line[station_name]
            else:
                metro_line[station_name].set_prev_station(station_prev)
                station_prev = metro_line[station_name]

        station_next = None
        for i, station_name in enumerate(reversed(station_list)):
            if i == 0:
                station_next = metro_line[station_name]
            else:
                metro_line[station_name].set_next_station(station_next)
                station_next = metro_line[station_name]

        return metro_line

    def init_transport_stations(self):
        line_number_list = [2, 3, 5, "G", "S"]
        for i in range(len(line_number_list)):
            line_number_i = line_number_list[i]
            line_i = self.get_metro_line(line_number_i)
            for j in range(len(line_number_list)):
                line_number_j = line_number_list[j]
                line_j = self.get_metro_line(line_number_j)
                for station_i in line_i.values():
                    for station_j in line_j.values():
                        if station_i.get_name() == station_j.get_name():
                            station_i.set_transport_line(line_number_j, station_j)
                            station_j.set_transport_line(line_number_i, station_i)

    def get_metro_line(self, line_number):
        if line_number == 2:
            return self.__line_2

        elif line_number == 3:
            return self.__line_3

        elif line_number == 5:
            return self.__line_5

        elif line_number == "S":
            return self.__line_S

        elif line_number == "G":
            return self.__line_G

        else:
            raise Exception("Invalid Line Number")

    def get_route_time(self, node_start, node_goal):
        return 0

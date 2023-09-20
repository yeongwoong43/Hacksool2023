class Station:
    def __init__(self, num, name=None, weight=None):
        self.__name = name
        self.__num = num
        self.__weight = weight

        self.__station_next = []

    def get_name(self):
        return self.__name
    
    def get_num(self):
        return self.__num

    def get_line_number(self):
        return self.__line_number

    def get_weight(self):
        return self.__weight

    def get_next_stations(self):
        return self.__station_next

    def get_next_station_of_(self, next_station_name):
        return self.__station_next[next_station_name]

    def set_next_station(self, next_station):
        self.__station_next.append(next_station)
        return

class SungDongMetroLines:
	def __init__(self, metro_line):
		station_map = {
			0: [1],
			1: [0, 2, 7, 12, 10, 11],
			2: [1, 3],
			3: [2, 4],
			4: [3, 5],
			5: [13],
			6: [7, 8],
			7: [6, 1],
			8: [6],
			9: [10],
			10: [9, 1],
			11: [1, 14],
			12: [1],
			13: [],
			14: [],
		}
		self.metro_line = metro_line

		for station_num in station_map.keys():
			tmp = []
			for transport_num in station_map[station_num]:
				tmp.append(transport_num)
			metro_line.append(tmp)

	def get_metro_line(self):
		return self.metro_line
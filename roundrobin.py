class Process:
    def __init__(self, pid, arrival_time, burst_time, remaining_time, waiting_time, turnaround_time):
        self.__pid = pid # DECLARE pid : INTEGER 
        self.__arrival_time = arrival_time # DECLARE arrival_time : INTEGER 
        self.__burst_time = burst_time # DECLARE burst_time : INTEGER
        self.__remaining_time = remaining_time # DECLARE remaining_time : INTEGER
        self.__waiting_time = waiting_time # DECLARE waiting_time : INTEGER
        self.__turnaround_time = turnaround_time # DECLARE turnaround : INTEGER
        
    def Execute_Time_Slice(self, timeslice):
        self.__remaining_time -= timeslice
        return self.__waiting_time

    def Set_Completion_Time(self, current_time):
        self.__turnaround_time = current_time - self.__arrival_time
        self.__waiting_time = self.__turnaround_time - self.__burst_time
        return self.__waiting_time

class Round_Robin:
    def __init__(self, processes, time_slice):
        self.__processes = processes # DECLARE PROCESS : ARRAY[1:∞] OF Processes
        self.__time_slice = time_slice # DECLARE time_slice : INTEGER
        self.__current_time = 0 # DECLARE current_time : INTEGER


queue = [process(1, 0, 7), process(2, 2, 4), process(3, 4, 9), process(4, 6, 5), process(5, 8, 2)]


from collections import defaultdict
import math

def h_to_m(time):
    hh, mm = time.split(":")
    return int(hh)*60 + int(mm)

def solution(fees, records):
    answer = []

    car_records = defaultdict(list)
    car_numbers = []

    for i in records:
        time, car_number, status = i.split()
        car_numbers.append(car_number)
        car_records[car_number].append(time)
    car_numbers = list(set(car_numbers))
    car_numbers.sort()

    car_times = []
    car_records = dict(sorted(car_records.items()))

    for k, v in car_records.items():
        car_time = 0
        if(len(v)%2 == 1):
            v.append("23:59")
        for t in range(0,len(v)//2):
            car_time += h_to_m(v[2*t+1]) - h_to_m(v[2*t])
        car_times.append(car_time)

    for i in range(len(car_numbers)):
        if(car_times[i]<fees[0]):
            answer.append(fees[1])
        else:
            answer.append(fees[1]+math.ceil(((car_times[i]-fees[0])/fees[2]))*fees[3])

    return answer
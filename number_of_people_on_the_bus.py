def number(bus_stops):
    return sum([e[0] - e[1] for e in bus_stops])
    
print(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]))
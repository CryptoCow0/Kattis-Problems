import geometry
TestCases = int(input())
for x in range(TestCases):
        
    Xone,yone,xtwo,ytwo = map(int,input().split())

    HurricaneOne = geometry.Point(float(Xone), float(yone))

    HurricaneTwo = geometry.Point(float(xtwo), float(ytwo))

    AmountOfCities = int(input())

    CityLocations = []

    for x in range(AmountOfCities):
        Name,x,y = input().split()
        CityLocations.append((Name, geometry.Point(float(x),float(y))))

    distance = abs(CityLocations[0][1].distanceToLine(HurricaneOne,HurricaneTwo))
    cityToPrint = [CityLocations[0][0]]


    if AmountOfCities > 1:
        for city in CityLocations[1:]:
            dist = abs(city[1].distanceToLine(HurricaneOne,HurricaneTwo))

            if abs(distance - dist) < (1e-9):
                cityToPrint.append(city[0])
            elif dist < distance:
                distance = dist
                cityToPrint = [city[0]]

    print(" ".join(cityToPrint))



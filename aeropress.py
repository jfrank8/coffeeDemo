import ingredients
class aeropress:
    def __init__(self, filter):
        self.filter = filter

    def setFilter(self,filter):
        self.filter = filter
    def getFilter(self):
        return self.filter

def press(inWater, inBeans, inAeropress):
    #handle the origin
    if inBeans.getOrigin() == 'Kenya':
        topNote = 'fruit'
    else:
        topNote = 'chocolate'

    #handle the roast
    if inBeans.getRoast() == 'light':
        caffeine = 10
    else:
        caffeine = 6

    if inWater.getTemp() < 85:
        acidity = 'high'
    else:
        acidity = 'low'

    if inAeropress.getFilter() == 'paper':
        fines = 'low'
    else:
        fines = 'high'

    outCoffee = ingredients.coffee(caffeine, fines, topNote, acidity)
    return outCoffee

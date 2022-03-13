import ingredients
class aeropress:
    def __init__(self, filter):
        self.filter = filter

    def setFilter(self,filter):
        self.filter = filter
    def getFilter(self):
        return self.filter

def press(water, beans, aeropress):
    #handle the origin
    if beans.getOrigin() == 'Kenya':
        topNote = 'fruit'
    else:
        topNote = 'chocolate'

    #handle the roast
    if beans.getRoast() == 'light':
        caffeine = 10
    else:
        caffeine = 6

    if water.getTemp() < 85:
        acidity = 'high'
    else:
        acidity = 'low'

    if aeropress.getFilter() == 'paper':
        fines = 'low'
    else:
        fines = 'high'

    coffee = coffee(caffeine, fines, topNote, acidity)
    return coffee

class water:
    def __init__(self, temp):
        self.tempurature = name

    def setTemp(self, temp):
        self.tempurature = temp

    def getTemp(self):
        return self.tempurature

class beans():
    def __init__(self,origin,roast,grind = 0):
        self.origin = origin
        self.roast = roast
        self.grind = grind

    def getOrigin(self):
        return self.origin
    def getRoast(self):
        return self.roast
    def setGrind(self,grind):
        self.grind = grind%10
    def getGrind(self):
        return self.grind


class coffee():
    def __init__(self, caffine, fines, topNote, acidity):
        self.caffeine = caffine
        self.fines = fines
        self.topNote = topNote
        self.extraction = extraction


def grind(beans, grind):
    groundBeans = beans(beans.getOrigin(), beans.getRoast(), grind)
    return groundBeans

def heatWater(water,temp):
    heatedWater= water(temp%100)
    return heatedWater

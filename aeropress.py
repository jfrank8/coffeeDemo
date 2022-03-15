import coffeeDemo.ingredients
class aeropress:
    """
    A nifty way to brew coffee.

    ...

    Attributes
    ----------
    filter : str
        The type of filter to press the coffee through. Either metal or paper.

    """
    def __init__(self, filter):
        """constructor for aeropress.

        Parameters
        ----------
        filter : str
            The type of filter to press the coffee through. Either metal or paper.
        """
        self.filter = filter

    def setFilter(self,filter):
        """Setter for the aeropress's filter type.

        Parameters
        ----------
        filter : str
            The type of filter to press the coffee through. Either metal or paper.
        """
        self.filter = filter

    def getFilter(self):
        """Getter for the aeropress's filter type.

        Returns
        -------
        str
            The type of filter to press the coffee through. Either metal or paper.
        """
        return self.filter

def press(inWater, inBeans, inAeropress):
    """Brew coffee using the aeropress.

    This function clearly exhaustively models the mechanisms at action
    when brewing coffee with an aeropress.

    Parameters
    ----------
    inWater : coffeeDemo.ingredients.water
        The water to use to brew your coffee
    inBeans : coffeeDemo.ingredients.beans
        The ground coffee to brew.
    inAeropress: coffeeDemo.aeropress.aeropress
        The aeropress you wish to brew with

    Returns
    -------
    outCoffe : coffeeDemo.ingredients.coffee
        The coffee you have brewed

    """
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

    outCoffee = coffeeDemo.ingredients.coffee(caffeine, fines, topNote, acidity)
    return outCoffee

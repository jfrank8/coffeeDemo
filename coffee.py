import ingredients
import aeropress

def brew():
    myAeropress = aeropress.aeropress(filter = 'paper')
    myWater = ingredients.water(temp = 20)
    myBeans = ingredients.beans(origin = 'Kenya', roast = 'light', grind = 0);
    groundBeans = ingredients.grind(myBeans, grind='fine')
    hotWater = ingredients.heatWater(myWater,temp=100)
    myCoffee = aeropress.press(inWater = hotWater, inBeans = groundBeans, inAeropress = myAeropress)
    myCoffee.coffeePrint()

def main():
    brew()

if __name__ == '__main__':
    main()

import coffeeDemo.ingredients
import coffeeDemo.aeropress

def brew():
    myAeropress = coffeeDemo.aeropress.aeropress(filter = 'paper')
    myWater = coffeeDemo.ingredients.water(temp = 20)
    myBeans = coffeeDemo.ingredients.beans(origin = 'Kenya', roast = 'light', grind = 0);
    groundBeans = coffeeDemo.ingredients.grind(myBeans, grind='fine')
    hotWater = coffeeDemo.ingredients.heatWater(myWater,temp=100)
    myCoffee = coffeeDemo.aeropress.press(inWater = hotWater, inBeans = groundBeans, inAeropress = myAeropress)
    myCoffee.coffeePrint()

def main():
    brew()

if __name__ == '__main__':
    main()

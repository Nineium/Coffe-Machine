status = 'on'
resources = {
    "Water" : 2000,
    "Milk" : 1000,
    "Coffe" : 1000,
    "Money" : 100

}
prices = {
    "espresso" : 8,
    "latte" : 15,
    "cappuccino" : 15,
}

while status == 'on':
    prompt = input("What would you like (espresso/latte/cappuccino): ")
    money_insert = ""
    enough_resources = "Yes"
    if prompt == 'off':
        status = 'off'
    if prompt == "status":
        print (resources)
    if prompt == "espresso":
        money_insert = input("Insert "+ str(prices["espresso"]) + "$: ")
        int_money_insert = int(money_insert)
        if resources["Water"] < 30 and resources["Coffe"] < 18:
            enough_resources = "No"
            print("Sorry, there is not enough resources!")
        elif int_money_insert >= prices["espresso"] and enough_resources == "Yes":
            resources["Money"] += int_money_insert
            resources["Water"] = resources["Water"] - 30
            resources["Coffe"] = resources["Coffe"] - 18
            print("Here is your coffe, enjoy!")
            if int_money_insert > prices["espresso"]:
                change = int_money_insert - prices["espresso"]
                resources["Money"] = resources["Money"]- change
                print("Here is your change " +str(change)+ "$")
        elif int_money_insert < prices["espresso"]:
            print("Not enough money!")
    if prompt == "latte":
        money_insert = input("Insert " + str(prices["latte"]) + "$: ")
        int_money_insert = int(money_insert)
        if resources["Water"] < 200 and resources["Coffe"] < 30 and resources["Milk"] < 150:
            enough_resources = "No"
            print("Sorry, there is not enough resources!")
        elif int_money_insert >= prices["latte"] and enough_resources == "Yes":
            resources["Money"] += int_money_insert
            resources["Water"] = resources["Water"] - 200
            resources["Coffe"] = resources["Coffe"] - 30
            resources["Milk"] = resources["Milk"] - 150
            print("Here is your coffe, enjoy!")
            if int_money_insert > prices["latte"]:
                change = int_money_insert - prices["latte"]
                resources["Money"] = resources["Money"] - change
                print("Here is your change " + str(change) + "$")
        elif int_money_insert < prices["latte"]:
            print("Not enough money!")
    if prompt == "cappuccino":
        money_insert = input("Insert " + str(prices["cappuccino"]) + "$: ")
        int_money_insert = int(money_insert)
        if resources["Water"] < 100 and resources["Coffe"] < 20 and resources["Milk"] < 250:
            enough_resources = "No"
            print("Sorry, there is not enough resources!")
        elif int_money_insert >= prices["cappuccino"] and enough_resources == "Yes":
            resources["Money"] += int_money_insert
            resources["Water"] = resources["Water"] - 100
            resources["Coffe"] = resources["Coffe"] - 20
            resources["Milk"] = resources["Milk"] - 250
            print("Here is your coffe, enjoy!")
            if int_money_insert > prices["cappuccino"]:
                change = int_money_insert - prices["cappuccino"]
                resources["Money"] = resources["Money"] - change
                print("Here is your change " + str(change) + "$")
        elif int_money_insert < prices["cappuccino"]:
            print("Not enough money!")






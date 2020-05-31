while True:
    x = input("Which habitat # do you need?")
    if x!='exit':
        print(animals[int(x)])
    elif x == 'exit':
        print("See you!")
        break

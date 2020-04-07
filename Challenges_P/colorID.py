def colorID(color):
    print(color)
    print(type(color))

    
    if color == "red":
        return("#FF0000")

    elif color == "yellow":
         return("#FFFF00")

    elif color == "blue":
         return("#0000FF")

    else:
        return("the color you entered isn't supported yet")

colorID(5)
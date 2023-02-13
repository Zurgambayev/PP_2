def myFunction(**x):
    for k in x:
        print("product "  + k + ": " + x[k])
myFunction(name = "dep", price = "12%", dur = "3 m")
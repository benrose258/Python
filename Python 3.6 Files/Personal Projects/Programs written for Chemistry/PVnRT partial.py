def pvnrt():
    r = 0.08206
    find = input("What are you solving for? p, v, n, t> ")
    if find = "p":
        n = input("Number of moles of substance (n)> ")
        t = input("Temperature (in K)> ")
        v = input("Volume (V)> ")
        print("P = (nRT) / V")
        print("P = (" + str(n) + " * " + str(r) + " * " + str(t) + ") / "+str(v))
        return (n * r * t) / v
    
        

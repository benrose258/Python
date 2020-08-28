def CartesianProduct(setA,setB,setC):
    for numberOne in setA:
        for numberTwo in setB:
            for numberThree in setC:
                print (str(numberOne)+", "+str(numberTwo)+", "+str(numberThree))

CartesianProduct([0,1],[1,2],[0,1,2])

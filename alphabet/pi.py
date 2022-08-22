

import random

def CalcPi(n):

    in_circle=0
    in_square=0


    for i in range(n):
        x=random.uniform(0,1)
        y=random.uniform(0,1)


        if x**2+y**2 <= 1:
            in_circle+=1
        
        in_square+=1

        # print(in_circle, in_square)

    print(4*in_circle/in_square)





CalcPi(100000000)

# f=open("dataset1.csv", "w")
# f.write("NAME,LEG_LENGTH,DIET\n")
# f.write("Hadrosaurus,1.4,herbivore\n")
# f.write("Struthiomimus,0.72,omnivore\n")
# f.write("Velociraptor,1.8,carnivore\n")
# f.write("Triceratops,0.47,herbivore\n")
# f.write("Euoplocephalus,2.6,herbivore\n")
# f.write("Stegosaurus,1.50,herbivore\n")
# f.write("Tyrannosaurus Rex,6.5,carnivore\n")
# f.close()

# f=open("dataset2.csv", "w")
# f.write("NAME,STRIDE_LENGTH,STANCE\n")
# f.write("Euoplocephalus,1.97,quadrupedal\n")
# f.write("Stegosaurus,1.70,quadrupedal\n")
# f.write("Tyrannosaurus Rex,4.76,bipedal\n")
# f.write("Hadrosaurus,1.3,bipedal\n")
# f.write("Deinonychus,1.11,bipedal\n")
# f.write("Struthiomimus,1.24,bipedal\n")
# f.write("Velociraptor,2.62,bipedal\n")
# f.close()

# Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)

import math

GRAVITY=9.8

def calc_speed(stride, leg):
    return (stride/leg-1)*math.sqrt(leg*GRAVITY)


stride_length={}
leg_length={}
speedmap={}

f=open("/tmp/dataset2.csv", "r")
lines=f.readlines()
for i in range(1, len(lines)):
    dino,x,y=lines[i].strip().split(',')
    if y=='bipedal':
        stride_length[dino]=x

f=open("/tmp/dataset1.csv", "r")
lines=f.readlines()
for i in range(1, len(lines)):
    dino,x,y=lines[i].strip().split(',')
    if dino in stride_length:
        leg_length[dino]=x

for i in stride_length:
    if i in leg_length:
        speed=calc_speed(float(stride_length[i]), float(leg_length[i]))
        speedmap[i]=speed

print( [i for i, j in sorted(speedmap.items(), key=lambda kv: kv[1], reverse=True) ] )
    




f=open("dataset1.csv", "w")
f.write("NAME,LEG_LENGTH,DIET\n")
f.write("Hadrosaurus,1.4,herbivore\n")
f.write("Struthiomimus,0.72,omnivore\n")
f.write("Velociraptor,1.8,carnivore\n")
f.write("Triceratops,0.47,herbivore\n")
f.write("Euoplocephalus,2.6,herbivore\n")
f.write("Stegosaurus,1.50,herbivore\n")
f.write("Tyrannosaurus Rex,6.5,carnivore\n")
f.close()

f=open("dataset2.csv", "w")
f.write("NAME,STRIDE_LENGTH,STANCE\n")
f.write("Euoplocephalus,1.97,quadrupedal\n")
f.write("Stegosaurus,1.70,quadrupedal\n")
f.write("Tyrannosaurus Rex,4.76,bipedal\n")
f.write("Hadrosaurus,1.3,bipedal\n")
f.write("Deinonychus,1.11,bipedal\n")
f.write("Struthiomimus,1.24,bipedal\n")
f.write("Velociraptor,2.62,bipedal\n")
f.close()

# You will be supplied with two data files in CSV format .
# The first file contains statistics about various dinosaurs. The second file contains additional data.
# Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)

# Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
# Do not print any other information.

import math

G=9.8

stride_length={}
leg_length={}
speed_map={}

f=open("dataset2.csv", 'r')
lines=f.readlines()

for i in range(1,len(lines)):
  dino,stride,stance=lines[i].strip().split(',')
  if stance == "bipedal":
    stride_length[dino]=float(stride)

f=open("dataset1.csv", 'r')
lines=f.readlines()
for i in range(1,len(lines)):
  dino,leg,diet=lines[i].strip().split(',')
  if dino in stride_length:
    leg_length[dino]=float(leg)

for dino in stride_length:
  if dino in leg_length:
    speed_map[dino]=(stride_length[dino]/leg_length[dino]-1)*math.sqrt(leg_length[dino]*G)

print([sorted(speed_map.items(), key=lambda kv:kv[1], reverse=True)])






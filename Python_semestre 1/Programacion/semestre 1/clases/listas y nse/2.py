age = ()
name= ()
p1=()
namee = input('ingrese su nombre')
name+= (namee,)

while True:
  agee = int(input('ingrese su edad'))
  if agee<0 or agee>150:
     continue
  else:
     age +=(agee,)
     break 

p1 += (name[0],age[0])
print(p1)
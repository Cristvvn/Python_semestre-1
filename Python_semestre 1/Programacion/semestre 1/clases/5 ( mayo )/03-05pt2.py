name = ()
age = ()
p1 =()
namee = input('ingresa tu nombre: ')
name += (namee, )

while True:
    agee= int(input('ingresa tu edad: '))
    if agee<0 or agee>150:
         continue
    else:
         age+=(agee, )
         break
     
p1 += (age[0], name[0])
print (p1)
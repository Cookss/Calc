
vel = input("Type in the velocity: ")
acc = input("Type in acceleration: ")
time = input("Type in time: ")
x = input("Type in x: ")
xo = input("Type in xo: ")

if vel == '?':
    answer = vel
    answer = int(vel) / int(acc)
    print('Velocity: ')
    print(answer)


elif x == '?':
    answer = x
    answer = int(xo) + int(vel) * int(xo) * int(time) * int(.5) * int(acc) * int(time) ^ int(2)
    print('x: ')
    print(answer)





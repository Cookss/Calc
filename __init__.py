vel = input("Type in the velocity: ")
acc = input("Type in acceleration: ")
time = input("Type in time: ")

if vel == '?':
    answer = int(acc) / int(time)
    print('Velocity: ')
    print(answer)
    raise SystemExit

else:
    x = input("Type in x: ")
    xo = input("Type in xo: ")

if x == '?':
    answer1 = int(xo) + int(vel) * int(xo) * int(time) * int(.5) * int(acc) * int(time) ^ int(2)
    print('x: ')
    print(answer1)

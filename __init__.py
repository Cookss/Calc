vel = input("Type in the velocity: ")
speed = input("Type in speed: ")
time = input("Type in time: ")

if vel == '?':
    answer = int(speed) / int(time)
    vel = answer
    print('Velocity: ')
    print(answer)
    x = input("Type in x (displacement): ")
    xo = input("Type in xo (average displacement): ")

    if x == '?':
        answer1 = int(xo) + int(vel) * int(xo) * int(time) * int(.5) * int(speed) * int(time) ^ int(2)
        print('x: ')
        print(answer1)
        raise SystemExit


else:
    x = input("Type in x (displacement): ")
    xo = input("Type in xo (average displacement): ")

if x == '?':
    answer1 = int(xo) + int(vel) * int(xo) * int(time) * int(.5) * int(speed) * int(time) ^ int(2)
    print('x: ')
    print(answer1)

import numpy as np
import matplotlib.pyplot as plt

vel = input("Type in the velocity: ")
speed = input("Type in speed: ")
time = input("Type in time: ")
if time == '?':
    time = 1
vo = input("Type Vo: ")
if vo == '?':
    vo = 0
a = input("Type Acceleration: ")

if vel == '?':
    answer = int(speed) / int(time)
    vel = int(answer)
    print('Velocity: ')
    print(answer)
    if a == '?':
        a = int(vel) - int(vo)
        print("Speed: ")
        print(a)
    x = input("Type in x (displacement): ")
    xo = input("Type in xo (average displacement): ")
    if xo == '?':
        xo = 0
elif speed == '?':
    speed = int(vel) * int(time)
    print('Speed: ')
    print(speed)
    x = input("Type in x (displacement): ")
    xo = input("Type in xo (average displacement): ")
    if xo == '?':
        xo = 0
    a = int(vo) - int(vel) / int(time)
    print("Acceleration: ")
    print(a)

    if x == '?':
        answer1 = int(xo) + int(vel) * int(xo) * int(time) * int(.5) * int(speed) * int(time) ^ int(2)
        x = int(answer1)
        print('x: ')
        print(answer1)

        ten = np.linspace(int(xo), int(x), int(time))
        zen = np.linspace(int(xo), int(vo) * int(speed), int(x))
        plt.plot(zen, label="Object speed")
        plt.plot(ten, label="Object's displacement")
        plt.plot()

        plt.xlabel('Time')
        plt.ylabel('Destination')

        plt.title("Results")

        plt.legend()

        plt.show(block=True)
        plt.interactive(True)
        raise SystemExit

else:
    x = input("Type in x (displacement): ")
    xo = input("Type in xo (final displacement): ")
    if xo == '?':
        xo = 0

if x == '?':
    answer1 = int(xo) + int(vel) * int(xo) * int(time) * int(.5) * int(speed) * int(time) ^ int(2)
    print('x: ')
    print(answer1)

ten = np.linspace(int(xo), int(x), int(time))
zen = np.linspace(int(xo), int(vo) * int(speed), int(x))
plt.plot(zen, label="Object speed")
plt.plot(ten, label="Object's displacement")
plt.plot()

plt.xlabel('Time')
plt.ylabel('Destination')

plt.title("Results")

plt.legend()

plt.show(block=True)
plt.interactive(True)

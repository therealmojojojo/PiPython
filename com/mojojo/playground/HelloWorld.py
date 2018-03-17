print("Hello world")

lights = {"light1": 1, "light2": 0, "light3": 1}

for light in lights:
    if lights[light] == 1:
        print("%s is on" % light)
    else:
        print("%s is off" % light)

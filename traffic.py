light = input("enter your light color:")
light = light.lower()
print(light)
if light == "red":
    print("stop")
elif light == "yellow":
    print("get ready")
elif light == "green":
    print("go")
else:
    print("invalid light color")
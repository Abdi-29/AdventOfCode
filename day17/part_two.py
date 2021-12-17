def trench(x, y, target):
    step = 0, 0
    x_min, x_max, y_min, y_max = target
    velocity = x, y
    h_max = 0
    while 1:
        step = step[0] + velocity[0], step[1] + velocity[1]
        if velocity[0] == 0:
            tmp1 = 0
        else:
            if velocity[0] > 0:
                tmp1 = velocity[0] - 1
            else:
                tmp1 = velocity[0] + 1
        tmp2 = velocity[1] - 1
        velocity = tmp1, tmp2
        if step[1] > h_max:
            h_max = step[1]
        if x_min <= step[0] <= x_max and y_min <= step[1] <= y_max:
            return h_max 
        if velocity[0] > x_max:
            return -1
        if velocity[1] < y_min:
            return -1
        if velocity[0] == 0 and x_min > step[0] > x_max:
            return -1

def main():
    target = (240, 292, -90, -57)
    check = 0
    for i in range(-300, 300, 1):
        for j in range(-300, 300, 1):
          current = trench(i, j, target)
          if current != -1:
              check += 1
    print(check)
            
if __name__ == "__main__":
    main()

# The probe's x position increases by its x velocity.
# The probe's y position increases by its y velocity.
# Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1
# if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
# Due to gravity, the probe's y velocity decreases by 1.
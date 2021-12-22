def light_off(x, y, z, steps):
    x = list(x)
    y = list(y)
    z = list(z)
    for x1 in range(x[0], x[1] + 1, 1):
        for y1 in range(y[0], y[1] + 1, 1):
            for z1 in range(z[0], z[1] + 1, 1):
                tmp = x1, y1, z1
                tmp = list(tmp)
                if tmp in steps:
                    i = steps.index(tmp)
                    del steps[i]
    return steps

def light_on(x, y, z, steps):
    x = list(x)
    y = list(y)
    z = list(z)
    for x1 in range(x[0], x[1] + 1, 1):
        for y1 in range(y[0], y[1] + 1, 1):
            for z1 in range(z[0], z[1] + 1, 1):
                tmp = x1, y1, z1
                tmp = list(tmp)
                if tmp not in steps:
                    steps.append(tmp)
    return steps

def parse(reboot):
    steps = []
    for line in reboot:
        x1, y1, z1 = line.split(',')
        if 'on' in x1:
            x1, y1, z1 = x1[5:], y1[2:], z1[2:]
            x = tuple([int(x) for x in x1.split('..')])
            y = tuple([int(x) for x in y1.split('..')])
            z = tuple([int(x) for x in z1.split('..')])
            steps = light_on(x, y, z, steps)
        else:
            x1, y1, z1 = x1[6:], y1[2:], z1[2:]
            x = tuple([int(x) for x in x1.split('..')])
            y = tuple([int(x) for x in y1.split('..')])
            z = tuple([int(x) for x in z1.split('..')])
            steps = light_off(x, y, z, steps)
    print(len(steps))
    # sep, row = reboot.split(' ')
    # step = [line[2:] for line in row.split(',')]
    # print(step)
      

def main():
    reboot = open('input.txt').read().splitlines()
    parse(reboot)

if __name__ == "__main__":
    main()
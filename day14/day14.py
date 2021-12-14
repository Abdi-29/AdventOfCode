def count_letters(pair):
    value = []
    for i in pair:
        if i not in value:
            value.append(i)
    count = [0]*len(value)
    for i in range(len(value)):
        for char in pair:
            if char == value[i]:
                count[i] += 1
    print(max(count) - min(count))

def check_matches(template, pair):
    for _ in range(40):
        polymer = []
        for i in range(len(pair) - 1):
            tmp = pair[i] + pair[i + 1]
            if tmp in template:
                polymer.append(tmp[:1] + template[tmp] + tmp [2:])
            if len(pair) - 1 == i + 1:
                polymer.append(pair[i + 1])  
        pair = "".join(polymer)
    count_letters(pair)

def main():
    template = open("input.txt").read().splitlines()
    polymer = template.pop(0)
    elements = {}
    for line in template[0:]:
        rule, element = line.split(' -> ')
        elements.update({rule : element})
    check_matches(elements, polymer)
 

if __name__ == "__main__":
    main()
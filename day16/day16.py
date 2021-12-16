def operator(new_binary):
    result = []
    i = 0
    print(new_binary)
    while len(new_binary) > 12:
        Id = new_binary[0]
        print(f'id {Id}')
        # print(f'new_binary {new_binary}')
        # print(f'result {result}')
        if Id == '0':
            if i == 0:
                result.append(check_id(hex, new_binary[1:16]))
            else:
                result.append(check_id(hex, new_binary[:16]))
            new_binary = new_binary[16:]
        else:
            result.append(check_id(hex, new_binary[:11]))
            new_binary = new_binary[11:]
        i += 1
    # print("djjs ", result)

def literal_value(hex, new_binary):
    result = []
    for i in range(0, len(new_binary), 5):
        if new_binary[i] == '1':
            tmp = new_binary[i+1:i+5]
            result.append(tmp)
        else:
            tmp = new_binary[i+1:i+5]
            print(tmp)
            result.append(tmp)
            break
    return (result)

def check_id(hex, binary):
    new_binary = binary[6:]
    # print("binary ", binary)
    packet_version = binary[0:3]
    version = binary[3:6]
    if version == '100':
        result = literal_value(hex, new_binary)
    elif len(new_binary) < 12:
        return new_binary[3:]
    else:
        result = operator(new_binary)
    return result

def main():
    file = open('input.txt').read()
    result = []
    hex = { "0": '0000',
            "1": '0001',
            "2": '0010',
            "3": '0011',
            "4": '0100',
            "5": '0101',
            "6": '0110',
            "7": '0111',
            "8": '1000',
            "9": '1001',
            "A": '1010',
            "B": '1011',
            "C": '1100',
            "D": '1101',
            "E": '1110',
            "F": '1111'
    }
    binary = ""
    for char in file:
        binary += "".join(hex[char])
    result = check_id(hex, binary)
    print(result)
    # new_binary = binary[6:]
    # packet_version = binary[0:3]
    # # version = binary[3:6]
    # if check_id(new_binary) == '100':
    #     result = literal_value(hex, new_binary)
    # else:
    #     result = operator(hex, new_binary)
    # print(result)

if __name__ == "__main__":
    main()
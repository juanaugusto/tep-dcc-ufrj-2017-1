import math

qtd_inputs = int(input())

cases = [input() for i in range(qtd_inputs)]

pot = math.pow(2, 31)

last = cases[-1].split()

for case in cases:
    case = case.split()

    num_a = case[0]
    num_b = case[1]

    print('{} {}'.format(num_a, num_b))

    while True:
        num_c = []
        num_d = []
        for i in range(31):
            if num_a[i] != num_b[i]:
                num_c.append('1')
            elif num_a[i] == num_b[i]:
                num_c.append('0')

            if num_a[i] == '1' and num_b[i] == '1':
                num_d.append('1')
            elif num_a[i] == '0' or num_b[i] == '0':
                num_d.append('0')

        num_c = ''.join(num_c)
        num_d = ''.join(num_d)

        num_d = bin(int(num_d, 2) * 2).replace('0b', '').zfill(31)

        num_a = num_c
        num_b = num_d

        num_b = 'overflow' if len(num_b) > 31 else num_b

        print('{} {}'.format(num_a, num_b))

        try:
            if int(num_b, 2) == 0 or int(num_b, 2) >= pot:
                break
        except ValueError:
            break

    if case != last:
        print()




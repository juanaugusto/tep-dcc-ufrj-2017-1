qtd_strs = int(input())

strs = [input() for i in range(qtd_strs)]

for str in strs:

    open_actually = []
    try:
        for ch in str:

            if ch == '(':
                open_actually.append('(')
            elif ch == '[':
                open_actually.append('[')
            elif (ch == ')' and open_actually[len(open_actually) - 1] == '[') or (
                    ch == ']' and open_actually[len(open_actually) - 1] == '('):
                raise Exception()
            elif (ch == ')' and open_actually[len(open_actually) - 1] == '(') or (
                    ch == ']' and open_actually[len(open_actually) - 1] == '['):
                open_actually.pop()

        if len(open_actually) == 0:
            print('Yes')
        else:
            print('No')

    except Exception:
        print('No')



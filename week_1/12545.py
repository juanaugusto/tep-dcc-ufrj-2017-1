import itertools


def how_much(l1, l2):
    count_ = 0
    for e1, e2 in zip(l1, l2):
        if e1 == e2 or (e1 == '0c' and e2 == '0') or (e1 == '0' and e2 == '0c'):
            count_ += 1

    return count_


def how_diff(l1, l2):
    count_ = 0
    for e1, e2 in zip(l1, l2):
        if ((e1 == '0' or e1 == '0c') and (e2 == '1')) or ((e2 == '0' or e2 == '0c') and (e1 == '1')):
            count_ += 1

    return count_


qtd_inputs = int(input())
S_ = []
T_ = []
for i in range(qtd_inputs):
    S_.append(list(input()))
    T_.append(list(input()))

for num_case, (s, t) in enumerate(itertools.zip_longest(S_, T_), start=1):
    count = 0

    if s.count('1') > t.count('1'):
        print('Case {}: {}'.format(num_case, -1))

    else:

        for i, (ch_s, ch_t) in enumerate(zip(s, t)):

            if ch_s == '?':
                count += 1
                aux_s = list(s)
                aux_s[i] = ch_t

                if ch_t == '1' and aux_s.count('1') <= t.count('1'):
                    s[i] = '1'
                elif ch_t == '0':
                    s[i] = '0c'
                elif ch_t == '1' and aux_s.count('1') > t.count('1'):
                    s[i] = '0c'

        for i, (ch_s, ch_t) in enumerate(zip(s, t)):

            if ch_s != ch_t and ch_s == '0':
                aux_s = list(s)
                aux_s[i] = ch_t

                if aux_s.count('1') <= t.count('1'):
                    s[i] = '1'
                    count += 1

        count += how_diff(s, t) // 2

        print('Case {}: {}'.format(num_case, count))


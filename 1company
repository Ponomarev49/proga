for n in range(10, 17):
    dict = {}
    bd_fio = {}
    f = open(f'input_s1_{n}.txt', 'r')
    l = open(f'output_s1_{n}.txt', 'r')

    f1 = f.readlines()
    l1 = l.readlines()

    main = f1[-1]
    f1.pop(-1)

    for i in range(len(f1)):
        f1[i] = f1[i].replace('\n', '')
        f1[i] = f1[i].split(' ')
        if len(f1[i]) == 1:
            f1[i].append('')

    for i in range(len(l1)):
        l1[i] = l1[i].replace('\n', '')
    for i in range(0, len(f1), 2):
        if f1[i][0] != "END":
            if f1[i][0] not in dict.keys():
                dict[f1[i][0]] = [f1[i + 1][0]]
            else:
                dict[f1[i][0]].append(f1[i + 1][0])
        else:
            break

    for i in range(len(f1)):
        a = f1[i][0]
        b = ' '.join(f1[i][1:])
        if a != "END":
            if a in bd_fio.keys():
                if b != '' and bd_fio[a] == '':
                    bd_fio[a] = b
            else:
                bd_fio[a] = b
        else:
            break

    for el in bd_fio.keys():
        if bd_fio[el] == "":
            bd_fio[el] = "Unknown Name"

    c = 0
    if main in dict.keys():
        c = main
    else:
        for el in dict.keys():
            if bd_fio[el] == main:
                c = el
                break

    needs = [c]
    needs_c = needs.copy()
    lena = 0
    otv = []

    while len(needs) != 0:
        broke = 0
        for i in range(len(needs)):
            if needs[i] in dict.keys():
                for j in range(len(dict[needs[i]])):
                    needs_c.append(dict[needs[i]][j])
                    otv.append(dict[needs[i]][j])
                lena += len(dict[needs[i]])
                needs_c.remove(needs[i])
            else:
                broke += 1
        if broke == len(needs):
            break
        needs = needs_c.copy()

    otv = sorted(otv)
    final = []
    for el in otv:
        final.append(f'{el} {bd_fio[el]}')

    if not final:
        final = ['NO']

    if final == l1:
        print(f'true - {n}')

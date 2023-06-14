for l in range(13):
    a = 'input_s1_0' + str(l+1) + '.txt'
    b = 'output_s1_0' + str(l+1) + '.txt'
    if l > 8:
        a = 'input_s1_' + str(l+1) + '.txt'
        b = 'output_s1_' + str(l+1) + '.txt'
    f = open(a)
    fb = open(b)
    b = int(fb.readline())
    n = int(f.readline())
    words = []
    for i in range(n):
        words.append(f.readline().replace('\n', ''))
    n = int(f.readline())
    beg = {}
    for i in range(n):
        line = f.readline().split()
        beg[line[0]] = int(line[1])
    n = int(f.readline())
    end = {}
    for i in range(n):
        line = f.readline().split()
        end[line[0]] = int(line[1])
    k = 0
    s = 0
    beglet = ''
    endlet = ''
    for i in range(len(words)):
        for j in range(len(beg)):
            if words[i][0] == list(beg.keys())[j] and beg[list(beg.keys())[j]] > 0:
                k += 1
                beglet = words[i][0]
        for j in range(len(end)):
            if words[i][-1] == list(end.keys())[j] and end[list(end.keys())[j]] > 0:
                k += 1
                endlet = words[i][-1]
        if k == 2:
            s += 1
            beg[beglet] -= 1
            end[endlet] -= 1
        k = 0
    if s == b:
        print(str(l+1) + '. True')
    else:
        print(str(l+1) + '. False')

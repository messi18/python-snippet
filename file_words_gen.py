def words_gen(file):
    with open(file) as f:
        chs=[]
        while True:
            ch=f.read(1)
            if ch == ' ':
                yield ''.join(chs)
                chs=[]
            elif ch == '':
                yield ''.join(chs)
                chs=[]
                break;
            else:
                chs.append(ch)
if __name__ == '__main__':
    import sys
    filename=sys.argv[1]
    for w in words_gen(filename):
        print "%s" %w;

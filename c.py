
from operator import countOf


def count_win():
    with open('hammer-trades', 'r') as f:
        lines = f.readlines()
        tcount = 0
        fcount = 0
        fsymbols = []
        tsymbols = []
        for line in lines:
            if len(line) < 20:
                strx = str(line)
                if 'True' in strx:
                    newx = strx.replace(" True\n","")
                    tcount += 1
                    tsymbols.append(newx)
                elif 'False' in strx:
                    fcount += 1
                    newx = strx.replace(" False\n","")
                    fsymbols.append(newx)
        total = tcount + fcount
        winrate = (tcount / total) * (100) 
        print('------------------------------------------------')
        print('FAILED')
        print(fsymbols)
        print('------------------------------------------------')
        print('SUCCESS')
        print(tsymbols)
        print('------------------------------------------------')
        print('PROFIT:', tcount)
        print('LOSS:',fcount)
        print('WINRATE:',winrate)   
        print('------------------------------------------------')


count_win()
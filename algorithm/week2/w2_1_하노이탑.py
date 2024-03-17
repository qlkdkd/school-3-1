def hanoi_tower(n, fr, tmp, to):
    if (n==1):
        print("원판1: %s--> %s"%(fr, to))
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판%d: %s--> %s"%(n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)


if __name__=='__main__':
    hanoi_tower(4, 'A', 'B', 'C')
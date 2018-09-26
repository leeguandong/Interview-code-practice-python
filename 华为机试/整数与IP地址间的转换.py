while True:
    try:
        print(sum([256 ** j * int(i) for j, i in enumerate(input().split('.')[::-1])]))
        b = int(input())
        print('.'.join([str(b // (256 ** i) % 256) for i in range(3, -1, -1)]))
    except:
        break

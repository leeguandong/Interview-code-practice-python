x = input().replace('*', ' ').replace('#', ' ').replace('!', ' ').replace('$', ' ').split()

print(' '.join(x[::-1]))

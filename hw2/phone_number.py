def wrapper(f):
    def fun(l):
        return f(['+7 (' + n[-10:-7] + ') ' + n[-7:-4] + '-' + n[-4:-2] + '-' + n[-2:] for n in l])
    return fun


@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')

import sys
n, m = map(int, sys.stdin.readline().strip().split())

pokemon_book = {}

result = []

for i in range(1, n+1):
    pokemon = sys.stdin.readline().strip()
    pokemon_book[pokemon] = i
    pokemon_book[i] = pokemon

for _ in range(m):
    search = sys.stdin.readline().strip()
    if search.isdigit(): # 숫자인가
        print(pokemon_book[int(search)])
    else:
        print(pokemon_book[search])
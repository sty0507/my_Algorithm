import sys

N = int(sys.stdin.readline())

company = dict()

for _ in range(N):
    name, method = sys.stdin.readline().split(" ")
    method = method.strip()
    if method == "enter":
        company[name] = 1
    else:
        company[name] = 0

results = []

for i in company.keys():
    if company[i] == 1:
        results.append(i)

results.sort(reverse=True)

for result in results:
    print(result)
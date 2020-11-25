n = int(input())
games = [input().split() for x in range(n)]
wins = [x[0] for x in games if x[1] == 'win']
print(wins, len(wins), sep="\n")

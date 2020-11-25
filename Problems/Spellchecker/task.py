dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
a = input().split()
count = 0
for elem in a:
    if elem not in dictionary:
        print(elem)
        count += 1
if count == 0:
    print("OK")

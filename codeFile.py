inp = int(input())
toi = [3, 3, 3, 3, 3, 5, 6]
hindu = [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4]
et = [4, 4, 4, 4, 4, 4, 10]
bm = [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]
ht = [2, 2, 2, 2, 2, 4 ,4]
names = ["TOI", "Hindu", "ET", "BM", "HT"]
l = [sum(toi), sum(hindu), sum(et), sum(bm), sum(ht)]
dup = []
for i in range(0, len(l)):
    for j in range(0, len(l)):
        if l[i]==l[j] or (l[j] in dup):
            pass
        else:
            sumTwo = l[i] + l[j]
            if inp >= sumTwo:
                print("{},{}".format(names[i], names[j]))
                dup.append(l[i])

def diff(x, y):
    s=x
    ans1=''
    for i in s:
        if i in y:
            ans1+=i
            y=y[y.find(i)+1:]
    return ans1
def diff2(z, w):
    ans=''
    s1=z
    w=w[::-1]
    for i in s1[::-1]:
        if i in w:
            ans+=i
            w=w[w.find(i)+1:]
    return ans
ans=set(diff(x="antidisestablishmentarianism", y="antitotalitarianism"))
ans2=set(diff(y="antidisestablishmentarianism", x="antitotalitarianism"))
ans3=set(diff2(z="antidisestablishmentarianism", w="antitotalitarianism"))
ans4=set(diff2(w="antidisestablishmentarianism", z="antitotalitarianism"))
fin=""
for i in ans:
    if i in ans2 and i in ans3 and i in ans4:
        fin+=i
if fin:
    print("".join(sorted(fin)))
else:
    print(None)

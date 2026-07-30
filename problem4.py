import bisect
def insert_letter(array, letter):
    bisect.insort(array, letter)
def check(array, ans, n):
    try:
        return ans.append(array[n])
    except:
        pass
def duplicates(string, n):
    n-=1
    string=string.upper().replace(' ', '')
    array=[]
    ans=[]
    for letter in string:
        insert_letter(array, letter)
        check(array, ans, n)
    return len(set(ans))
print(duplicates('american computer science league', 5))

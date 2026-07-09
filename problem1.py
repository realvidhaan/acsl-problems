def num_transformation(n, p):
    n_list=[int(digit) for digit in str(n)]
    p_digit=n_list[::-1][p-1]
    new_i=len(n_list)-p
    n_right=n_list[:new_i]
    n_left=n_list[new_i+1:]
    new_l=[]
    new_r=[]
    for i in n_left:
        new_l.append(abs(i-p_digit))
        print(abs(i-p_digit))
    for i in n_right:
        d=0
        d=i+p_digit
        if d>9:
            new_d=str(d)
            d=int(new_d[-1])
        new_r.append(d)
        print(d)
    ans=new_r+[p_digit]+new_l
    num=""
    for i in ans:
        num+=str(i)
    return int(num)

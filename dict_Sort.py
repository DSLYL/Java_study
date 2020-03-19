# def Dict(a):
#     a1=len(a)
#     for i in range(a1-1,0,-1):
#         j=i-1
#         if a[i]> a[j]:
#             break
#     for k in range(a1-1,j,-1):
#         if a[k]>a[j]:
#             a[k],a[j]=a[j],a[k]
#             break
#     a[j+1::]=a[-1:j:-1]
# if __name__ == '__main__':
#     a=list()
#     b=int(input("列表的数量"))
#     for i in range(0,b):
#         a.append(int(input()))
#     Dict(a)

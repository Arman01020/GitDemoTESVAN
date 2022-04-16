# l=[('abcd','absb','abse'),('fdha','klmnc','ajshdjk'),('bcde','fgha','gklma')]
# print(l)
# l_sorted= sorted(l, key=lambda i: i[1][-1])
# print(l_sorted)
#
# l1 = [(1, 8, 57, 20, 25),
#      (58, 20, 6, 2, 8),
#      (6, 35, 87, 15, 3)]
# print(l1)
# print(sorted(l1, key=lambda x: str(x[1])[-1]))
#
# l2 = [{'Full name': 'Fedorova Elena', 'Age': 33, 'job_id': 'Manager', 'salary': 50000},
#      {'Full name': 'Ivanov Konstantin', 'Age': 28, 'job_id': 'IT-Prog', 'salary': 100000},
#      {'Full name': 'Glinka Margarita', 'Age': 32, 'job_id': 'ST-Clerk', 'salary': 46000}]
# print(sorted(l2, key=lambda n: n['Age']))

'''35.3. Напишите программу, которая будет считать количество четных и нечетных чисел в заданном списке с помощью lambda-функции.'''

# l = [1, 6, 7, 2, 8, 11, 5, 15]
# def tver(args):
#     chetnie_count=0
#     nechetnie_count=0
#     for i in args:
#         if i%2==0:
#             chetnie_count+=1
#         else:
#             nechetnie_count+=1
#     return print("Chetnie - ",chetnie_count, "nechetnie - ", nechetnie_count)
# tver(l)
# l2 = [1, 6, 7, 2, 8, 11, 5, 15]
# print("chetnie _ ",len(list(filter(lambda x: x%2==0 and x!=0 , l2))), "nechetnie _ ",len(list(filter(lambda x: x%2!=0 and x!=0 , l2))) )
#
# l = [2, 2, 3, 4,15]
# s = (3, 4, 5, 6)
#
# res = list(filter(lambda i: i%5==0, l+list(s)))
#
# print(res)

l = {"name": "Arman Hakobyan",
     "gender": "male",
     "email": "TestingTesvan12@15ce.com",
     "status": "active"}


def stugel(n):
    if n == "active":
        return True

    return False


print(stugel(l["status"]))

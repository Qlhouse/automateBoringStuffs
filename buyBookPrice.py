import sys

def buyBook(num, price, dis_con, dis_base):
    # num, number of books to buy
    # price, price of the book
    # dis_con, distcount condition
    # dis_base, discount基数

    total = 0
    for i in range(num):
        total = i * price
        dis_num = total // dis_con
        total_dis = total - dis_num *  dis_base
        print(i, '--->', total_dis, dis_num)

num = int(sys.argv[1])
price = float(sys.argv[2])
dis_con = float(sys.argv[3])
dis_base = float(sys.argv[4])

buyBook(num, price, dis_con, dis_base)

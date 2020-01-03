"""
Problem Statement
collections.Counter() 
A counter is container, where elements are stored as dictionary keys and their counts are stored as dictionary values.
Sample Code
>>> from collections import Counter
>>> 
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5]
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1]
Task
Raghu is a shoe shop owner. His shop has X number of shoes. 
He has a list containing size of each shoe he has in his shop. 
There are N number of customers, who are willing to pay xi amount of money only if they get the shoe of their desired size.
Your task is to compute, how much money Raghu earned.
Input Format
First line contains, X number of shoes. 
Second line contains, space separated size of the shoes. 
Third line contains, N number of customers. 
Next N line contain, space separated values of shoe size and xi price of shoe.
Constraints
0<X<103 
0<N≤103 
20<xi<100 
2<shoe size<20
Output Format
Print the amount of money earned by Raghu
Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output
200
Explanation
Customer 1 : Purchased shoe of size 6 for $ 55. 
Customer 2 : Purchased shoe of size 6 for $ 45. 
Customer 3 : Size 6 not available, so no purchase. 
Customer 4 : Purchased shoe of size 4 for $ 40. 
Customer 5 : Purchased shoe of size 18 for $ 60. 
Customer 6 : Size 10 not available, so no purchase.
Total money earned = 55 + 45 + 40 + 60 = $ 200
"""
from collections import Counter

def read_data():
    d={}
    d["shoes_count"]=int(raw_input())
    d["sizes"]=Counter(map(int,raw_input().split()))
    d["customers_count"]=int(raw_input())
    d["wanted_sizes"]=[]
    for i in range(d["customers_count"]):
        d["wanted_sizes"].append(map(int,raw_input().split()))
        
    return d

def count_money_amount(shoes_shopping_info):
    money_amount=0
    for i in range (shoes_shopping_info["customers_count"]):
        if(shoes_shopping_info["sizes"][shoes_shopping_info["wanted_sizes"][i][0]]>0):  
            shoes_shopping_info["sizes"][shoes_shopping_info["wanted_sizes"][i][0]]-=1
            money_amount+=shoes_shopping_info["wanted_sizes"][i][1]
       
    return money_amount


if __name__ == '__main__':
    print (count_money_amount(read_data()))

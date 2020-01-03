"""
collections.OrderedDict
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.
Example
Code
>>> from collections import OrderedDict
>>> 
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>> 
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>> 
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>> 
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
Task
You are the manager of a supermarket. 
You have a list of N items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.
item_name = Name of the item. 
net_price = Quantity of the item sold multiplied by the price of each item.
Input Format
The first line contains the number of items, N. 
The next N lines contains the item's name and price, separated by a space.
Constraints
0<N≤100
Output Format
Print the item_name and net_price in order of its first occurrence.
Sample Input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
Explanation
BANANA FRIES: Quantity bought: 1, Price: 12 
Net Price: 12 
POTATO CHIPS: Quantity bought: 2, Price: 30
Net Price: 60 
APPLE JUICE: Quantity bought: 2, Price: 10 
Net Price: 20 
CANDY: Quantity bought: 4, Price: 5 
Net Price: 20
"""

from collections import OrderedDict

def count_price():
    line_count=int(raw_input())
    products_sold=OrderedDict()
    for _ in range (line_count):
        product_name, price =raw_input().rsplit(' ',1)
        price=int(price)
        if(products_sold.has_key(product_name)):
            products_sold[product_name]+=price
        else:
            products_sold.__setitem__(product_name,price)
    
    for key,value in products_sold.items():
        print(key+" "+str(value))


        

if __name__=='__main__':
    count_price()

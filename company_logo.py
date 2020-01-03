"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""

from collections import Counter


if __name__ == '__main__':
    letters_count=Counter(raw_input())
   
    ordered_letters_count=sorted(letters_count.iteritems(),key=lambda x: (-x[1],x[0]))

    print ''.join(map(lambda x:x[0]+' '+str(x[1])+'\n',ordered_letters_count[:3]))


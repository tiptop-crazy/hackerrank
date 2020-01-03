# Lists




# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.

# print: Print the list.

# remove e: Delete the first occurrence of integer e.

# append e: Insert integer e at the end of the list.

# sort: Sort the list.

# pop: Pop the last element from the list.

# reverse: Reverse the list.



# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above.

# Iterate through each command in order and perform the corresponding operation on your list.



# Input Format

# The first line contains an integer, n, denoting the number of commands. 

# Each line i of the n subsequent lines contains one of the commands described above.



# Constraints

# The elements added to the list must be integers.



# Output Format

# For each command of type print, print the list on a new line.





# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    l = []

    N = int(raw_input())

    for i in range(N):
        command=raw_input().split()
        if len(command)==3:
            eval("l."+command[0]+"("+command[1]+","+command[2]+")")
        elif len(command)==2:
            eval("l."+command[0]+"("+command[1]+")")
        elif command[0]=="print":
            print(l)
        else:
            eval("l."+command[0]+"()")




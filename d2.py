# name = "shrenitha"
# name[0]="s"
# name = "s"+"hrenitha"
# print(name)

# str1 = "All silver tea cups"
# for i in range(len(str1)):
#     if str1[i]==" "and str1[i+1]!=" ":
#         str1 = str1[:i+1]+str1[i+1].upper()+str1[i+2:]
# print(str1)#to print starting letter capital

# print(input("enter").title())

# list = "1 2 3 4"
# list=list.split()
# print(list)

# a = "all silver tea cups"
# b = a.split()
# c= "_".join(b)
# # print(c) #snake


# a= "all silver tea cups"
# b = a.split(" ")
# c = "-".join(b)
# print(c) 

# a= "all silver tea cups".title()
# b = a.split(" ")
# c = "".join(b)
# print(c)  #pascal


# a= "all silver tea cups".title()
# b = a.split(" ")
# c = "".join(b)
# c=c[0].lower()+c[1:]
# print(c) #camel


# n = input().lower()
# c = 0 
# for i in n:
#     if i in "aeiou":
#         c+=1
# print(c) #for vowel count

# n = input()
# new_str =" "
# for i in n:
#     if i.isupper():
#         new_str += i.lower()
#     else:
#         new_str += i.upper()
# print(new_str) #coverts upper to lower and vice versa

# l1 = input()
# l2 = sorted(l1)
# print(l2[len(l2)-1]) #to find largest num

# l1 = input()
# l2 = sorted(l1)
# print(l2[len(l2)-2]) #second largest

# list_1 = [3,5,6,7,8,9]
# highest = list_1[0]
# for i in range(len(list_1)):
#     if list_1[i]>highest:
#         highest = list_1[i]
# print(highest)        


#day-3

# list_1 = [3,6,4,7,6,7,3]
# list_2 = set(list_1)
# print(list_2) #removes duplicates and gives in order

# list_1 = [3,6,4,7,6,7,3]
# first_sum= sum(list_1)
# second_sum = sum(set(list_1))*2
# res = second_sum-first_sum
# print(res)   #here it doubles each number and gives the output which is single and unique

# n = int(input())
# fact = 1
# for i in range(n,1,-1):
#     fact *=i  = fact=fact*i
# print(fact)  #factorial of number

# n = 5
# f = 1
# for i in range(n*11):
#     f = i*n+n
# print(f)


# n = 5
# f = 0
# for i in range(1,11):
#     f =f+n*i
# print(f)    #multiples and sum of 5

# n = int(input())
# print(n*55)   #another method


# list_1 = [1,2,9,7,4,6,2]
# target = 7
# for i in range(len(list_1)):
#     if target==list_1[i]:
#         print(i)
#         break #linear search,searches for target index

# list_1 = [1,2,3,4,5,6,7,8,9,10]
# target=8
# start=0
# end=len(list_1)-1
# index=-1
# while(start<=end):
#     middle = (start+end)//2 
#     if list_1[middle]==target:
#         index = (middle)
#         break
#     elif list_1[middle]>target:
#         end = middle-1
#     elif list_1[middle]<target:
#         start = middle-1
# print(index) #binary search

# n = int(input())
# for i in range(1,n+1):
#     print("* "*i) #for stars #triangle

# n = int(input())
# for i in range(n,0,-1):
#     print("* "*i)# inverted triangle

# n=int(input())
# for i in range(1,n+1):
#     str1 = ""
#     for j in range(1,i+1):
#         str1+=str(j)+" "
#     print(str1) #number triangle


# n=int(input())
# for i in range(n,0,-1):
#     str1 = ""
#     for j in range(1,i+1):
#         str1+=str(j)+" "
#     print(str1) #inverted number

# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i) #pyramid of stars
   
# n = int(input())
# for i in range(n,0,-1):
#     print(" "*(n-i)+"* "*i)#reverse pyramid

# n = int(input())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "*i)
#     else:
#         print("*"+" "*(2*i-3)+"*")#hallow pyramid

n = int(input())
for i in range(1,n+1):
    if i==1 or i==5 :
        print(" "*(n-i)+"* "*i)
    else:
        print("*"+" "*(2*i-3)+"*")
        
    
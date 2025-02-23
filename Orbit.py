

# 1 Factorial
# def fact(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*fact(n-1)
# print("Factorial of given number is :",fact(5))   

# 2 Average of numbers

# total = 0
# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     total = total + i
# avg = total / num
# print("Average:", avg)
# print(total)

# 3 Average of elemnt in array

# sum=0
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in range (len(list)):
#     sum=sum+list[i]
# avg=sum/len(list)
# print(avg)

# 4 Common in 2 list

# list1 =[1,2,3,4,5]
# list2 =[4,5,6,7,8]
# commont_elements = set(list1) & set(list2)
# print(commont_elements)
   
   
#5 Random number 1-9 
# import random
# rand=random.randint(1,9)
# print(rand)


# 6 Prime number
# num = int(input("Enter a number"))
# if num>1:
#     for i in range (2,num):
#         if (num % i)== 0:
#             print("Not prime number")
#             break
#     else:
#         print("It is prime number")
# else:
#     print("Not Prime number")
    
# sql
# select sum(city.population) from city join country on City.CountryCode = County.Code where country.continent ="Asia"; 

# num = int(input("Enter a number"))
# if num>1:
#     for i in range (2,num):
#         if(num%i)==0:
#             print("Not prime")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not Prime")

# def fact(n):
#     if(n==0) or (n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# print("Factorial of number is: ",fact(5))

# total=0
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in range(1,len(list)):
#     total= total+list[i]
# avg=total/len(list)
# print(avg)

        
# def fact(n):
#     if (n==1) or (n==0):
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# total=0
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in range (len(list)):
#     total= total+ list[i]
# avg= total/len(list)
# print(avg)
    
# total=0
# sum=int(input("Enter a number"))
# for i in range (1,sum+1):
#     total=total+i
# avg=total/sum
# print(sum)
    
    
# num= int(input("enter a number"))
# if num>1:
#     for i in range (2,num):
#         if(num%i)==0:
#             print("Not prime")
#             break
#     else:
#         print("prime number")
# else:
#     print("not prime")

# import random
# num= random.randint(1,9)
# print(num)

list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

common = set(list1) & set(list2)
print(common)
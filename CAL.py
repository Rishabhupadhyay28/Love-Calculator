print('''
 _                             _            _       _             
| |                           | |          | |     | |            
| | _____   _____     ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |/ _ \ \ / / _ \   / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| | (_) \ V /  __/  | (_| (_| | | (__| |_| | | (_| | || (_) | |   
|_|\___/ \_/ \___|   \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                  
                                                                  ''')
name1=input("enter the name of first person: \n")
name2=input("enter the name of second person: \n")
combine_name=name1+name2
lower_case=combine_name.lower()

a=lower_case.count("t")
b=lower_case.count("r")
c=lower_case.count("u")
d=lower_case.count("e")

true=a+b+c+d

i=lower_case.count("l")
j=lower_case.count("o")
k=lower_case.count("v")
z=lower_case.count("e")
love=i+j+k+z
final=str(true)+str(love)
print(f"your love % is {final} %")

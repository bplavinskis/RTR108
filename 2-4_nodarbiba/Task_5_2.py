largest = 0				
smallest = 0xff				
while True:
    num = input("Enter a number: ")	
    if num == "done" : break		
    try:				
        n = int(num)			
    except:				
        print("Invalid input")		
    if largest < n: largest = n		
    if smallest > n: smallest = n	

print("Maximum is", largest)		
print("Minimum is", smallest)

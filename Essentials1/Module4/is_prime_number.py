#   Autor   :   XhannAmatH

def is_prime(num):
    
    prime=True
    
    for i in range(num):
        if(i<2 or i==num):
            pass
        elif num%i==0:
            prime=False
        
    return prime
    
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


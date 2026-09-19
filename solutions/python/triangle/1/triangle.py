def all_posi(sides):
    a, b, c=sides
    if (a>0) and (b>0) and (c>0) and (a+b>=c) and (a+c>=b) and (b+c>=a):
        return True 
    return False 

#print(all_posi([1, 3, 1]))
    
def equilateral(sides):
    a, b, c=sides
    if all_posi(sides) and a==b==c:
        return True
    return False
    pass


def isosceles(sides):
    a, b, c=sides
    #print (all_posi)
    if all_posi(sides) and ((a==b) or (a==c) or (b==c)):
        return True 
    return False
    #print all_posi
    pass

def scalene(sides):
    a, b, c=sides 
    if all_posi(sides) and a!=b and a!=c and b!=c:
       return True
    return False
    pass


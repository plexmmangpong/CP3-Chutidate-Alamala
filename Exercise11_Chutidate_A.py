height = int(input("Enter Pyramid height  : "))
space  = int(input("Enter Pyramid Space   : "))
spaceleftstep = height*space
spacerightstep = height-height
spacemiddle = height-height
for i in range(height):
    
    spacemiddle  += space
    
    rightspace = ("*"*spacerightstep)
    middle =("*"*(spacemiddle))
    leftspace = " "*spaceleftstep
    
    print(leftspace+middle+rightspace)
    
    spaceleftstep -=space
    spacerightstep +=space
    

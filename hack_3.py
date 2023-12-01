"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):

        
    list_comp = [("a","@"),("e","3"),("i","¡"),("o","0"),("u","v"),("A","@"),("E","3"),("I","¡"),("O","0"),("U","v")]

    if len(result)>=2:      
        result = result[0].upper() + result[1:-1] + result[-1].upper()

    for i in result:
        for x in list_comp:
            if i in x[0]: result = result.replace(i,x[1])
    
    return result

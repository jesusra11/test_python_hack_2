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

result = "fooziman"

def fn_hack_3(result):
    result = result.replace("o","0")
    result = result.replace("i", "¡")
    result = result.replace("a", "@")
    result = result.replace("q", "Q")
    result = result.replace("u", "v")
    result = result.replace("x", "X")
    result = result.replace("n", "N")
    result = result[0].upper() + result[1:]
    return result


print(fn_hack_3(result))

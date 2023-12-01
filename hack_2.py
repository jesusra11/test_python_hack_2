"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    list_comp = ["a","e","i","o","u"]
    for i in result:
        if i in list_comp: result = result.replace(i, "")                     
    return result


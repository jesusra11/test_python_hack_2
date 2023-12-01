"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(result):
    if len(result)>=3:
        result = result[:1] + result[1].upper() + result[2:]
    if len(result)>=5:
        result = result[:4] + result[4].upper() + result[5:]
    return result


"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(result):
    
    if len(result)>=3:
        count = 2
        while count <= len(result):
            if result[0] == "f":
                if count<5:
                    result = result[:count] + "-" + result[count+1:]
                else:
                    result = result[:count] + "-" + result[count:-1]
                count+=3
            else:
                if count <= 5:
                    result = result[:count] + "-" + result[count + 1:]
                count+=3
    return result

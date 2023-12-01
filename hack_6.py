"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    list_comp = ["a","b","c","d","e"]
    if result==[]:
        result.append("0")
    else:
        for i in range(len(result)):
            if (result[i] in list_comp) and i%2==0:
                result[i] = f"{i+1}"
            elif (result[i] in list_comp) and i%2!=0:
                 result[i] = "-"
    return result



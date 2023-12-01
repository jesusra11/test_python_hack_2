"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    list_comp = ["a","b","c","d","e"]
    i=0
    if result==[]:
        result.append(0)
    else:
        while i < len(result):
            if (result[i] in list_comp) and i%2==0:
                result[i] = f"{i+1}"
            elif (result[i] in list_comp) and i%2!=0:
                 result[i] = i+1
            i+=1
    return result

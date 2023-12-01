"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

result = ["a","b","c","d","e"]

def fn_hack_8(input_list):
    result = []  
    for i in range(len(input_list)):
        if len(input_list) > 1:
            result.append(f"{input_list[-i - 1]}-{i + 1}")
        else:
            result.append(str(i + 1))
    result.reverse()
    return result


print(fn_hack_8(result))

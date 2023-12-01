"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(result):
    count = 1
    for i in range(len(result)):
        if isinstance(result[i],dict):           
            for k,v in result[i].items():
                k,v=count, count+1
                result[i] = {f"{k}":f"{v}"}
        else:
            result[i]={f"{count}",f"{count+1}"}
        count+=2
    return result

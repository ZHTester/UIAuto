
"""
# @Time    : 2019-10-11 09:50
# @Author  : Function
# @FileName    : table_write.py
# @Software: PyCharm

"""
def get_length(ts):
    ls = []
    hs = ts['head']
    for h in hs:
        ls.append(len(h))
    bs = ts['body']
    for b in bs:
        for i in range(len(ls)):
            li = len(b[i])
            if ls[i] < li:
               ls[i] = li
    return ls
def out_line(ts):
    rs = '+'
    ls = get_length(ts)
    for l in ls:
        rs += '-'*(l+2)+'+'
    rs += '\n'
    return rs

def out_head(ts):
    rs = '|'
    ls = get_length(ts)
    hs = ts['head']
    for i in range(len(ls)):
        rs += ''+hs[i]+''*(ls[i]-len(hs[i]))+' |'
    rs += '\n'
    return rs

def out_body(ts):
    rs = ''
    ls = get_length(ts)
    bs = ts['body']
    for i in bs:
        r ='|'
        for j in range(len(ls)):
            r += ''+i[j]+''*(ls[j]-len(i[j]))+'  |'
        rs += r + '\n'
    return rs
def out_table(ts):
    rs = out_line(ts)
    rs += out_head(ts)
    rs += out_line(ts)
    rs += out_body(ts)
    rs += out_line(ts)
    return rs

if __name__ == '__main__':
    T = {
            'head':['用例总数','成功数','失败数','成功率','失败率'],
            'body':[
                        ['100','50', '50', '20%','80%']
                    ]
            }
    print(out_table(T),end='')

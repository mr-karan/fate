def icon_list(p_list,*pos):
    if pos:
        return [p_list[i][pos[0]] for i in range(len(p_list)) if (p_list[i][pos[0]] is not None)]
    else:
        return [p_list[i][2] for i in range(len(p_list))]
    
def icon_output(l):
    print('Icon''(s) matched this criteria :')
    for i in l:
        print(i)
    
def give_id_unicode(p_list,*text):
    if text:
        id_unicode = {p_list[i][2]:p_list[i][3] for i in range(len(p_list)) if (p_list[i][text[1]] is not None) and (text[0] in p_list[i][text[1]])}
    else:
        id_unicode = {p_list[i][2]:p_list[i][3] for i in range(len(p_list))}
    return id_unicode

def clean(a):
    for i in a:
        try:
            if (i['aliases']):
                continue
        except KeyError:
            i['aliases']=''
    for i in a:
        try:
            if (i['filter']):
                continue
        except KeyError:
            i['filter']=''     
    return a 
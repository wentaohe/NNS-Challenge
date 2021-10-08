def search_through_dict(myDict, lookup):
    
    keylist = []
    for key, value in myDict.items():
        for v in value:
            if lookup in v:
                keylist.append(key)
    return keylist
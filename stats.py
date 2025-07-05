def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    words = text.lower()
    characters ={}
    for character in words:
        if character.isalpha():
            if character in characters:
                characters[character]+=1
            else:
                characters[character]=1
    return characters

def sort_on(items):
    return items["num"]

def sort_dic(dics):
    list_of_dic=[]
    for dic in dics:
        new_dic={}
        new_dic["char"]=dic
        new_dic["num"]=dics[dic]
        list_of_dic.append(new_dic)
    list_of_dic.sort(reverse=True, key=sort_on)
    for i in list_of_dic:
        print(f"{i["char"]}: {i["num"]}")
    return list_of_dic

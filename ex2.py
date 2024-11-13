def Read_Categories_Keywords():
    with open ("keywords_toyExample.txt", "r") as cat_file:
        LCategories = []
        LKeywords = []
        for line in cat_file:
            first_word = line.strip().split()[0][:-1]
            LCategories.append(first_word)
            
            keyword_set = set(line.strip().split(" ")[1:])
            LKeywords.append(keyword_set)
            
    return LCategories, LKeywords
            

#main

print(Read_Categories_Keywords())

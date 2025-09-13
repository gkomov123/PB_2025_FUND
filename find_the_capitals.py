string = input()

def capital_indeces(str):
      return [i for i, char in enumerate(string) if char.isupper()]



#for i, letter in enumerate(string):
    #capitals_list = []
    #if letter.isupper():
      #capitals_list.append(letter)
      #print(list(enumerate(capitals_list)))


#for i, item in enumerate(capitals_list):
 #  print(i)

#print(capitals_list)
print(capital_indeces(string))
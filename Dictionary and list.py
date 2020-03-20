price_lst = ['125.62', '25', '566', '159']
my_items = ['speakers', 'mouse', 'laptop', 'HDD']

new_dict = {}               #create a empty dictionary

for k in my_items:          #a for loop for find all items in my_items
    for v in price_lst:     #a for loop for find all items in price_lst
        new_dict[k] = v
        price_lst.remove(v)     #remove the one value in price_lst
        

print(str(new_dict))                #print the new dictionary

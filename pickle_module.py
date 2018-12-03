import pickle

# store_list=['eggs','apple','peach']
# with open('/opt/store.data','wb') as fobj:
#     pickle.dump(store_list,fobj)
#

with open('/opt/store.data','rb') as fobj:
    mylist = pickle.load(fobj)
print(mylist)
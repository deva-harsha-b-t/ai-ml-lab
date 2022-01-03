import pandas as pd
from collections import Counter
import math
df_tennis=pd.read_csv("company.csv")

def entropy_list(a_list):
    cnt=Counter(x for x in a_list)
    num_instance=len(a_list)*1.0
    probs=[x/num_instance for x in cnt.values()]
    return entropy(probs)

def entropy(probs):
    return sum([-prob*math.log(prob,2) for prob in probs])

def info_gain(df,attr,target):
    df_split=df.groupby(attr)   #splitting the dataset into two parts, in which one dataset consist of a column values of attribute 'attr'
    nobs=len(df.index)*1.0      #no. of rows in the dataset
    df_agg_ent=df_split.agg({target:[entropy_list, lambda x: len(x)/nobs]})
    #print(df_agg_ent)
    df_agg_ent.columns=['Entropy','PropObserved']   #adding columns names to the dataset 'df_agg_ent'
    new_entropy=sum(df_agg_ent['Entropy']*df_agg_ent["PropObserved"])
    old_entropy=entropy_list(df[target])
    return old_entropy-new_entropy

def id3(df,attribute_name,target):
    cnt=Counter(x for x in df[target])
    if len(cnt)==1:
        return next(iter(cnt))
    elif df.empty or (not attribute_name):
        return None
    else:
        #default_class=max(cnt.keys())
        gains=[info_gain(df,attr,target) for attr in attribute_name]  #gains stores ig values for each atttributes in dataset
        index_max=gains.index(max(gains))
        best_attr=attribute_name[index_max]
        tree={best_attr:{}}   #creating empty dict
        remaining_attr=[x for x in attribute_name if x!=best_attr]
        #remaining_attr=attribute_name.remove(best_attr)
        for attr_val,data_subset in df.groupby(best_attr):
            subtree=id3(data_subset,remaining_attr,target)
            tree[best_attr][attr_val]=subtree
        return tree

attribute_names=list(df_tennis.columns)
attribute_names.remove('Profit')
tree=id3(df_tennis,attribute_names,'Profit')
print("The resulant Decision Tree")
print(tree)

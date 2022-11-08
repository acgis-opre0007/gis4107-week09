# ------------------------------------------------------------------------------
# Name:        DictListUtils.py
#
# Purpose:     Various utility functions for working with dictionaries and lists
#
# Author:      David Viljoen
#
# Created:     18/12/2021
# Last update: 31/10/2022
# ------------------------------------------------------------------------------




def get_missing_keys(dict_ref, dict_to_compare):
    """Returns a list of missing keys.
       dict_to_compare is the dict that may have missing keys
       dict_ref is the dict to compare it to
       Example:  dict_ref = {1:1, 2:2, 3:3}, dict_to_compare = {2:2}
                 returns [1, 3]
    """
    dict_ref = {1:1, 2:2, 3:3}
    dict_to_compare = {2:2}

    res = []


    for key in dict_ref:
        if key not in dict_to_compare:
            res.append(key)
    return res 

       
                        
 


def get_missing_keys_with_count(dict_ref, dict_to_compare):
    """Returns a count and a list of missing keys.
       dict_to_compare is the dict that may have missing keys
       dict_ref is the dict to compare it to
       Example:  dict_ref = {1:1, 2:2, 3:3}, dict_to_compare = {2:2}
                 returns (2, [1, 3])
    """
    dict_ref = {1:1, 2:2, 3:3}
    dict_to_compare = {2:2}
    missing_keys =  2 
    
    res = []

    for key in dict_ref:
        if key not in dict_to_compare:
            res.append(key)
    return (missing_keys,res) 




def get_unique(in_list):
    """Retuns a list of unique values from in_list
    Example:  in_list = [1, 2, 2, 3] returns [1, 2, 3]
    """
    in_list = [1, 2, 2, 3]
    
    res = []

    unique_numbers = set(in_list)


    for key in unique_numbers: 
        res.append(key)
    return res 





def flatten_list(in_list):
    """ 
    This function will return a list that contains the items of
    in_list that are not lists or tuples as well as the items
    of the list(s) or tuples(s).  The lists and tuples of in_list 
    will be removed.  
    For example, if in_list = [1, (2,3), [4,5]], 
    the returned list would be [1, 2, 3, 4, 5]
    """
    in_list = [1, (2,3), [4,5]] 

    res = []

    for item in in_list:
        if str(type(item)) == "<class 'tuple'>": 
            for i in item:
                p = int(i)
                res.append(p)
        elif str(type(item)) == "<class 'list'>":
            for i in item: 
                res.append(i)
        else: 
            res.append(item)
    return res 
  


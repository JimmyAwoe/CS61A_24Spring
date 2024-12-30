# the lecture achieve of tree
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

t2 = tree(5, [tree(6), tree(7)])
t1 = tree(3, [tree(4), t2])

# Q1
result = label(min(branches(max([t1, t2], key=label)), key=label))
# result = 6

# Q2
def has_path(t, p):
    """
    >>> has_path(t1, [3, 5, 6])
    True
    """
    if label(t) == p[0] and len(p) == 1:
        return True
    elif label(t) != p[0]:
        return False
    else:
        for b in branches(t):
            if has_path(b, p[1:]) == True:
                return True
        return False
        # or use this one line expression
        #return True in [has_path(b, p[1:]) for b in branches(t)]

# Q3 
def find_path(t, x):
    if is_leaf(t) and label(t) != x:
        return None 
    elif is_leaf(t) and label(t) == x:
        return [label(t)]
    else:
        for b in branches(t):
            sublist = find_path(b, x)
            if sublist:
                return [label(t)] + sublist
        return None
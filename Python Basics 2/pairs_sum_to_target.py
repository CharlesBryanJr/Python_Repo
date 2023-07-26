def pairs_sum_to_target(list1, list2, target):
    # Write your code here.
    sum_equals_target = []

    for i, integer1 in enumerate(list1):
        for ii, integer2 in enumerate(list2):
            if integer1 + integer2 == target:
                add_indice_pair = [i, ii]
                sum_equals_target.append(add_indice_pair)

    return sum_equals_target

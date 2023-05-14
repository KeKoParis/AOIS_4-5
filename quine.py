import formatting as form


def mul(x, y):  # Multiply 2 minterms
    res = []
    for i in x:
        if "!" + i in y or (len(i) == 2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            res.append(i)
    return res


def multiply(x, y):  # Multiply 2 expressions
    res = []
    for i in x:
        for j in y:
            tmp = mul(i, j)
            res.append(tmp) if len(tmp) != 0 else None
    return res


def find_epi(x):  # Function to find essential prime implicants from prime implicants chart
    res = []
    for i in x:
        if len(x[i]) == 1:
            res.append(x[i][0]) if x[i][0] not in res else None
    return res


def findVariables(
        x):  # Function to find variables in a minterm. For example, the minterm --01 has !C and D as variables
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append('!' + 'x' + str(i + 1))
        elif x[i] == '1':
            var_list.append('x' + str(i + 1))
    return var_list


def flatten(x):  # Flattens a list
    flattened_items = []
    for i in x:
        flattened_items.extend(x[i])
    return flattened_items


def findminterms(a):
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a, 2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2, gaps))]
    minterms = []
    for i in range(pow(2, gaps)):
        curr_minterms, ind = a[:], -1
        for j in x[0]:
            if ind != -1:
                ind = ind + curr_minterms[ind + 1:].find('-') + 1
            else:
                ind = curr_minterms[ind + 1:].find('-')
            curr_minterms = curr_minterms[:ind] + j + curr_minterms[ind + 1:]
        minterms.append(str(int(curr_minterms, 2)))
        x.pop(0)
    return minterms


def compare(a, b):  # Function for checking if 2 minterms differ by 1 bit only
    c, mismatch_index = 0, 0
    for i in range(len(a)):
        if a[i] != b[i]:
            mismatch_index = i
            c += 1
            if c > 1:
                return False, None
    return True, mismatch_index


def removeTerms(_chart, terms):  # Removes minterms which are already covered from chart
    for i in terms:
        for j in findminterms(i):
            try:
                del _chart[j]
            except KeyError:
                pass


def solve(expr):
    expr_str = form.formatting(expr)

    mt = [int(i) for i in expr_str.strip().split()]
    mt.sort()
    minterms = mt
    minterms.sort()
    size = len(bin(minterms[-1])) - 2
    groups, all_pi = {}, set()

    # Primary grouping starts
    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]
    # Primary grouping ends

    # Process for creating tables and finding prime implicants starts
    while True:
        cp_group = groups.copy()
        groups, m, marked, should_stop = {}, 0, set(), True
        list_sort = sorted(list(cp_group.keys()))
        for i in range(len(list_sort) - 1):
            for j in cp_group[list_sort[i]]:  # Loop which iterates through current group elements
                for k in cp_group[list_sort[i + 1]]:  # Loop which iterates through next group elements
                    res = compare(j, k)  # Compare the minterms
                    if res[0]:  # If the minterms differ by 1 bit only
                        try:
                            groups[m].append(j[:res[1]] + '-' + j[res[1] + 1:]) if j[:res[1]] + '-' + j[res[
                                                                                                            1] + 1:] not in \
                                                                                   groups[
                                                                                       m] else None
                            # Put a '-' in the changing bit and add it to corresponding group
                        except KeyError:
                            groups[m] = [j[:res[1]] + '-' + j[res[1] + 1:]]
                            # If the group doesn't exist, create the group at first and then put a '-' in the changing
                            # bit and add it to the newly created group
                        should_stop = False
                        marked.add(j)  # Mark element j
                        marked.add(k)  # Mark element k
            m += 1
        local_unmarked = set(flatten(cp_group)).difference(marked)  # Unmarked elements of each table
        all_pi = all_pi.union(local_unmarked)  # Adding Prime Implicants to global list

        if should_stop:  # If the minterms cannot be combined further
            break

    chart = {}

    for i in all_pi:
        merged_minterms, y = findminterms(i), 0
        for j in merged_minterms:
            try:
                chart[j].append(i) if i not in chart[j] else None  # Add minterm in chart
            except KeyError:
                chart[j] = [i]

    epi = find_epi(chart)  # Finding essential prime implicants
    removeTerms(chart, epi)  # Remove epi related columns from chart

    if len(chart) == 0:  # If no minterms remain after removing epi related columns
        final_result = [findVariables(i) for i in epi]  # Final result with only EPIs
    else:  # Else follow Petrick's method for further simplification
        petr = [[findVariables(j) for j in chart[i]] for i in chart]
        while len(petr) > 1:  # Keep multiplying until we get the SOP form of petr
            petr[1] = multiply(petr[0], petr[1])
            petr.pop(0)
        final_result = [min(petr[0], key=len)]  # Choosing the term with minimum variables from petr
        final_result.extend(findVariables(i) for i in epi)  # Adding the EPIs to final solution
    print('Solution: ' + ' + '.join(''.join(i) for i in final_result))

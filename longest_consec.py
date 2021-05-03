def longest_consec(strarr, k):
    result = ""
    if len(strarr) < 1:
        return result
    indexes = [len(strarr[i]) for i in range(len(strarr))]
    index = 0
    while index < k and len(indexes) > 0:
        i = indexes.index(max(indexes))
        if i >= 0:
            result += strarr[i]
            del strarr[i]
            del indexes[i]
        index += 1
    return result


def main():
    strarr = ["zone", "abigail", "theta", "form", "libe", "zas"]
    p = longest_consec(strarr, 2)
    print(p)

if __name__ == '__main__':
    main()

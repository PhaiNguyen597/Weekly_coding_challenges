def unique_styles(lst):
    tmp = []
    for i in range(len(lst)):
        tmp_str = lst[i].split(",")
        for j in range(len(tmp_str)):
            if tmp_str[j] not in tmp:
                tmp.append(tmp_str[j])
    return len(tmp)


print(
    unique_styles(
        ["Soul", "House,Folk", "Trance,Downtempo,Big Beat,House", "Deep House", "Soul"]
    )
)

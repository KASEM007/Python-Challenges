def histogram(str):
    d = dict()
    for char in str:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d


# h = histogram("brontosaurus")
# # print(h)
# # h = histogram("a")
# # print(h)
# print(h.get("r"))


# def print_hist(h):
#     for c in h:
#         print(c, h[c])


# h = histogram("parrot")
# print_hist(h)
print(histogram("parrot"))

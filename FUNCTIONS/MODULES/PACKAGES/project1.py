
def sort_colors(colors):
    color_list = colors.split("-")   # split by hyphen
    color_list.sort()                # sort alphabetically
    result = "-".join(color_list)    # join with hyphen
    return result


# input
colors = input()

# output
print(sort_colors(colors))

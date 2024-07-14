def generate_Color(rating_Lists):
    color_Lists = []
    for i in rating_Lists:
        if i <= 1199:
            color_Lists.append("Grey")
        elif i <= 1399:
            color_Lists.append("Green")
        elif i <= 1599:
            color_Lists.append("Cyan")
        elif i <= 1899:
            color_Lists.append("Blue")
        elif i <= 2099:
            color_Lists.append("Violet")
        elif i <= 2399:
            color_Lists.append("Orange")
        elif i <= 2999:
            color_Lists.append("Red")
        elif i >= 3000:
            color_Lists.append("Black")

    return color_Lists

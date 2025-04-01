def theme(theme):
    if theme == "dark":
        return "#0F2B38"
    elif theme == "light":
        return "#F2FAED"
    else:
        return "#FFB338"


print(theme("dark"))


def theme2(theme):
    match theme:
        case "dark":
            return "#0F2B38"
        case "light":
            return "#F2FAED"
        case _:
            return "#FFB338"


print(theme2("dark"))


dict_theme = {
    "dark": "#0F2B38",
    "light": "#F2FAED",
    "default": "#FFB338",
}

print(dict_theme.get("light", dict_theme["default"]))
print(dict_theme.get("medium", "#FFB338"))

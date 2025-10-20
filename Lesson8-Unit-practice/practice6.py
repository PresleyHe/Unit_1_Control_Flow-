Emoji_indicator = ":fire:cool:100:"
validation = True
if len(Emoji_indicator) < 2:
    validation = False
elif Emoji_indicator[0] == ":" and Emoji_indicator[-1] == ":":
    validation = True
else:
    validation = False
print(f"Emoji indicator is {validation}")
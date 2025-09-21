def troll(original_text):
    new_text = original_text.replace("Barcelona is the best team", "Hala Madrid")
    return new_text

result = troll("Barcelona is the best team!")
print(result)
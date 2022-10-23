def roll(text):
    return text[::-1]

def swoop(text):
    text = list(text)
    for i in range(len(text)):
        if text[i] not in '{}':
            text[i] = chr(ord(text[i]) - (i % 6))
    return ''.join(text)

print(roll(swoop("}zudidsbybwxaqaqehxbebimt`jks{XNidpka")))

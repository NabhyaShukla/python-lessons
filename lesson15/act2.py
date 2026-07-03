with open('class_notes.txt', 'r') as f:
    for index, line in enumerate(f, start=1):
        words = line.split()
        print(f"Line - {index} : Count of words :{len(words)}")
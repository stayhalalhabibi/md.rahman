# Word, Line, Character Counter from File

filename = "sample.txt"

try:
    with open(filename, "r") as file:
        text = file.read()

        # Characters
        char_count = len(text)

        # Lines
        lines = text.splitlines()
        line_count = len(lines)

        # Words
        words = text.split()
        word_count = len(words)

        print("----- FILE ANALYSIS -----")
        print("Characters:", char_count)
        print("Lines:", line_count)
        print("Words:", word_count)

except FileNotFoundError:
    print("File not found! Please check filename.")
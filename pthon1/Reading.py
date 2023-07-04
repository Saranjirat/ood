print("*** Reading E-Book ***")
text,  Highlight = input("Text , Highlight : ").split(",")
highlighted_text = text.replace(Highlight, f"[{Highlight}]")
print(highlighted_text)



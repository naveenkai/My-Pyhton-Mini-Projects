from difflib import SequenceMatcher
text1 = "My Name is Naveen K"
text2 = "Hi, My Name is Naveen K"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")

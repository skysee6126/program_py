kor = ["사과", "바나나", "오렌지"]
eng = ["appple", "banana", "orange"]

print(list(zip(kor, eng)))

mixed = [('사과', 'appple'), ('바나나', 'banana'), ('오렌지', 'orange')]
print(list(zip(*mixed)))
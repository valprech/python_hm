sentence = input("Enter the sentence: ").split()
print(sentence)
for k, v in enumerate(sentence):
    print(f"{k+1} {v:.10}")
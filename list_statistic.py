n = int(input())
positives = []
negatives = []

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

negatives_sum = sum(negatives)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Count of negatives: {negatives_sum}")
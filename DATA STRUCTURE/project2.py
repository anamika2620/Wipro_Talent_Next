
# List of scores
scores = [2, 3, 6, 6, 5]

# Remove duplicate values using set
unique_scores = list(set(scores))

# Sort the list
unique_scores.sort()

# Runner-up score (second highest)
runner_up = unique_scores[-2]

# Print result
print("Scores:", scores)
print("Runner-up score:", runner_up)

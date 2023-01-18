def calculate_final_grade(scores):
    # weights for different assessments
    weights = {'exam': 0.6, 'quiz': 0.1, 'homework': 0.3}
    final_grade = 0
    for assessment, weight in weights.items():
        final_grade += scores[assessment] * weight
    return final_grade

# example usage
scores = {'exam': 88, 'quiz': 75, 'homework': 90}
final_grade = calculate_final_grade(scores)
print(final_grade)

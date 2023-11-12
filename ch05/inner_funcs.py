# 4 exer, 1 middle-exam, 1 final-exam
# 40%     30 %              30%

def calculate_grade(assignment_scores, mid_score, final_score):
    """Calculate the final grade"""

    def weighted_average():
        """Calculate the weighted average"""
        assignment_score = sum(assignment_scores) / len(assignment_scores)
        return (assignment_score * 0.4) + mid_score * 0.3 + final_score * 0.3

    def determine_grade(average):
        """Determine the letter grade based on the average score"""
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    average = weighted_average()
    grade = determine_grade(average)

    return average, grade

# Test the function
final_average, final_grade = calculate_grade([85, 90, 88], 92, 84)
print(f"The final grade is {final_grade} with average: {int(final_average)}")
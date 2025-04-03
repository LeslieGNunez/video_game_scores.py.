# Scores in a Video Game

# Define the scores array
scores = [1200, 1500, 1800, 1700, 1900]

# Display scores for each level
def display_scores(scores):
    print("Player's High Scores by Level:")
    for i, score in enumerate(scores):
        print(f"Level {i + 1}: {score} points")

# Calculate the average score
def average_score(scores):
    return sum(scores) / len(scores)

# Highlight the highest and lowest scores
def highest_score(scores):
    return max(scores)

def lowest_score(scores):
    return min(scores)

# Update score at a specific level
def update_score(scores, level, new_score):
    if 1 <= level <= len(scores):
        scores[level - 1] = new_score
        print(f"Updated: Level {level} now has {new_score} points.")
    else:
        print("Invalid level number.")

# Determine player rank based on total score
def determine_rank(scores): 
    total = sum(scores)
    if total >= 8000:
        return "Pro"
    else:
        return "Trash"

# Reward based on the highest score
def reward_player(scores):
    top = highest_score(scores)
    if top >= 2000:
        return "Reward Unlocked"
    else:
        return "No reward"

# Example usage
if __name__ == "__main__":
    display_scores(scores)
    print(f"Average Score: {average_score(scores):.2f}")
    print(f"Highest Score: {highest_score(scores)}")
    print(f"Lowest Score: {lowest_score(scores)}")
    update_score(scores, 3, 2100)  # Example update
    print(f"Player Rank: {determine_rank(scores)}")
    print(f"Reward Status: {reward_player(scores)}")

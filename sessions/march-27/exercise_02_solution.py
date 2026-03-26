# ============================================================
#  ZAS Python Working Group — Session 1, Exercise 2
#  SOLUTION
# ============================================================


# [DIFF 1] Assignment: Python uses = (not <-)

participant_count = 12
session_num = 1


# [DIFF 2] Logical values: Python uses True / False (not TRUE / FALSE)

is_recorded = True
has_video   = False


# [DIFF 3] Lists and indexing: Python uses [] (not c()), and indexing starts at 0

scores = [72, 85, 61, 90, 78]

first_score = scores[0]       # R: scores[1]
last_score  = scores[-1]      # R: scores[length(scores)]  — Python's -1 trick!


# [DIFF 4] Printing with f-strings (not paste/cat)

print(f"Participant count: {participant_count}")
print(f"Session: {session_num}")
print(f"Mean score: {sum(scores) / len(scores)}")

# Alternative using the statistics module:
# import statistics
# print(f"Mean score: {statistics.mean(scores)}")


# [DIFF 5] Functions: def + indentation (no curly braces, no <- function(...))

def normalise(x):
    mn = min(x)
    mx = max(x)
    return [(v - mn) / (mx - mn) for v in x]

normalised_scores = normalise(scores)
print(f"Normalised: {[round(v, 3) for v in normalised_scores]}")


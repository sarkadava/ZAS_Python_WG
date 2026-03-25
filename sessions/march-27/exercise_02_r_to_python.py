# ============================================================
#  ZAS Python Working Group — Session 1, Exercise 2
#
#  TASK: Below is a working R script.
#        Your job: rewrite it as a Python script.
#
#  Five things work differently in Python — they are each
#  marked with a [DIFF #N] comment. Study how R does it,
#  then figure out the Python equivalent.
#
#  A blank Python template is waiting for you at the bottom.
# ============================================================


# ============================================================
#  THE R SCRIPT  (read-only — just study it!)
# ============================================================

# --- [DIFF 1] Assignment operator -------------------------
#
# R:       x <- 42
# Python:  ???
#
# In R you assign with <-
# (= also works in R but <- is idiomatic)

# participant_count <- 12
# session_num <- 1


# --- [DIFF 2] Logical values ------------------------------
#
# R:       is_recorded <- TRUE
# Python:  ???
#
# R uses TRUE / FALSE (all caps).

# is_recorded <- TRUE
# has_video   <- FALSE


# --- [DIFF 3] Vectors / lists and indexing ----------------
#
# R:       scores <- c(72, 85, 61, 90, 78)
#          first  <- scores[1]          # index starts at 1!
#          last   <- scores[length(scores)]
#
# Python:  ???
#          first  <- ???                # index starts at 0!
#          last   <- ???
#
# Python lists use 0-based indexing.
# Python also has a neat trick for the last element.

# scores <- c(72, 85, 61, 90, 78)
# first_score <- scores[1]
# last_score  <- scores[length(scores)]


# --- [DIFF 4] String formatting / printing ----------------
#
# R:       cat(paste("Mean score:", mean(scores), "\n"))
# Python:  ???
#
# R uses paste() to glue strings together.
# Python has f-strings (formatted string literals) — much cleaner.

# cat(paste("Participant count:", participant_count, "\n"))
# cat(paste("Session:", session_num, "\n"))
# cat(paste("Mean score:", mean(scores), "\n"))


# --- [DIFF 5] Simple function definition ------------------
#
# R:
#   normalise <- function(x) {
#     (x - min(x)) / (max(x) - min(x))
#   }
#   normalised_scores <- normalise(scores)
#   cat(paste("Normalised:", normalised_scores, "\n"))
#
# Python:  ???
#
# Python uses def, no curly braces, indentation is everything.
# Inside the function, use a list comprehension or just arithmetic.

# normalise <- function(x) {
#   (x - min(x)) / (max(x) - min(x))
# }
# normalised_scores <- normalise(scores)
# cat(paste("Normalised:", normalised_scores, "\n"))


# ============================================================
#  YOUR PYTHON TRANSLATION — write your code below
# ============================================================

# [DIFF 1] Assignment — translate:
#   participant_count <- 12
#   session_num <- 1



# [DIFF 2] Logical values — translate:
#   is_recorded <- TRUE
#   has_video   <- FALSE



# [DIFF 3] List + indexing — translate:
#   scores <- c(72, 85, 61, 90, 78)
#   first_score <- scores[1]
#   last_score  <- scores[length(scores)]



# [DIFF 4] Print with f-string — translate:
#   cat(paste("Participant count:", participant_count, "\n"))
#   cat(paste("Session:", session_num, "\n"))
#   cat(paste("Mean score:", mean(scores), "\n"))
#
# Hint: Python's built-in sum() and len() can replace mean().
#       Or: import statistics; statistics.mean(scores)



# [DIFF 5] Define a function — translate:
#   normalise <- function(x) {
#     (x - min(x)) / (max(x) - min(x))
#   }
#   normalised_scores <- normalise(scores)
#   cat(paste("Normalised:", normalised_scores, "\n"))
#
# Hint: Python's built-in min() and max() work on lists.
#       For element-wise arithmetic, try a list comprehension:
#         [(v - mn) / (mx - mn) for v in x]



# ============================================================
#  EXPECTED OUTPUT (all five diffs working)
# ============================================================
#
#  Participant count: 12
#  Session: 1
#  Mean score: 77.2
#  Normalised: [0.379, 0.828, 0.0, 1.0, 0.586]   (approx)
#
# ============================================================
#  BONUS
#  -----
#  1. Add a 6th participant with score 95.
#     Print the updated mean.
#  2. Sort the scores list from highest to lowest and print it.
#     (Look up: sorted() with reverse=True)
# ============================================================

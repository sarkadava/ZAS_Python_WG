# ZAS Python Working Group — Session 1, Exercise 2
# Task: translate this R script into Python.

participant_count <- 12
session_num <- 1

is_recorded <- TRUE
has_video   <- FALSE

scores <- c(72, 85, 61, 90, 78)
first_score <- scores[1]
last_score  <- scores[length(scores)]

cat(paste("Participant count:", participant_count, "\n"))
cat(paste("Session:", session_num, "\n"))
cat(paste("Mean score:", mean(scores), "\n"))

normalise <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}

normalised_scores <- normalise(scores)
cat(paste("Normalised:", normalised_scores, "\n"))


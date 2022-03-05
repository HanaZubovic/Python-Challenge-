import os
import csv

vote_file_path = os.path.join("election_data.csv").replace("\\", "/")
print(vote_file_path)


with open(vote_file_path, "r") as vote_memory:
    vote_read = csv.reader(vote_memory, delimiter=',')
    next(vote_read)
    # The total number of votes cast
    votes = 0
    total_votes = 0
    voted_candidates = 0
    percent_votes_won = 0
    total_candidate_votes = 0
    pop_vote_winner = ""
    votes = {}

    for row in vote_read:
        total_votes += 1
        if row[2] in votes:
            votes[row[2]] += 1
        else:
            votes[row[2]] = 1
    print("Election Results")
    sep = "-------------------------"
    print(sep)
    print(f"Total Votes: {total_votes}\n{sep}")
    max_votes = -1
    best_candidate = ""

    for candidate in votes.keys():
        print(
            f"{candidate}: {round(100 * votes[candidate] / total_votes, 3)}% ({votes[candidate]})")
        if votes[candidate] > max_votes:
            max_votes = votes[candidate]
            best_candidate = candidate

    print(sep)
    print(f"Winner: {best_candidate}")
    print(sep)

#!bin/usr/env python3
import sys

class ScoreError(Exception):
    def __init__(self, name):
        super().__init__(self, name)
        self.name = name
    def __str__(self):
        return f"Invalid parameter: '{self.name}'"
    
def check_digit(score : str):
    if score.isdigit() == False:
        raise ScoreError(score)

def main():
    print("=== Player Score Analytics ===")
    argv_len = len(sys.argv)
    scores = [None] * (argv_len - 1)
    i = 0 #interate throught scores
    s = 1 #interate( throught argv
    for s in range (1, argv_len):
        try:
            check_digit(sys.argv[s])
        except ScoreError as e:
            print(f"{e}")
            pass    
        else:
            scores[i] = int(sys.argv[s])
            i += 1
            s += 1
    if len(scores) == 0 or scores[0] == None:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores)/len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
    
if __name__ == "__main__":
    main()
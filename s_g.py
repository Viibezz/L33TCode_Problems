import random
import json
import sys

#add attributes to the json or delete for all properties
def add_to_json():
    c = 0
    with open("properties.json", "r") as read_file:
        data = json.load(read_file)
    for property in data:
        c+=1
        # property['bruteforce'] = "-"
        # property['optimized'] = "-"
        # del property['time']
        # del property['space']
        # property['time'] = "bruteforce -> O(), optimized-> O()"
        # property["space"] = "bruteforce -> O(), optimized-> O()"
    print(c)
    with open("properties.json", "w") as read_file:
        json.dump(data, read_file) 
#Gets problem name from command line with whitespace characters
def name_helper(start, problem_name):
    name = ""
    for i in range(start, len(problem_name)):
        name += str(problem_name[i]) + " "
    return name

#Finds a random problem to test myself
def solve(problem, level = None, pattern = None):
    c = 0
    for p in problem:
        c += 1
    x = random.choice(problem)
    if level == 'any':
        level = None
    if pattern == "any":
        pattern = None
    if pattern and level:
        c = 0
        for p in problem:
            if p["level"] == level and p["pattern"] == pattern:
                c += 1
                print(p['title'])
        while True:
            x = random.choice(problem)
            if x["level"] == level and x["pattern"] == pattern:
                return x['title'] 
    elif pattern and not level:
        c = 0
        for p in problem:
            if p["pattern"] == pattern:
                c += 1
                print(p['title'])
        while x["pattern"] != pattern:
            x = random.choice(problem)
    elif level and not pattern:
        c = 0
        for p in problem:
            if p["level"] == level:
                c += 1
                print(p['title'])
        while x["level"] != level:
            x = random.choice(problem)
    else:
        return x['title'] + "\n\nTotal problems with this input: " + str(c)
    print("\n\nStart With:")
    return x['title'] + "\n\nTotal problems with this input: " + str(c)
        
# returns all info and properties of a problem
def info(problems, problem_name):
    for n in problems:
        if n["title"] == problem_name:
            return n
#gets command line arguments and starts test
def start():
    problems = json.load(open("properties.json","r"))
    if sys.argv[1] == "info" and len(sys.argv) == 2:
        problem_name = name_helper(2,sys.argv)
        print(info(problems, problem_name[:-1]))
    elif sys.argv[1] == "solve" and len(sys.argv) == 2:
        print(solve(problems))
    elif sys.argv[1] == "solve" and len(sys.argv) >= 4:
        pattern_name = name_helper(3, sys.argv)
        print(solve(problems, sys.argv[2], pattern_name[:-1]))
    else:
        print("s_g.py solve\ns_g.py solve level pattern\ns_g.py info problem name")


start()
#patterns
# Sorting        - checking
# Two Pointer    - checking
# Math Trick     - checking
# Binary Search  - not yet
# DFS            - not yet
# BFS            - not yet
# BackTracking   - not yet
# Graphs         - not yet

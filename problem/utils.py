from .models import Problem, Tag
from urllib.request import urlopen
import json

def get_data(url):
    try:
        response = urlopen(url)
        response_data = []
        response_data = json.loads(response.read())
        
        if response_data['status'] == 'OK':
            return response_data['result']
        else:
            return []

    except:
        return []


def get_problem_statistics(problemset):
    solve_count = {}
    for problem in problemset:
        contest_id = problem["contestId"]
        index = problem["index"]
        solve_count[str(contest_id) + index] = problem["solvedCount"]
    return solve_count


def get_problemset():
    print("Getting problemset...")

    URL = "https://codeforces.com/api/problemset.problems"

    Problem.objects.all().delete()

    data = get_data(URL)

    if data == [] or not "problems" in data:
        print("No data found")
        return

    print("Getting solve count...")
    solve_count = get_problem_statistics(data["problemStatistics"])
    print("Got solve count")

    problemset = data["problems"]

    for problem in problemset:
        if (problem["type"] != "PROGRAMMING" or not "rating" in problem or "*special" in problem["tags"]):
            continue
        
        contest_id = problem["contestId"]
        index = problem["index"]
        problem_obj = Problem(
            contest_id=contest_id,
            index=index,
            name=problem["name"],
            rating=problem["rating"],
            solve_count = solve_count[str(contest_id) + index],
        )

        problem_obj.save()

        for tag in set(problem["tags"]):
            try:
                tag_obj = Tag.objects.get(name=tag)
                problem_obj.tags.add(tag_obj)
            except:
                tag_obj = Tag(name=tag)
                tag_obj.save()
                problem_obj.tags.add(tag_obj)
        
    
    print("Got problemset")
from .models import Contest
from problem.utils import get_data

def get_contests():
    print("Getting contests...")

    URL = "https://codeforces.com/api/contest.list"

    Contest.objects.all().delete()

    data = get_data(URL)

    if data == [] or not "result" in data:
        print("No data found")
        return
    
    contest_list = data["result"]

    for contest in contest_list:
        if contest.phase != "FINISHED":
            continue
        
        contest_obj = Contest(
            contest_id = contest.id,
            contest_duration = contest.durationSeconds, 
            name = contest.name,
        )
    
        contest_obj.save()
    
    print("Got contests")
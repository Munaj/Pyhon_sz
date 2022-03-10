
projects = ["Brexit", "Nord Stream", "US Mexico Border"]
leaders = ["Theresa May", "Wladimir Putin", "Donald Trump and Bill Clinton"]

for proj, lead in zip(projects,leaders):
    print(f"The leader of {proj} is {lead}")

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

print("-"*30)

for proj, date, lead in zip(projects,dates,leaders):
    print(f"The leader of {proj} started {date} is {lead}")

print("-"*30)

for i, (proj, date, name) in enumerate(zip(projects,dates,leaders)):
    print(f"{i+1} - The leader of {proj} started {date} is {name}")

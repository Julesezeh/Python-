n=int(input())
students={}
for _ in range(n):
    name, *lips =input().split()
    marks = list(map(float,lips))
    students[name]=marks
query_name = input()
solution=sum(students[query_name])/len(students[query_name])
print(f"{solution:1.2f}")

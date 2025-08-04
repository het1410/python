marks = {
    "het" : 100,
    "patel" : 80,
    
}
#print(marks.items())
#print(marks.keys())
#print(marks.values())

marks.update({"het":99})
print(marks)

print(marks.get("het"))
print(marks.get("hp"))
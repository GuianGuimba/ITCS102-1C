months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

print(months)
for i in months:
    print(f"{i},2025")

months.reverse()
print(months)

#Difference between string and list
fullname = "Guian Esteebean A. Guimba"

newlist = list(fullname)
newlist.reverse()
print(newlist)

newlist.sort()
print(newlist)

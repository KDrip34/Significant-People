new_peoples  = {
'Coach Jon': ['Boxing coach from Koa Academy'],
'Eddie': ['Boxing coach from city sports whos started me off'],
'God':['The creator who has help me down with all the ups and downs with my life '],
'George' : ['One of the real ass homies I could relate too'],
}
for name, people in new_peoples.items():
	print("\n" + name.title() + "'s back story in my life is:")
	for people in people:
		print("\t" + people.title())
print("...")

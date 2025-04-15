ignoreCE = True
ignore_submission_after_AC = True
prettyTime = True

def timef(timei):
	if prettyTime == False:
		return timei
	mi = timei//60
	se = timei%60
	if se<10:
		se = "0{0}".format(se)
	if mi>=60:
		ho = mi//60
		mi = mi%60
		if mi<10:
			mi = "0{0}".format(mi)
		return "{0}:{1}:{2}".format(ho,mi,se)
	return "{0}:{1}".format(mi,se)

import sys

argv = sys.argv

if len(argv) == 1:
	print("Use main.py [file]")
	sys.exit()

fileName = argv[1]
file = open(fileName, "r", encoding="utf-8")

filecon = file.readlines()
if filecon[0][0] != '@':
	del filecon[0]

file.close()

standing = {}
memberstatus = {}
memberstatusz = {}
problems = []
problemsinfo = []
inited = {}
fs = []
firsts = {}

for line in filecon:
	linelist = line.split(" ",maxsplit=1)
	type = linelist[0]
	content = linelist[1].rstrip()
	if type == "@contest":
		print("{0}\n".format(content))
	if type == "@p":
		scontentp = content.split(",",maxsplit=1)
		scontentp[1] = scontentp[1][::-1]
		scontentb = scontentp[1].split(",",maxsplit=2)
		scontent = [scontentp[0], scontentb[-1][::-1]]
		problems.append(scontent[0])
		problemsinfo.append({"name":scontent[1],"time":-1})
		firsts[len(problems)-1] = False
	if type == "@t":
		scontent = content.split(",",maxsplit=3)
		standing[scontent[0]] = scontent[3]
		inited[scontent[3]] = False
	if type == "@s":
		scontent = content.split(",")
		sname = standing[scontent[0]]
		sprob = scontent[1]
		stried = scontent[2]
		stime = scontent[3]
		sstatus = scontent[4]
		sprobid = problems.index(sprob)

		if inited[sname]==False:
			inited[sname] = True
			memberstatus[sname] = []
			memberstatusz[sname] = {"count": 0, "time": 0}
			for i in range(len(problems)):
				memberstatus[sname].append({"time": 0, "tried": 0, "pass": False})
		if ignoreCE and sstatus == "CE":
			continue
		if ignore_submission_after_AC and memberstatus[sname][sprobid]["pass"]:
			continue
		memberstatus[sname][sprobid]["time"] += int(stime)
		memberstatusz[sname]["time"] += int(stime)
		memberstatus[sname][sprobid]["tried"] += 1
		if sstatus == "OK":
			if firsts[sprobid] == False:
				firsts[sprobid] = sname
				problemsinfo[sprobid]["time"] = int(stime)
			if memberstatus[sname][sprobid]["pass"] == False:
				memberstatusz[sname]["count"] += 1
			memberstatus[sname][sprobid]["pass"] = True

# print(memberstatus["cyhyeee"][0]["pass"]) # cyhyeee A status
# print(memberstatusz["zhenghaoming"]["time"])

# print(memberstatusz)

for name, value in memberstatusz.items():
	count = value["count"]
	time = value["time"]
	if len(fs) == 0:
		fs.append(name)
		continue
	added = False
	for cnameid in range(len(fs)):
		cname = fs[cnameid]
		if count > memberstatusz[cname]["count"]:
			fs.insert(cnameid, name)
			added = True
			break
		if count == memberstatusz[cname]["count"] and time < memberstatusz[cname]["time"]:
			fs.insert(cnameid, name)
			added = True
			break
	if added == False:
		fs.append(name)

# print(fs)

for nameid in range(len(fs)):
	name = fs[nameid]
	print("{0}.{1} ".format(nameid+1,name),end="")
	for i in range(len(problems)):
		if memberstatus[name][i]["tried"] == 0:
			print("{0} ".format(problems[i]),end="")
			continue
		info = ""
		if memberstatus[name][i]["pass"] == True:
			info = "+"
			if memberstatus[name][i]["tried"] > 1:
				info = "+{0}".format(memberstatus[name][i]["tried"]-1)
		else:
			info = "-{0}".format(memberstatus[name][i]["tried"])
		print("{0}:{1}({2}) ".format(problems[i],info,timef(memberstatus[name][i]["time"])),end="")
	print("| {0}({1})".format(memberstatusz[name]["count"],timef(memberstatusz[name]["time"])))

print()

for i in range(len(problems)):
	print("{0} [{1}]: ".format(problems[i],problemsinfo[i]["name"]),end="")
	info = ""
	if firsts[i] != False:
		info = "{0}({1})".format(firsts[i],timef(problemsinfo[i]["time"]))
	print("{0}".format(info))

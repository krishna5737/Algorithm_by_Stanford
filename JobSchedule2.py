with open("jobs.txt", 'r') as fileObj:
        lines = fileObj.readlines()
        numJobs = int(lines[0].strip())
        jobList = [(int(line.split()[0]),int(line.split()[1])) for line in lines[1:] ] 
        
JobList = [ (w, l, (w/float(l))) for w, l in jobList ]
JobList.sort(key=lambda x: x[0], reverse=True)   
JobList.sort(key=lambda x: x[2], reverse=True)   

ls = 0
ws = 0
for job in JobList:
    ls += job[1]
    ws += job[0] * ls

print(ws)

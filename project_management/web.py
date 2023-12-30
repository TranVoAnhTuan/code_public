from manager import *
from member import *
from position import *
from project import *
from task import *

#create project
p1 = Project()
# create position
po1 = Position()
po1.setPosition('Manager')
po1.setProject(p1)

po2 = Position()
po2.setPosition('Programmer')
po2.setProject(p1)

# create manager
m1 = Manager()

# create
task1 = Task()
task1.setID('101')
task1.setName('find knowledge')
task1.setStartTime(5, 9, 2023)
task1.setDeadline(20, 11, 2023)
task1.setProject(p1)
p1.addTask(task1)

task2 = Task()
task2.setID('102')
task2.setName('Choose domain and hosting')
task2.setStartTime(6, 9, 2023)
task2.setDeadline(20, 11, 2023)
task2.setProject(p1)
p1.addTask(task2)

task3 = Task()
task3.setID('103')
task3.setName('Install CMS')
task3.setStartTime(7, 9, 2023)
task3.setDeadline(20, 11, 2023)
task3.setProject(p1)
p1.addTask(task3)

task4 = Task()
task4.setID('104')
task4.setName('Design the interface')
task4.setStartTime(8, 9, 2023)
task4.setDeadline(20, 11, 2023)
task4.setProject(p1)
p1.addTask(task4)

task5 = Task()
task5.setID('105')
task5.setName('Add content')
task5.setStartTime(9, 9, 2023)
task5.setDeadline(20, 11, 2023)
task5.setProject(p1)
p1.addTask(task5)

task6 = Task()
task6.setID('106')
task6.setName('Optimize SEO')
task6.setStartTime(10, 9, 2023)
task6.setDeadline(20, 11, 2023)
task6.setProject(p1)
p1.addTask(task6)

task7 = Task()
task7.setID('107')
task7.setName('Integrate features')
task7.setStartTime(11, 9, 2023)
task7.setDeadline(20, 11, 2023)
task7.setProject(p1)
p1.addTask(task7)

task8 = Task()
task8.setID('108')
task8.setName('Test and debug')
task8.setStartTime(12, 9, 2023)
task8.setDeadline(20, 11, 2023)
task8.setProject(p1)
p1.addTask(task8)

task9 = Task()
task9.setID('109')
task9.setName('Maintain and update')
task9.setStartTime(13, 9, 2023)
task9.setDeadline(20, 11, 2023)
task9.setProject(p1)
p1.addTask(task9)

task10 = Task()
task10.setID('110')
task10.setName('Secure the website')
task10.setStartTime(14, 9, 2023)
task10.setDeadline(20, 11, 2023)
task10.setProject(p1)
p1.addTask(task10)

task11 = Task()
task11.setID('111')
task11.setName('Promote the website')
task11.setStartTime(15, 9, 2023)
task11.setDeadline(20, 11, 2023)
task11.setProject(p1)
p1.addTask(task11)

task12 = Task()
task12.setID('112')
task12.setName('Analyze website traffic')
task12.setStartTime(16, 9, 2023)
task12.setDeadline(20, 11, 2023)
task12.setProject(p1)
p1.addTask(task12)


task13 = Task()
task13.setID('113')
task13.setName('Gather user feedback')
task13.setStartTime(17, 9, 2023)
task13.setDeadline(20, 11, 2023)
task13.setProject(p1)
p1.addTask(task13)

task14 = Task()
task14.setID('114')
task14.setName('Optimize the website for mobile devices')
task14.setStartTime(18, 9, 2023)
task14.setDeadline(20, 11, 2023)
task14.setProject(p1)
p1.addTask(task14)

task15 = Task()
task15.setID('115')
task15.setName("Measure the website's success")
task15.setStartTime(19, 9, 2023)
task15.setDeadline(20, 11, 2023)
task15.setProject(p1)
p1.addTask(task15)

#create member
member1 = Member()
member1.setID('001')
member1.setName('Jack Tran')

member2 = Member()
member2.setID('002')
member2.setName('Bao')

member3 = Member()
member3.setID('003')
member3.setName('Thang')

# add Member
p1.addMember(member1, po1)
p1.addMember(member2, po2)
p1.addMember(member3, po2)

p1.setManager(m1, member1)

# assign
m1.assign(member1, task1)
m1.assign(member1, task2)
m1.assign(member1, task3)
m1.assign(member1, task4)
m1.assign(member1, task5)

m1.assign(member2, task6)
m1.assign(member2, task7)
m1.assign(member2, task8)
m1.assign(member2, task9)
m1.assign(member2, task10)


m1.assign(member3, task11)
m1.assign(member3, task12)
m1.assign(member3, task13)
m1.assign(member3, task14)
m1.assign(member3, task15)

# mark completed
m1.markCompleted(task1)
m1.markCompleted(task2)
m1.markCompleted(task6)
m1.markCompleted(task7)
m1.markCompleted(task11)

# mean
m1.trackProgress()

print(member1.getTask())
print(member1.getWarning())

print(p1.getMeanTime())





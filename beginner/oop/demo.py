from beginner.oop.student import Student

print()
sd = Student('mawenhao', 100)
sd_methods = dir(sd)
print('Student总计%d个属性和方法' % len(sd_methods))
for sd_method in sd_methods:
    print(sd_method)

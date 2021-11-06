# standard normal distribution or standardization
marks=[75,82,71,92,48,75,97,59,62,75,82,78,66,76,71]
new_marks=[]
mean=74
sd=11
for i in range(len(marks)):  
    m=(marks[i]-mean)/sd 
    new_marks.append(m)
new_mean=round(sum(new_marks)/len(new_marks))
print(new_mean)

# calculating variance
sum=0
for i in range(len(new_marks)): 
    sum+=(new_marks[i]-new_mean)**2

new_var=sum/len(new_marks)
new_sd=round(new_var**0.5)
print(new_sd)
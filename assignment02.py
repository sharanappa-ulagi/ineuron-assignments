# Question 01
n=5
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')
	
# Question 02
in_word=input("Input word: ")
out_word=""
for i in in_word:
    out_word=i+out_word
print("Output:",out_word)



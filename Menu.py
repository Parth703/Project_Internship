#A- Palindrome
def palindrome(n):
	for i in range(int(len(n)/2)):
		if n[i] != n[len(n)-i-1]:
			return False
	return True
	
#B- Fibonacci
def fib(x):
	if x < 0:
		print("Positive Numbers only")
	if x <= 1:                         #This will recursively check for numbers till
		return x                       #it gets to 0 and then will fill the blanks back
	return fib(x-1) + fib(x-2)         #upto the entered number.
#C- Leap Year check
def leap_year(year):
	if year%4 == 0 and year%100 != 0:
		print(year, "is a Leap Year")
	elif year%100 == 0:
		print(year, "is not a Leap Year")
	elif year%400 == 0:
		print(year, "is a Leap Year")
	else:
		print(year, "is not a Leap Year")
#D- Random Password Generator
def rgp(user_words, required_length, no_of_passwords):
	import random 
	generated_password = ""
	for n in range(no_of_passwords):
		generated_password = ""
		for i in range(required_length):
			g = random.randrange(len(user_words))
			generated_password += user_words[g]
		print("Password", n+1, "is:", generated_password)

while True:
	m = input("\nMenu: \n1-Palindrome \n2-Fibonacci Series \n3-Year is Leap or Not \n4-Random Password Generator\n5-Quiz\nTo Exit Enter: 0\nChoose your option in 1 to 5: ") 
	if m == "0":
		break
	elif m == "1":
		print("Program to check if a number or string is a Palindrome")
		n = input("Enter Number or String: ")
		p = palindrome(n)
		if p :
			print("It is a Palindrome!")
		else:
			print("It is not a Palindrome!")
	elif m == "2":
		n = input("Provide a Number: ")
		n1 = int(n)
		for a in range(n1 + 1):
			print(fib(a), end=" ")
	elif m == "3":
		print("Program to Check if Year is a Leap Year")
		year = int(input("Enter Year: "))
		ly = leap_year(year)
	elif m == "4":
		user_words = []
		user_words = input("Enter any word: ")
		required_length = int(input("Length of password you require: "))
		no_of_passwords = int(input("How many passwords do you require: "))
		r = rgp(user_words, required_length, no_of_passwords)
	elif m == "5":
		print("WELCOME TO THE SMALL QUIZ COMPETETION")
		name = input('Enter Your Name: ')
		print("Game's Rules:\n 1.There will be 10 questions.\n 2.Each question will have 4 options.\n 3.You have to select your answer from them by pressing 1,2,3 or 4.\n 4.Four points will be given for right answer and zero for wrong answer.\n ")
		print("Lets Proceed :")
		count_marks = 0
		correct_count = 0
		print("Q1.Who invented zero ?\n 1.Aryabhatta\n 2.Brhmagupta\n 3.Bauddhyana\n 4.Pingala")
		n = int(input('Select your answer = '))
		if n == 2 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 2 and n <5 and n>0:
			print("Your answer is wrong. Correct answer is Brahmagupta.\n")
		else:
			print("You have chosen invalid option")

		print("Q2.What is the national flower of India ?\n 1.Lotus\n 2.Lily\n 3.Sunflower\n 4.Rose")
		n = int(input('Select your answer = '))
		if n == 1 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 1 and n <5 and n>0:
			print("Your answer is wrong. Correct answer is Lotus.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q3.Who first described the Gravitation mathematically ?\n 1.Brahmagupta\n 2.Galilleo\n 3.Newton\n 4.Keplar")
		n = int(input('Select your answer = '))
		if n == 3 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 3 and n <5 and n>0:
			print("Your answer is wrong.Correct answer is Newton.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q4.Which is the smallest country in the world ?\n 1.Cuba\n 2.Jamaica\n 3.Vatican city\n 4.Albenia")
		n = int(input('Select your answer = '))
		if n == 3 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 3 and n <5 and n>0:
			print("Your answer is wrong. Correct answer is Vatican City.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q5.What is the national anthem of India ?\n 1.Jana Gana Mana\n 2.Bande Mataram\n 3. Saare Jahan Se Accha\n 4.Subh Sukh Chan")
		n = int(input('Select your answer = '))
		if n == 1 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 1 and n <5 and n>0:
			print("Your answer is wrong. Correct answer is Jana Gana Mana.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q6.Who invented radio ?\n 1.Markoni\n 2.Tesla\n 3. Edison\n 4.J.C. Bose")
		n = int(input('Select your answer = '))
		if n == 4 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 4 and n <5 and n>0:
			print("Your answer is wrong.Correct answer is J.C. Bose.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q7.Who showed that Electric and Magnetic force are two differnt forms of the same aspect ?\n 1.Coulomb\n 2.Faradey\n 3.Gauss\n 4.Maxwell")
		n = int(input('Select your answer = '))
		if n == 4 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 4 and n <5 and n>0:
			print("Your answer is wrong. Correct answer is Maxwell.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q8.Who figured out how Gravity works between two bodies ?\n 1.Max Planck\n 2.Rutherford\n 3.Albert Einstein\n 4.Newton")
		n = int(input('Select your answer = '))
		if n == 3 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 3 and n <5 and n>0:
			print("Your answer is wrong.Correct answer is Albert Einstein.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q9.Who invented Matrix Mechanics ?\n 1.Bohr\n 2.Heisenberg\n 3.Schrodinger\n 4.Dirac")
		n = int(input('Select your answer = '))
		if n == 2 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 2 and n <5 and n>0:
			print("Your answer is wrong. Correct answer is Heisenberg.\n")
		else:
			print("You have chosen invalid option\n")

		print("Q10.Who first came up with the idea of quantum computing ?\n 1.Paul Benioff\n 2.Von Neuman\n 3.Richard Feynman\n 4.Alan Turing")
		n = int(input('Select your answer = '))
		if n == 1 :
			count_marks = count_marks + 4
			correct_count += 1
			print("Absolutely right answer\n")
		elif n != 1 and n <5 and n>0:
			print("Your answer is wrong. Correct answer is Paul Benioff.\n")
		else:
			print("You have chosen invalid option\n")

		print(name, ",", correct_count, "out of 10 questions are correct.")
		print("You have scored",count_marks, "out of 40")
                        
		print("The quiz is over.\n")
		print("Thank your very much for perticipating.\n Have a good day.\n")
	else:
		print("Invalid Choice")

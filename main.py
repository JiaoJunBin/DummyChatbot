import math

def main():
	num = input("Find all factors of : ")

	print_factor(int(num))

def print_factor(x):
	s = set()
	mid = math.ceil(math.sqrt(x))

	for i in range(1,mid):
		if(x%i==0):
			s.add(i)
			s.add(int(x/i))

	l = list(s)
	l.sort()
	print(l)

if __name__ == '__main__':
	main()

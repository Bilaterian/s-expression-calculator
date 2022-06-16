How to run:
python calc.py 123

this program expects an argument after calc.py

it can accept integers such as:
	calc.py 123

or basic arithmetic:
	calc.py "(add 123 456)"

also allows for recursive strings:
	calc.py "(add (multiply 2 2) 40)"
	calc.py "(add (add 3 5) (multiply 9 9))"

so far it can handle the "add" and "multiply" operations
import sys
import os

# print(sys.argv[0]+",\t"+sys.argv[1])

# operators = []

# block sample:(a,b) '''
# 	expressions
# 	return 0;
# 	'''


# ## notes

# # motive
# close to natural language .
# everything is a block .
# every block is mutually exclusive
# block can work on variables inside it 

# # syntax 
# close to natural language .
# terminate a line with " ."
# " "(space) is the seperator
# process is done on block

# block(a,b)+block()

# process with a b c .
# 1+process with a b c .

# add process with a b c and 12 then subtract with 30 then multiply with 10 then divide by 5 then divide with 2 in t .

# add 2 and 3 then put in k .

# operator_blocks = ['add','subtract','multiply','divide','remainder']


# define block test with a,b,c .
# start block .
# 	add process with a,b,c and 12 and 5 then subtract 30 then multiply 10 then divide by 5 then divide 2 put in t .
# 	add 12 and 5 and 3 then subtract 20 then multiply 5 then divide 2 put in t .
# end block .

# define a is 10 .
# define b is 20 as shared .

# 14+5-7*5/2

import re
s = "add 12 and 5 and 3 then subtract 20 then multiply 5 then divide 2 put in t ."

class WordBlueprint:
	WordType = None
	Words = []
	WhatToExpectNext = None

	def __class__(self):
		return "WordBlueprint"

	def __init__(self,wordtype=None,words=[],what_to_expect_next=None):
		self.WordType = wordtype
		self.Words = words
		self.WhatToExpectNext = what_to_expect_next

		try:
			if what_to_expect_next.__str__() == "WordBlueprint":
				self.WhatToExpectNext = what_to_expect_next
			else:
				raise AttributeError("'what_to_expect_next' argument should be a instance of WordBlueprint .")
		except AttributeError as ae:
			print(str(ae))


# create type of Words
operators = WordBlueprint("operator",tuple(['add','subtract','multiply','divide']),"")
pipeliner = WordBlueprint("pipeliner",tuple(["then"]),"")
block_argument_separator = WordBlueprint("block-argument-separator",tuple([","]),"")
expression_argument_separator = WordBlueprint("expression-argument-separator",tuple(["and"]),"")

class ExpressionParserBlueprint:

	def __init_(self):
		pass

	def expression_parser(self,expression):
		words = re.split(r'\s+',str(expression))
		try:
			for word in words:
				if word in operators:
					#operator is encountered
					pass
				elif word in pipeliner:
					pass
				elif word in argument_separator:
					pass
				elif word in expression_argument_separator:
					pass
				else:
					#unrecognized template
					pass
		except Exception as e:
			print(e)
		return words


# # assumption for start
# syntax is correct .
# time-optimization does not matter right now .

# 1. detect variables

# parser code
# def tree_parser(expression):
# 	14+3*6/5
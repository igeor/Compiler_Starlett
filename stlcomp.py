

import sys
from difflib import SequenceMatcher
try:
	if ((len(sys.argv) != 2 )):
		print("Wrong format. Expected: py/python lexsyn.py filename.stl")
		exit()
	else:
	    with open(sys.argv[1], 'r') as file:
	        contents = file.read()     
except OSError as e:
    print(".stl file not found")
    exit()

programtk="program"
endprogramtk="endprogram"
iftk="if"
thentk="then"
elsetk="else"
endiftk="endif"
dowhiletk="dowhile"
enddowhiletk="enddowhile"
whiletk="while"
endwhiletk="endwhile"
endlooptk="endloop"
looptk="loop"
exittk="exit"
forcasetk="forecase"
endforcasetk="endforcase"
incasetk="incase"
endincasetk="endincase"
whentk="when"
endwhentk="endwhen"
defaulttk="default"
enddefaulttk="enddefault"
functiontk="function"
endfunctiontk="endfunction"
returntk="return"
intk="in"
inouttk="inout"
inandouttk="inandout"
andtk="and"
ortk="or"
nottk="not"
inputtk="input"
printtk="print"
idtk="idtk"
declaretk="declare"

# STATES
state0=0 
state1=1
state2=2
state3=3
state4=4
state5=5
state6=6
state7=7
state8=8
state9=9

Error = -1
OK  = -2
OK2 = -3
OK3 = -4
OK4 = -5
OK5 = -6

array=[[state0,state1,state2,state3,state4,state5,state6,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK],
	   [OK,state1,state1,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK],
	   [OK,OK,state2,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK],
	   [OK,OK,OK,OK,OK2,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK3,OK,OK],
	   [OK,OK,OK,OK,Error,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK,OK4,OK,OK],
	   [OK,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error,OK5,Error,Error],
	   [OK,OK,OK,Error,Error,Error,state9,state7,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error],
	   [state7,state7,state7,state7,state7,state7,state7,state8,state7,state7,state7,state7,state7,state7,state7,state7,state7,state7],
	   [Error,Error,Error,Error,Error,Error,state0,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error,Error],
	   [state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9,state9]
	   ]

# NEWSYMBOL
def newSymbol(input):
	if(input==" " or input=="\t" or input=="\n"):
		return 0
	elif(input.isalpha()):
		return 1
	elif(input.isdigit()):
		return 2
	elif(input=="<"):
		return 3
	elif(input==">"):
		return 4
	elif(input==":"):
		return 5
	elif(input=="/"):
		return 6
	elif(input=="*"):
		return 7
	elif(input==","):
		return 8
	elif(input==";"):
		return 9
	elif(input==")"):
		return 10
	elif(input=="("):
		return 11
	elif(input==""):
		return 12
	elif(input=="+"):
		return 13
	elif(input=="-"):
		return 14
	elif(input=="="):
		return 15
	else:
		return 16

# lexical analysis, it returns a lectical unit, every time it has been called

def lex():
	global tokentk
	global token
	global line

	tokentk=""
	token=""
	flag=0
	flag2=0	
	state=state0
	Buffer=""

	while(state!=OK and state!=Error and state!=OK2 and state!=OK3 and state!=OK4 and state!=OK5):
		input=file.read(1)

		if(state==state0 and input=="\n"):
			line=line+1
		state=array[state][newSymbol(input)]

		if(state==state8):
			Buffer=""
		if(state==state9 and input=="\n"):
			line=line+1
			Buffer=""
			state=state0
			
		
		if(state==state1 or state==state2):
			Buffer=Buffer+input
			flag=1

		if(state==OK):
			
			if(flag==1):
				token=token+Buffer
				file.seek(file.tell() - 1, 0)


			else:
				if(flag2==1):
					token=Buffer
					if(newSymbol(input)==1 or newSymbol(input)==2):
					 	file.seek(file.tell() - 1, 0)		
				else:
				    token=input	

		if(state==state3 or state==state4 or state==state5 or state==state6):
			Buffer=Buffer+input
			flag2=1

		if(state==OK2 or state==OK3 or state==OK4 or state==OK5):
			token=Buffer+input

		if(state==Error):
			print("Syntax error at line (",line,")")
			exit(0)
	
	
	if(token==programtk) : tokentk="programtk"
	elif(token==endprogramtk) : tokentk="endprogramtk"	
	elif(token==iftk) : tokentk="iftk"
	elif(token==thentk) : tokentk="thentk"
	elif(token==elsetk) : tokentk="elsetk"
	elif(token==endiftk) : tokentk="endiftk"
	elif(token==dowhiletk) : tokentk="dowhiletk"
	elif(token==enddowhiletk) : tokentk="enddowhiletk"
	elif(token==whiletk) : tokentk="whiletk"
	elif(token==endwhiletk) : tokentk="endwhiletk"
	elif(token==endlooptk) : tokentk="endlooptk"
	elif(token==exittk) : tokentk="exittk"
	elif(token==forcasetk) : tokentk="forcasetk"
	elif(token==exittk) : tokentk="exittk"
	elif(token==forcasetk) : tokentk="forcasetk"	
	elif(token==endforcasetk) : tokentk="endforcasetk"
	elif(token==incasetk) : tokentk="incasetk"
	elif(token==endincasetk) : tokentk="endincasetk"
	elif(token==whentk) : tokentk="whentk"
	elif(token==endwhentk) : tokentk="endwhentk"
	elif(token==defaulttk) : tokentk="defaulttk"
	elif(token==enddefaulttk) : tokentk="enddefaulttk"
	elif(token==functiontk) : tokentk="functiontk"
	elif(token==endfunctiontk) : tokentk="endfunctiontk"
	elif(token==returntk) : tokentk="returntk"
	elif(token==intk) : tokentk="intk"
	elif(token==inouttk) : tokentk="inouttk"
	elif(token==inandouttk) : tokentk="inandouttk"
	elif(token==andtk) : tokentk="andtk"
	elif(token==ortk) : tokentk="ortk"
	elif(token==nottk) : tokentk="nottk"
	elif(token==inputtk) : tokentk="inputtk"
	elif(token==printtk) : tokentk="printtk"
	elif(token==declaretk) : tokentk="declaretk"
	else : 
		if(token!=""):
			if(token[0].isalpha()) : tokentk="idtk"
			else : tokentk=""

#this is a function that handles the errors
def error_comp(err_flag) :

	if(err_flag==programtk) : 
		if(similarity(programtk)>0.7) :
			print("Error at line (",line,"): Expected <"+programtk+">.") 
			exit()
	if(err_flag==idtk) :
		print("Error at line (",line,"): Using a reserved or invalid word.")
		exit()
	if(err_flag=="ProgramID") :
		print(programid)
		print("Error at line (",line,"): Program ID is invalid.") 
		exit()
	if(err_flag==endprogramtk or err_flag==endfunctiontk or err_flag==endiftk or err_flag==endwhiletk or \
		err_flag==enddowhiletk or err_flag==endlooptk or err_flag==endforcasetk or err_flag==defaulttk or \
		err_flag==enddefaulttk or err_flag==endincasetk) :
			if(similarity(err_flag)>0.7) :
				print("Error at line (",line,"): Expected <"+err_flag+">.") 
				exit()
			else :
				print("Error at line (",line,"): Expected <;> between statements.")
				exit()
	if(err_flag=="VarSyntErr") :
		print("Error at line (",line,"): A syntax Error occurred when declaring the variables.") 
		exit()
	if(err_flag=="DeclVar"):
		if(check_statements(token)) :
			print("Error at line (",line,"):  <;> missing from declaration.")
			exit()	
		else :
			print("Error at line (",line,"): Variables aren't separated by the character <,>.")  
			exit()
	if(err_flag=="FuncForm"):
		print("Error at line (",line,"): Wrong form of the function.")
		exit()
	if(err_flag=="FuncArgs") :
		print("Error at line (",line,"): Missing <,> between parameters or missing (in/inout/inandout).") 
		exit()
	if(err_flag=="AssStatMiss") :
		print("Error at line (",line-1,"): Unexpected <;> after statement.") 
		exit()
	if(err_flag=="BlockErr") :
		if(tokentk==idtk) :
			error_comp(idtk)
		else:
			error_comp("BlockErr")
	if(err_flag=="AssStatErr") :
		print("Error at line (",line,"): Invalid expression.") 
		exit()
	if(err_flag=="CondErr1") :
		print("Error at line (",line,"): Missing <()> from condition.") 
		exit()
	if(err_flag=="IfErr1") :
		print("Error at line (",line,"): Expected <then> at if statement.")
		exit()
	if(err_flag=="WhenStatErr") :
		print("Error at line (",line,"): Expected <:> at statement.") 
		exit()
	if(err_flag=="ParErr") :
		print("Error at line (",line,"): Expected <,> between parameters.")
		exit()
	if(err_flag=="CondErr2") :
		print("Error at line (",line,"): Missing <[]> from condition.") 
		exit()
	if(err_flag=="ExpErr1") :
		print("Error at line (",line,"): Missing <()> from expression.") 
		exit()
	if(err_flag=="DeclErr"):
		print("Error at line (",line,"): Variable not declared in the scope.") 
		exit()
	if(err_flag=="FuncArgsErr"):
		print("Error at line (",line,"): Parameter passing is incorrect.") 
		exit()
	if(err_flag=="FuncErr"):
		print("Error at line (",line,"): Function not declared in the scope") 
		exit()
	if(err_flag=="RetErr"):
		print("Error at line (",line,"): Function block requires return statement.") 
		exit()
	if(err_flag=="RetErr2"):
		print("Error at line (",line,"): Return statements must not exist in program block.") 
		exit()
	if(err_flag=="exitErr"):
		print("Error at line (",line,"): Exit statement out of loop statement.") 
		exit()	



def check_statements(this_token): 
	stats = ["if","else","while","dowhile","loop","exit","forcase","incase","return","input","print"]
	if this_token in stats:
		return True
	return False

# PROGRAM
def program():
	global scopeList
	global scopesToString
	global programOffset
	global programFrameLength
	global programStartQuad

	lex()

	if (token == programtk) :

		programscope = new_scope(programid)

		blockID=token
		lex()
		if(token == programid) :

			lex()

			block_return_stat=[False]
			block(programid,block_return_stat)
			if(block_return_stat==[True]):
				error_comp("RetErr2")
			if(token == endprogramtk) :
				#programscope.printScope()
				programOffset=programscope.getOffset()
				programFrameLength=programscope.getFrameLength()
				programStartQuad=programscope.getStartQuad()
				#append_c_file()
				finalCodeGeneration(programFrameLength,programStartQuad)
				delete_scope()
				return True
			else :

				error_comp(endprogramtk)
		else :
			error_comp("ProgramID")
	else :
		error_comp(programtk)
		
# BLOCK
def block(blockID,ret):

	declarations()
	subprograms()
	genquad("begin_block",blockID,"__","__")	
	scopeList[-1].setStartQuad(nextquad())
	statements([],ret)
	if(blockID==programid):
		genquad("halt","__","__","__")
	genquad("end_block",blockID,"__","__")

# DECLARATIONS
def declarations():
	while(token == declaretk) :
		lex()
		varlist()

# VARLIST
def varlist() :
	var_read = False
	if(token == ";") : 
		lex()
		return True
	while True :
		if(token == ";" and var_read == True) : 
			lex()
			return True
		if(token == "," and var_read == False) :
			error_comp("VarSyntErr")	
		if(token == "," and var_read == True) :
			lex()
			var_read = False	
		if(token != "," and var_read == True) :
			error_comp("DeclVar")
		if(token != "," and tokentk != ";" and var_read == False) :
			if(tokentk == idtk):
				var_read = True
				new_variable_entity(token)		
				lex()
			else : 

				error_comp(idtk)
	
# SUBPROGRAMS
def subprograms() :

	global scopeLevel
	while(subprogram()) :
		True
	
def subprogram():	
	if(token == functiontk) :
		lex()
		blockID=token

		function_entity=new_function_entity(blockID)
		functionScope=new_scope(token) # we found function as Entity. We need to create new Scope

		if(tokentk==idtk) : 
			lex()
			funcbody(blockID)
			if(token == endfunctiontk) :
				lex()
				framelength=functionScope.getFrameLength()
				function_entity.initFucntion(framelength,functionScope.getStartQuad())
				#functionScope.printScope() # print scope before delete
				# edo tha ginei i paragogi tou telikou kodika
				finalCodeGeneration(framelength,functionScope.getStartQuad())
				
				delete_scope()			
				return True
			else :
				error_comp(endfunctiontk)
		else :

			error_comp(idtk)
	else :
		return False

# FUNCBODY
def funcbody(blockID) :
	formalpars()
	block_return_stat=[False]
	block(blockID,block_return_stat)
	if(block_return_stat==[False]):
		error_comp("RetErr")

# FORMALPARS
def formalpars() :
	if(token == "(") :
		lex()
		formalparlist()
		if(token==")") :
			lex()
		else :
			error_comp("FuncForm")
	else :
		error_comp("FuncForm")

# FORMALPARLIST
def formalparlist() :
	if(token == ")") :
		return True
	while(formalparitem()) : 
		if(token == ",") :
			lex()
		else :
			if(token == ")") :
				return True
			else :
				error_comp("FuncArgs")
				
# FORMALPARITEM
def formalparitem() :
	param_type=token
	if(token == inouttk or token == inandouttk or token == intk) :
		lex()
		if(tokentk == idtk) :
			#startcode
			newEntity=entity(token)
			offset=scopeList[-1].getOffset()
			if(param_type==intk):
				newEntity.initParameter("cv",offset)
				newArgument=argument("cv")
				scopeList[-2].getLastEntity().appendArgument(newArgument)
			elif(param_type==inandouttk):
				newEntity.initParameter("cp",offset)
				newArgument=argument("cp")
				scopeList[-2].getLastEntity().appendArgument(newArgument)
			else:
				newEntity.initParameter("ref",offset)
				newArgument=argument("ref")
				scopeList[-2].getLastEntity().appendArgument(newArgument)
			scopeList[-1].addEntity(newEntity)
			#endcode
			lex()
			return True
		else:

			error_comp(idtk)
	else:
		error_comp("FuncArgs")

# STATEMENTS
def statements(exitlist,retv):
	exitl=statement(exitlist,retv)

	if(exitl==False):
		return True
	if(exitl):
		exitlist=merge_list(exitl,exitlist)
		
	while(token == ";") :
		lex()
		exitl=statement(exitlist,retv)
		if(exitl):
			exitlist=merge_list(exitl,exitlist)
	return exitlist

# STATEMENT
def statement(exitlist,ret) :

	if(token==iftk):
		lex()
		exitl=if_stat(exitlist,ret)
		exitlist=merge_list(exitl,exitlist)
	elif(token==whiletk):
		lex()
		exitl=while_stat(exitlist,ret)
		exitlist=merge_list(exitl,exitlist)
	elif(token==dowhiletk):
		lex()
		do_while_stat(exitlist,ret)
	elif(token==looptk):
		lex()
		exitl=loop_stat(exitlist,ret)
		exitlist=merge_list(exitl,exitlist)
	elif(token==exittk):
		lex()
		exitl=exit_stat(exitlist)
		exitlist=merge_list(exitlist,exitl)
		return exitlist
	elif(token==forcasetk):
		lex()
		exitl=forcase_stat(exitlist,ret)
		exitlist=merge_list(exitl,exitlist)
	elif(token==incasetk):
		lex()
		exitl=incase_stat(exitlist,ret)
		exitlist=merge_list(exitl,exitlist)
	elif(token==returntk):
		lex()
		return_stat()
		ret[0]=True
	elif(token==inputtk):
		lex()
		input_stat()
	elif(token==printtk):
		lex()
		print_stat()
	elif(token==elsetk):
		return []
	else:
		endblock=assignment_stat()
		if(endblock):
			return False
	return exitlist


# ASSIGNMENT STAT
def assignment_stat() :

	if(check_end_statement(token)) :
		return []
	else:
	
		if(tokentk == idtk) :
			Eid=token
			searchEntity(token)
			lex()
			if(token == ":=") :
				lex()
				E=expression()
				genquad(":=",E,"__",Eid)
			else :
				error_comp("AssStatErr")
		else :

			error_comp(idtk)
		return False

# if_statEMENT
def if_stat(exitlist,ret) :
	if(token=="(") :
		lex()
		Btrue,Bfalse=condition()
		if(token==")") :
			lex()
			if(token==thentk) :
				backpatch(Btrue,nextquad())
				lex()
				exitl=statements([],ret)
				exitlist=merge_list(exitl,exitlist)
				iflist=make_list(nextquad())
				genquad("jump","__","__","__")
				backpatch(Bfalse,nextquad())

				exitl=elsepart(exitlist,ret)
				exitlist=merge_list(exitl,exitlist)
				backpatch(iflist,nextquad())

				if(token==endiftk):
					lex()	
				else:
					error_comp(endiftk)
			else:
				error_comp("IfErr1")
		else:
			error_comp("CondErr1")
	else:
		error_comp("CondErr1")

	return exitlist

# ELSEPART
def elsepart(exitlist,ret) :
	if(token==elsetk):
		lex()
		exitl=statements([],ret)
		exitlist=merge_list(exitl,exitlist)
	return exitlist

# WHILE STATEMENT
def while_stat(exitlist,ret) :
	firstQuad=nextquad()
	if(token=="(") :
		lex()
		Btrue,Bfalse=condition()
		if(token==")") :
			lex()
			backpatch(Btrue,nextquad())

			exitl=statements([],ret)
			exitlist=merge_list(exitl,exitlist)

			if(token==endwhiletk):
				lex()
				genquad("jump","__","__",firstQuad)
				backpatch(Bfalse,nextquad())
			else:
				error_comp(endwhiletk)
		else:
			error_comp("CondErr1")
	else :
		error_comp("CondErr1")

	return exitlist

# DO WHILE STAT
def do_while_stat(exitlist,ret) :
	sQuad=nextquad()
	exitl=statements([],ret)
	exitlist=merge_list(exitl,exitlist)
	if(token == enddowhiletk) :
		lex()
		if(token == "(") :
			lex()
			Btrue,Bfalse=condition()
			backpatch(Bfalse,sQuad)
			backpatch(Btrue,nextquad())
			if(token == ")") :
				lex()
			else:
				error_comp("CondErr1")
		else :
			error_comp("CondErr1")
	else :
		error_comp(enddowhiletk)
	return exitlist

# LOOP STATEMENT
def loop_stat(exL,ret) :
	global inLoop
	inLoop=True
	firstQuad=nextquad()
	exitlist=empty_list()
	exitl=statements(exitlist,ret)
	genquad("jump","__","__",firstQuad)
	backpatch(exitl,nextquad())
	if(token==endlooptk) :
		lex()
		inLoop=False
	else :
		error_comp(endlooptk)
	return exL

# EXIT STATEMENT
def exit_stat(exitlist) :
	global inLoop
	if(not inLoop):
		error_comp("exitErr")
	t=make_list(nextquad())
	genquad("jump","__","__","__")
	exitlist=merge_list(exitlist,t)
	return exitlist

# FORCASE STATEMENT
def forcase_stat(exitLoopList,ret):
	exitlist=empty_list()
	firstQuad=nextquad()
	while(token==whentk):
		lex()
		if(token=="("):
			lex()
			Btrue,Bfalse=condition()
			backpatch(Btrue,nextquad())
			if(token==")") :
				lex()
				if(token==":"):
					lex()
					exitl=statements([],ret)
					exitLoopList=merge_list(exitl,exitLoopList)
					exitlist=merge_list(exitlist,make_list(nextquad()))
					genquad("jump","__","__","__")
					backpatch(Bfalse,nextquad())
				else:
					error_comp("WhenStatErr")
			else:
				error_comp("CondErr1")
		else:
			error_comp("CondErr1")
	if(token==defaulttk):
		lex()
		if(token==":"):
			lex()
			exitl=statements([],ret)
			exitLoopList=merge_list(exitl,exitLoopList)
			genquad("jump","__","__",firstQuad)
			if(token==enddefaulttk):
				lex()
				if(token==endforcasetk):
					lex()
				else:
					error_comp(endforcasetk)
			else:
				error_comp(enddefaulttk)
		else:
			error_comp("WhenStatErr")			
	else:
		error_comp(defaulttk)
	backpatch(exitlist,nextquad())
	return exitLoopList

# IN CASE STATEMENT
def incase_stat(exitlist,ret) :
	t=newtemp()
	flagQuad=nextquad()
	genquad(":=","0","__",t)
	while(token==whentk):

		lex()
		if(token=="(") :
			lex()
			Btrue,Bfalse=condition()
			backpatch(Btrue,nextquad())
			genquad(":=","1","__",t)
			if(token==")") :
				lex()
				if(token==":") :
					lex()
					exitl=statements([],ret)

					exitlist=merge_list(exitl,exitlist)
					backpatch(Bfalse,nextquad())
				else :
					error_comp("WhenStatErr")
			else :
				error_comp("CondErr1")
		else :
			error_comp("CondErr1")
	genquad("=","1",t,flagQuad)
	if(token==endincasetk) :
		lex()
	else :
		if(token=="(") :
			print("Error at line (",line,"): Expected <when> before condition at statement.")
			exit()
		else :
			error_comp(endincasetk)
	return exitlist

# RETURN STATEMENT
def return_stat() :
	Eplace=expression()
	genquad("retv","__","__",Eplace)

# PRINT STATEMENT
def print_stat() :
	Eplace=expression()
	genquad("out",Eplace,"__","__")

# INPUT STATEMENT 
def input_stat() :
	if(tokentk == idtk ) :
		genquad("inp",token,"__","__")
		lex()
	else :
		error_comp(idtk)

# ACTUALPARS
def actualpars():
	if(token == "(") :
		lex()
		Elist=actualparlist()
		if(token==")"):
			lex()	
			return Elist
		else:
			error_comp("FuncForm")
	else :
		error_comp("FuncForm")

	
# ACTUAL PAR LIST
def actualparlist():
	Elist=empty_list()
	E1place=actualparitem()
	Elist.append(E1place)
	while(token==",") :
		lex()
		if(token==")"):
			error_comp("FuncArgs")
		E2place=actualparitem()
		Elist.append(E2place)
	if(token==intk or token==inouttk or token==inandouttk) :
		error_comp("ParErr")
	return Elist

# ACTUALPARITEM
def actualparitem() :
	if(token == inouttk ) :
		lex()
		if(tokentk == idtk) :
			Eplace=[token,"ref"]
			lex()
			return Eplace
		else :
			error_comp(idtk)
	elif(token == inandouttk):
		lex()
		if(tokentk == idtk) :
			Eplace=[token,"cp"]
			lex()
			return Eplace
		else :
			error_comp(idtk)
	elif(token == intk) :
		lex()
		Eret=expression()
		Eplace=[Eret,"cv"]
		return Eplace
	elif(token != ")") :
		error_comp("FuncArgs")

# CONDITION
def condition () :
	Q1true,Q1false=boolterm()
	Btrue=Q1true
	Bfalse=Q1false
	while(token == ortk) :
		backpatch(Bfalse,nextquad())
		lex()
		Q2true,Q2false=boolterm()
		Btrue=merge_list(Q2true,Btrue)
		Bfalse=Q2false
		
	return Btrue,Bfalse

# BOOLTERM
def boolterm () :
	R1true,R1false=boolfactor()
	Qtrue=R1true
	Qfalse=R1false
	while(token == andtk) :
		backpatch(Qtrue,nextquad())
		lex()
		R2true,R2false=boolfactor()
		Qfalse=merge_list(Qfalse,R2false)
		Qtrue=R2true

	return Qtrue,Qfalse

# BOOLFACTOR - KANONAS R
def boolfactor() :
	if(token == nottk) :
		lex()
		if(token == "[") :
			lex()
			Btrue,Bfalse=condition()
			Rtrue=Bfalse
			Rfalse=Btrue
			if(token == "]") :
				lex()
			else :
				error_comp("CondErr2")
		else :
			error_comp("CondErr2")
	elif(token == "[") :
		lex()
		Btrue,Bfalse=condition()
		Rfalse=Bfalse
		Rtrue=Btrue
		if(token == "]") :
			lex()
		else :
			error_comp("CondErr2")
	else :
		E1place=expression()
		relop=relational_oper()
		E2place=expression()

		# P1 START
		Rtrue=make_list(nextquad())
		genquad(relop,E1place,E2place,'__')
		Rfalse=make_list(nextquad())
		genquad("jump","__","__","__")
		# P1 END

	return Rtrue,Rfalse

# EXPRESSION
def expression() :
	global call_func
	Eplace=token
	opt=optional_sign()
	T1=term()
	if(opt=="-"):
		w=newtemp()
		genquad(opt,0,T1,w)
		T1=w
	#print(T1)
	while(add_oper()) :
		addOper=token
		lex() 
		if(add_oper()) :
			error_comp("AssStatErr")
		T2=term()
		# P1 START
		w=newtemp()
		genquad(addOper,T1,T2,w)
		T1=w
		# P1 END

	Eplace=T1
	
	return Eplace

# TERM
def term() :
	Eplace=token
	w=""
	F1=factor()
	while(mul_oper()) :
		mulOper=token
		lex()
		if(mul_oper()) :
			error_comp("AssStatErr")
		F2=factor()
		# P1 START
		w=newtemp()
		genquad(mulOper,F1,F2,w)
		F1=w
		# P1 END

	Eplace=F1
	return Eplace

def factor() :
	if(token == "(") :
		lex() 
		F=expression()
		if(token==")"):
			lex()
		else :
			error_comp("ExpErr1")
	elif(tokentk == idtk) :
		funcName=token
		lex()
		ParList=id_tail()
		if (ParList==[]):
			searchEntity(funcName)
			return funcName
		else:
			if(ParList[0] is not None):
				for item in ParList :
					genquad("par",item[0],item[1],"__")
				#parList contains arrays with 2 elements.
				#example of parList: [[a,cv],[b,ref],[c,cp]]
				#item[0] is the name of parameter
				#item[1] is the type of parameter
				searchParametes(funcName,ParList)

			w=newtemp()
			genquad("par",w,"RET","__")
			genquad("call",funcName,"__","__")
			
			return w
	elif(token[0].isdigit()):
		F=token
		lex()
	else :
		error_comp("AssStatErr")
	return F

# ID TAIL
def id_tail():
	if(token == "(") :
		Alist=actualpars()
		if(not Alist== []):
			return Alist
	else :
		return []	

# RELATIONAL OPER
def relational_oper():
	relop=token
	if(token=="=" or token=="<=" or token==">=" or token==">" or token=="<" or token=="<>" ):
		lex()
		return relop
	else:
		print("Error at line (",line,"): Expected relational operator in condition.")
		exit()

# MUL OPER
def mul_oper() :
	if(token =="*" or token == "/") :
		return True
	return False

def add_oper() :
	if(token =="+" or token == "-") :
		return True
	return False

# OPTIONAL SIGN
def optional_sign() :
	opt_sign=token
	if(token =="+" or token =="-") :
		lex()
		return opt_sign

def check_end_statement(token) :
	end_statements = ["endif","endwhile","enddowhile","endloop","endforcase","endincase","endprogram","endfunction","default"]
	if(token in end_statements) :
		return True
	return False

def trash() :
	lex()
	if(token!=""):
		if(token=="m"):
			lex()
			if(token=="m") :
				return False
			else : return True
		else :
			return True
	else :
		return False

def similarity(errortk) :
	return SequenceMatcher(None, errortk, token).ratio()




###### CLASSES CLASSES CLASSES CLASSES ######

# QUAD #
class quad :
	global quadList
	label="__"
	op="__"
	op1="__"
	op2="__"
	tr="__"

	def __init__(self,label,op,op1,op2,tr) :
		if(label!=""):
			self.label=str(label)
		if(op!=""):
			self.op=str(op)
		if(op1!=""):
			self.op1=str(op1)
		if(op2!=""):
			self.op2=str(op2)
		if(tr!=""):
			self.tr=str(tr)

	def toString(self):
		#print(""+self.label+": "+self.op+", "+self.op1+", "+self.op2+", "+self.tr)
		return(""+self.label+": "+self.op+", "+self.op1+", "+self.op2+", "+self.tr)
	def getLabel(self):
		return self.label
	def getOperator(self):
		return self.op
	def getOp1(self): 
		return self.op1
	def getOp2(self):
		return self.op2
	def getTr(self):
		return self.tr
# END QUAD #

#ARGUMENT #
class argument :
	parMode=""
	nextArg=""
	address=""

	def __init__(self,parMode):
		self.parMode=parMode
	def getParMode(self):
		return self.parMode
	def setNextArg(self,nextArg):
		self.nextArg=nextArg
	def setAddress(self,address):
		self.address=address
	def getAddress(self):
		return self.address
	def toString(self):
		return self.parMode
#END ARGUMENT #

# SCOPE #
class scope :
	global nestingLevel	
	scopeName=""
	offset=12
	entitylist=[]
	enclosingScope=""
	startQuad=""
	nestingLevel=0
	cp=False

	def __init__(self,scopeName):
		global scopeLevel
		#print(scopeName,scopeLevel)
		self.scopeName=scopeName
		self.strtQuad=""
		self.startQuad=nextquad()
		
		self.nestingLevel=scopeLevel
		self.entitylist=[]
		scopeLevel+=1

	def addEntity(self,entity):

		self.offset+=4
		self.entitylist.append(entity)

	def setStartQuad(self,startQuad):
		int_startQuad=int(startQuad)
		self.startQuad=str(int_startQuad-1)

	def setNextScoe(self,scope):
		self.enclosingScope=scope
	def setCp(self):
		self.cp=True
	def getCp(self):
		return self.cp
	def getFrameLength(self):
			
		return self.offset

	def toString(self):
		return(str(self.nestingLevel))

	def getStartQuad(self):
		return self.startQuad

	def getStrEntity(self,num):
		return str(entitylist[num])
	def getLastEntity(self):
		return self.entitylist[-1]
	def getEntity(self,num):
		return self.entitylist[num]
	def getOffset(self):
		return self.offset;
	def getEntityList(self):
		return self.entitylist
	def getScopeName(self):
		return self.scopeName
	def getScopeLevel(self):
		return self.nestingLevel
	def printScope(self):
		print(self.toString()+": ")
		for entity in self.entitylist:
			if(entity.isParameter()):
				print("<"+entity.getParamtype()+">")
			if(entity.isFunction()):
				entity.printArgList()
				print("{fl:")
				print(entity.getFrameLength(),",stQ:"+entity.getStartQuad())
				print("}")
			print(entity.getName()+",")
		print("end")
	def setFuncOffset(self):
		self.offset-=4
# ENDSCOPE #

# ENTITY #
class entity :
	name=""
	entitype=""
	offset=0
	functionReturn=""
	paramtype=""
	framelength=0
	startQuad="" # contains firstquad's label of block. ( exmpl: 17: begin_block,block_name,__,__, ) )
														#entity P1 function's startquad contains label:  17
	nextEntity=""
	arguments=[]
	cp=False

	def __init__(self,name):
		self.name=name
		self.arguments=[]

	def initVariable(self,offset):
		self.entitype="variable"
		self.offset=offset

	def initParameter(self,paramtype,offset):
		self.entitype="parameter"
		self.paramtype=paramtype
		self.offset=offset

	def initFucntion(self,framelength,startQuad):

		self.entitype="function"
		self.framelength=framelength
		self.startQuad=startQuad
		#self.arguments=[]

	def appendArgument(self,argument):
		self.arguments.append(argument)
		#print("yo")
	
	def setNext(self,entity):
		self.nextEntity=entity

	# Getters
	def getName(self):
		return self.name
	def getType(self): 
		return self.entitype
	def getOffset(self):	
		return self.offset
	def getParamtype(self):
		return self.paramtype
	def getNext(self):
		return nextEntity;
	def isFunction(self):
		if(self.entitype=="function"):
			return True
		return False
	def isParameter(self):
		if(self.entitype=="parameter"):
			return True
		return False
	def getFrameLength(self):
		return self.framelength
	def getStartQuad(self):
		return self.startQuad
	def getArugments(self):
		return self.arguments
	def printArgList(self):
		print("[")
		if(self.entitype=="function"):
			for item in self.arguments:
				print(item.toString()+",")
		print("]->")				
#END ENTITY #
##### ..CLASSES .. ######


##### FUNCTIONS FOR INTERMEDIATE CODE GENERATION #####
def nextquad() :
	global label
	help_label=label+1
	return (str(help_label))


def genquad(op,op1,op2,tr):
	global label
	label=label+1
	new_quad=quad(str(label),op,op1,op2,tr)
	quadList.append(new_quad)

def newtemp():
	global ntmp
	global ntmp_num

	ntmp_num=ntmp_num+1
	newEntity=entity(ntmp+str(ntmp_num))
	offset=scopeList[-1].getOffset()
	newEntity.initVariable(offset)
	scopeList[-1].addEntity(newEntity)

	return (ntmp+str(ntmp_num))

def empty_list() :
	return []

def make_list(x):
	return [x]

def merge_list(list1,list2) :
	return (list1+list2)

def backpatch(list,z) :
	for i in list :
		for quad in quadList :
			if(i==quad.label) :
				quad.tr=z

##### END FUNCTIONS FOR INTERMEDIATE CODE GENERATION #####

##### FUNCTIONS FOR SYMBOL TABLE GENERATION #####
def new_variable_entity(entityname):
	newEntity=entity(entityname)
	offset=scopeList[-1].getOffset()
	newEntity.initVariable(offset)
	scopeList[-1].addEntity(newEntity)
	return newEntity

def new_function_entity(entityname):
	newEntity=entity(entityname)
	scopeList[-1].addEntity(newEntity)
	scopeList[-1].setFuncOffset()
	return newEntity

def new_scope(scopename):
	newScope=scope(scopename)
	scopeList.append(newScope)
	return newScope

def delete_scope():
	scopeList.pop(-1)

def searchEntity(entityName):
	for scope in reversed(scopeList):
		for entity in reversed(scope.getEntityList()):
			if(entity.getName()==entityName):
				return True
	#error_comp("DeclErr")
	return False

def searchParametes(funcName,parList):
	for scope in reversed(scopeList):
		for entity in reversed(scope.getEntityList()):
			if(entity.getName()==funcName):
				arguments=entity.getArugments()
				if(len(arguments)==len(parList)):
					for i in range(len(parList)):
						if(arguments[i].getParMode()!=parList[i][1]):
							error_comp("FuncArgsErr")
					return True
				else:
					error_comp("FuncArgsErr")
	#error_comp("FuncErr")
		
##### END FUNCTIONS FOR SYMBOL TABLE GENERATION #####

#### FUNCTIONS FOR FINAL CODE GENERATION #####
def finalCodeGeneration(framelength,startQuad):
	global fileASM
	global programFrameLength
	i=0
	lmain=0
	cparray=[]
	flag=False
	for quad in quadList :
		if(int(quad.getLabel())>=int(startQuad)):
			if(int(quad.getLabel())==int(programStartQuad) and flag==False):
				fileASM.write("Lmain:\n")
				fileASM.write("\taddi $sp,$sp,"+str(programFrameLength)+"\n")
				fileASM.write("\tmove $s0,$sp\n")
				flag=True
			fileASM.write("L"+quad.getLabel()+":\n")
			
			if(quad.getOperator()==":="):
				loadvr(quad.getOp1(),1)
				storerv(1,quad.getTr())
				fileASM.write("\t#"+quad.toString()+"\n")
			elif(quad.getOperator()=="halt"):
				fileASM.write("\tli $v0, 10\n")
				fileASM.write("\tsyscall\n")
			elif(quad.getOperator()=="begin_block"):
				fileASM.write("\t#"+quad.toString()+"\n")
				fileASM.write("\tsw $ra, 0($sp) 	# "+quad.getOp1()+"\n")
			elif(quad.getOperator()=="end_block"):
				fileASM.write("\t#"+quad.toString()+"\n")
				fileASM.write("\tlw $ra, 0($sp)\n")
				fileASM.write("\tjr $ra\n")
			elif(quad.getOperator()=="call"):
				fileASM.write("\t#"+quad.toString()+"\n")
				flag=False
				nextFuncFl=findFrameLength(quad.getOp1())
				nextFuncSq=findFirstQuad(quad.getOp1())
				nextFuncLevel=getDepth(quad.getOp1())
				for entity in scopeList[-1].getEntityList():
					if(quad.getOp1()==entity.getName()):
						flag=True
						fileASM.write("\tsw $sp,-4($fp)\t#"+quad.toString()+"\n")
				if(flag==False):  # anadromiki klisi h aderfos
					
					fileASM.write("\tlw $t0,-4($sp)\t#"+quad.toString()+"\n")
					fileASM.write("\tsw $t0,-4($fp)\n")
				
				fileASM.write("\taddi $sp,$sp,"+str(nextFuncFl)+"\n")
				fileASM.write("\tjal L"+str(nextFuncSq)+"\n")
				fileASM.write("\taddi $sp,$sp,-"+str(nextFuncFl)+"\n")
				i=0
				j=0
				for cpvar in reversed(cparray):
					if(j==0):
					#print("mpika sti loop ap to kodika tis: "+str(startQuad))
						fileASM.write("\taddi $fp,$sp,"+str(nextFuncFl)+"\n")

					fileASM.write(cpvar+"\n")
					j+=1

			## PAAAAAAAAAAAAAAAAAAAAAR ##
			elif(quad.getOperator()=="par"):
				fileASM.write("\t#"+quad.toString()+"\n")
				nextFuncQuad=findNextCallFunc(quad) #returns the quad of next called function
				nextFuncName=nextFuncQuad.getOp1()	#returns the name of function
				nextFuncFl=findFrameLength(nextFuncName) #returns the framelength of function
				nextFuncDepth=getDepth(nextFuncName)
	
				if(i==0):
					fileASM.write("\taddi $fp,$sp,"+str(nextFuncFl)+"\t#"+startQuad+"\n")
				if(quad.getOp2()=="cv"):
					loadvr(quad.getOp1(),0)
					fileASM.write("\tsw $t0,-"+str(12+4*i)+"($fp) \t#"+quad.toString()+"\n")
					i+=1
				elif(quad.getOp2()=="ref"):
					if(checkVariable(quad.getOp1())=="local_variable" or checkVariable(quad.getOp1())=="local_cv_parameter"):
						for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
							if(quad.getOp1()==entity.getName()):
								fileASM.write("\taddi $t0,$sp,-"+str(entity.getOffset())+"\n")
						fileASM.write("\tsw $t0,-"+str(12+4*i)+"($fp) \t#"+quad.toString()+"\n")
					elif(checkVariable(quad.getOp1())=="local_ref_parameter" ):
						for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
							if(quad.getOp1()==entity.getName()):
								fileASM.write("\tlw $t0,-"+str(entity.getOffset())+"($sp)"+"\n")
						fileASM.write("\tsw $t0,-"+str(12+4*i)+"($fp) \t#"+quad.toString()+"\n")
					elif(checkVariable(quad.getOp1())=="prog_variable" or checkVariable(quad.getOp1())=="prog_cv_parameter"):
						gnvlcode(quad.getOp1())
						fileASM.write("\tsw $t0,-"+str(12+4*i)+"($fp) \t#"+quad.toString()+"\n")
					elif(checkVariable(quad.getOp1())=="prog_ref_parameter"):
						gnvlcode(quad.getOp1())
						fileASM.write("\tlw $t0,0($t0)\n")
						fileASM.write("\tsw $t0,-"+str(12+4*i)+"($fp) \t#"+quad.toString()+"\n")
					
					i+=1
				elif(quad.getOp2()=="cp"):
					loadvr(quad.getOp1(),0)
					
					fileASM.write("\tsw $t0,-"+str(12+4*i)+"($fp) \t#"+quad.toString()+"\n")
					
					string="\tlw $t0,-"+str(12+4*i)+"($fp) \t#"+quad.toString()+"#  EDO TO CP\n"
					string+=storerp(0,quad.getOp1())
					#print("eimai sto scope: "+scopeList[-1].toString()+" kai kalo to scope: "+nextFuncName)
					cparray.append(string)
					# to str(12+4*i)+")($fp) diladi to address tis metavliti pu erhete prepei na ti kserw ston endblock tis sinartisis pu kaleite
					# oste sto telos tou enblock tis na apothikefso ti timi se afti ti diefthinsi
					i+=1
				elif(quad.getOp2()=="RET"):
					for entity in scopeList[-1].getEntityList():
						if(entity.getName()==quad.getOp1()):
							fileASM.write("\taddi $t0,$sp,-"+str(entity.getOffset())+"\n")
							fileASM.write("\tsw $t0,-8($fp)\n")
				else:
					i=0
				
			## PAAAAAAAAAAAAAAAAAAAAAR ##


			elif(quad.getOperator()=="jump"):
				fileASM.write("\t#"+quad.toString()+"\n")
				fileASM.write("\tj L"+quad.getTr()+"\n")
			elif(quad.getOperator() in [">","<","<=",">=","=","<>"]):
				fileASM.write("\t#"+quad.toString()+"\n")
				loadvr(quad.getOp1(),1)
				loadvr(quad.getOp2(),2)
				if(quad.getOperator()==">"):
					fileASM.write("\tbgt $t1,$t2,L"+quad.getTr()+"\n")
				elif(quad.getOperator()==">="):
					fileASM.write("\tbge $t1,$t2,L"+quad.getTr()+"\n")
				elif(quad.getOperator()=="<"):
					fileASM.write("\tblt $t1,$t2,L"+quad.getTr()+"\n")
				elif(quad.getOperator()=="<="):
					fileASM.write("\tble $t1,$t2,L"+quad.getTr()+"\n")
				elif(quad.getOperator()=="="):
					fileASM.write("\tbeq $t1,$t2,L"+quad.getTr()+"\n")
				elif(quad.getOperator()=="<>"):
					fileASM.write("\tbne $t1,$t2,L"+quad.getTr()+"\n")
			elif(quad.getOperator() in ["+","-","*","/"]):
				fileASM.write("\t#"+quad.toString()+"\n")
				loadvr(quad.getOp1(),1)
				loadvr(quad.getOp2(),2)
				if(quad.getOperator()=="+"):
					fileASM.write("\tadd $t1,$t1,$t2\n")
				elif(quad.getOperator()=="-"):
					fileASM.write("\tsub $t1,$t1,$t2\n")
				elif(quad.getOperator()=="*"):
					fileASM.write("\tmul $t1,$t1,$t2\n")
				elif(quad.getOperator()=="/"):
					fileASM.write("\tdiv $t1,$t1,$t2\n")
				storerv(1,quad.getTr())
			elif(quad.getOperator()=="out"):
				fileASM.write("\t#"+quad.toString()+"\n")
				fileASM.write("\tli $v0,1\n")
				loadvr(quad.getOp1(),1)
				fileASM.write("\tmove $a0,$t1\n")
				
				fileASM.write("\tsyscall\n")
				fileASM.write("\tli $v0,4\n")
				fileASM.write("\tla $a0,newline\n")
				fileASM.write("\tsyscall\n")
			elif(quad.getOperator()=="inp"):
				fileASM.write("\t#"+quad.toString()+"\n")
				fileASM.write("\t li $v0,5\n")
				fileASM.write("\tsyscall\n")
				fileASM.write("move $t0,$v0\n")

				storerv(0,quad.getOp1())
			elif(quad.getOperator()=="retv"):
				fileASM.write("\t#"+quad.toString()+"\n")
				loadvr(quad.getTr(),1)
				fileASM.write("\tlw $t0, -8($sp)\n")
				fileASM.write("\tsw $t1,0($t0)\n")
				fileASM.write("\tlw $ra, 0($sp)\n")
				fileASM.write("\tjr $ra\n")
			#fileASM.write("\n")
			

def loadvr(var, tr):
	global fileASM

	if(checkVariable(var)=="constant"): 
		fileASM.write("\tli $t"+str(tr)+","+var+"\n")
	elif(checkVariable(var)=="global_variable"):
		for entity in scopeList[0].getEntityList(): # diatrehw to entitylist tis main gia na vro to offset tis var
			if(var==entity.getName()):
				fileASM.write("\tlw $t"+str(tr)+",-"+str(entity.getOffset())+"($s0)"+"\n")
	elif(checkVariable(var)=="local_variable" or checkVariable(var)=="local_cv_parameter"):
		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):
				fileASM.write("\tlw $t"+str(tr)+",-"+str(entity.getOffset())+"($sp)"+"\n")
	elif(checkVariable(var)=="local_ref_parameter" ):
		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):
				fileASM.write("\tlw $t0,-"+str(entity.getOffset())+"($sp)"+"\n")
				fileASM.write("\tlw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="local_cp_parameter"):
		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):
				fileASM.write("\tlw $t"+str(tr)+",-"+str(entity.getOffset())+"($sp)"+"\n")
	elif(checkVariable(var)=="prog_variable" or checkVariable(var)=="prog_cv_parameter"):
		gnvlcode(var)
		fileASM.write("\tlw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="prog_ref_parameter"):
		gnvlcode(var)
		fileASM.write("\tlw $t0,($t0)\n")
		fileASM.write("\tlw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="prog_cp_parameter"):
		gnvlcode(var)
		fileASM.write("\tlw $t"+str(tr)+",0($t0)\n")
	


def storerv(tr, var):
	retString=""

	if(checkVariable(var)=="global_variable"):
		for entity in scopeList[0].getEntityList(): # diatrehw to entitylist tis main gia na vro to offset tis var
			if(var==entity.getName()):
				fileASM.write("\tsw $t"+str(tr)+",-"+str(entity.getOffset())+"($s0)"+"\n")
				retString+="\tsw $t"+str(tr)+",-"+str(entity.getOffset())+"($s0)"+"\n"
	elif(checkVariable(var)=="local_variable" or checkVariable(var)=="local_cv_parameter"):

		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):

				fileASM.write("\tsw $t"+str(tr)+",-"+str(entity.getOffset())+"($sp)"+"\n")
				retString+=("\tsw $t"+str(tr)+",-"+str(entity.getOffset())+"($sp)"+"\n")
	elif(checkVariable(var)=="local_ref_parameter" ):
		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):
				fileASM.write("\tlw $t0,-"+str(entity.getOffset())+"($sp)"+"\n")
				fileASM.write("\tsw $t"+str(tr)+",0($t0)\n")
				retString+=("\tlw $t0,-"+str(entity.getOffset())+"($sp)"+"\n")
				retString+=("\tsw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="prog_variable" or checkVariable(var)=="prog_cv_parameter"):
		retString+=gnvlcode(var)

		fileASM.write("\tsw $t"+str(tr)+",0($t0)\n")
		retString+=("\tsw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="prog_ref_parameter"):
		retString+=gnvlcode(var)
		fileASM.write("\tlw $t0,0($t0)\n")
		fileASM.write("\tsw $t"+str(tr)+",0($t0)\n")
		retString+=("\tlw $t0,0($t0)\n")
		retString+=("\tsw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="local_cp_parameter"):
		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):
				fileASM.write("\tsw $t"+str(tr)+",-"+str(entity.getOffset())+"($sp)"+"\n")
	elif(checkVariable(var)=="prog_cp_parameter"):
		gnvlcode(var)
		fileASM.write("\tsw $t"+str(tr)+",0($t0)\n")
	return retString

def storerp(tr, var):
	retString=""
	if(checkVariable(var)=="global_variable"):
		for entity in scopeList[0].getEntityList(): # diatrehw to entitylist tis main gia na vro to offset tis var
			if(var==entity.getName()):
				retString+="\tsw $t"+str(tr)+",-"+str(entity.getOffset())+"($s0)"+"\n"
	elif(checkVariable(var)=="local_variable" or checkVariable(var)=="local_cv_parameter"):
		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):
				retString+=("\tsw $t"+str(tr)+",-"+str(entity.getOffset())+"($sp)"+"\n")
	elif(checkVariable(var)=="local_ref_parameter" ):
		for entity in scopeList[-1].getEntityList(): # diatrehw to entitylist tou trexon scope gia na vro to offset tis var
			if(var==entity.getName()):
				retString+=("\tlw $t0,-"+str(entity.getOffset())+"($sp)"+"\n")
				retString+=("\tsw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="prog_variable" or checkVariable(var)=="prog_cv_parameter"):
		retString+=gnvlcodecp(var)
		retString+=("\tlw $t"+str(tr)+",0($t0)\n")
	elif(checkVariable(var)=="prog_ref_parameter"):
		retStrin+=gnvlcodecp(var)
		retString+=("\tlw $t0,0($t0)\n")
		retString+=("\tsw $t"+str(tr)+",0($t0)\n")
	return retString

def gnvlcode(var):
	global fileASM
	i=0
	flag=0
	offset=0
	retString=""

	for scope in reversed(scopeList):
		for entity in scope.getEntityList():
			if(var==entity.getName()):
				flag=1
				#print(entity.getName()+"->"+str(entity.getOffset()))
				offset=entity.getOffset()
				break
		if(flag==1):
			break
		i+=1

	fileASM.write("\tlw $t0,-4($sp)\n")
	retString+="\tlw $t0,-4($sp)\n"
	for j in range (2,i):
		fileASM.write("\tlw $t0,-4($t0)\n")
		retString+="\tlw $t0,-4($t0)\n"
	fileASM.write("\taddi $t0,$t0,-"+str(offset)+"\n")
	retString+="\taddi $t0,$t0,-"+str(offset)+"\n"
	return retString


def gnvlcodecp(var):
	
	global fileASM
	i=0
	flag=0
	offset=0
	retString=""

	for scope in reversed(scopeList):
		for entity in scope.getEntityList():
			if(var==entity.getName()):
				flag=1
				#print(entity.getName()+"->"+str(entity.getOffset()))
				offset=entity.getOffset()
				break
		if(flag==1):
			break
		i+=1

	retString+="\tlw $t0,-4($sp)\n"
	for j in range (2,i):
		retString+="\tlw $t0,-4($t0)\n"
	retString+="\taddi $t0,$t0,-"+str(offset)+"\n"
	return retString


def checkVariable(var):
	
	if(var.isdigit()):
		return "constant"
	i=0
	for scope in reversed(scopeList):
		for entity in scope.getEntityList():
			if(var == entity.getName()):
				if(i!=0): # diladi an den eimai sto current scope
					if(i!=len(scopeList)-1):
						if(entity.getType()=="variable"):
							return "prog_variable"
						elif(entity.getType()=="parameter"):
							if(entity.getParamtype()=="cv"):
								return "prog_cv_parameter"
							elif(entity.getParamtype()=="ref"):
								return "prog_ref_parameter"
							else:
								return "prog_cp_parameter"
					else:
						if(var == entity.getName()):

							return "global_variable"
				elif(i==0):
					if(entity.getType()=="variable"):
						return "local_variable"
					elif(entity.getType()=="parameter"):
						if(entity.getParamtype()=="cv"):
							return "local_cv_parameter"
						elif(entity.getParamtype()=="ref"):
							return "local_ref_parameter"
						else:
							return "local_cp_parameter"
		i+=1	

	scopeName=""
	for quad in quadList:
		if(int(nextquad())-1==int(quad.getLabel())):
			scopeName=quad.getOp1()

	print("Error : Variable ("+var+") not declared in the scope of "+scopeName+".") 
	exit(1)

def getvarOffset(var):
	for scope in scopeList:
		for entity in scope.getEntityList():
			if(var==entity.getName()):
				return entity.getOffset()
	return -1

def quadnext(otherquad):
	flag=False
	for quad in quadList:
		if(flag==True):
			return quad
		if(quad.getLabel()==otherquad.getLabel()):
			flag=True
		
def findNextCallFunc(other):
	#
	nextquad=quadnext(other)
	if(nextquad.getOperator()=="call"):
		return nextquad
	while(nextquad.getOperator()!="call"):
		nextquad=findNextCallFunc(nextquad)
		return nextquad

def findFrameLength(funcname):
	for scope in reversed(scopeList):
		for entity in scope.getEntityList():
			if(funcname==entity.getName()):
				return entity.getFrameLength()
	return -1

def findFirstQuad(funcname):
	for scope in reversed(scopeList):
		for entity in scope.getEntityList():
			if(funcname==entity.getName()):
				return entity.getStartQuad()
	return -1

def getDepth(quadName):
	for scope in reversed(scopeList):
		if(quadName==scope.getScopeName()):
			return scope.getScopeLevel()



#### END FUNCTIONS FOR FINAL CODE GENERATION #####


##### AUXILIARY FUNCTIONS #####
def printScope(): #print scopes
	print(scopeList[-1].toString()+": ")
	entlist=scopeList[-1].getEntityList()
	for entity in entlist:
		print(entity.getName()+",")
		if(entity.isFunction()):
			print("->[")
			entity.printArgList()
			print("]")
	#print("end print scope")

def append_c_file():
	programc=programid+".c"
	filec=open(programc,"w")
	filec.write("#include <stdio.h>\n")
	filec.write("int main()\n{\n\t")
	filec.write("int ")
	lenlist=len(scopeList[-1].getEntityList())
	i=0
	for entity in scopeList[-1].getEntityList():
		if i!=lenlist-1:
			filec.write(entity.getName()+",")
		else:
			filec.write(entity.getName())
		i+=1
	filec.write(";\n")

	for quad in quadList:
		filec.write("\tL_"+quad.getLabel()+": ")
		if(quad.getOperator()==":="):
			filec.write(quad.getTr()+"="+quad.getOp1()+"; ")
		if(cond(quad.getOperator())):
			filec.write("if ("+quad.getOp1()+quad.getOperator()+quad.getOp2()+") goto L_"+quad.getTr()+"; ")
		if(quad.getOperator()=="jump"):
			filec.write("goto L_"+quad.getTr()+"; ")
		if(quad.getOperator()=="+" or quad.getOperator()=="-" or quad.getOperator()=="*" or quad.getOperator()=="/"):
			filec.write(quad.getTr()+"="+quad.getOp1()+quad.getOperator()+quad.getOp2()+"; ")
		if(quad.getOperator()=="out"):
			string="printf("+'"'+"%d\\n"+'"'+","+quad.getOp1()+");"
			filec.write(string)
		if(quad.getOperator()=="inp"):
			string="scanf("+'"'+"%d\\n"+'"'+",&"+quad.getOp1()+");"
			filec.write(string)
		if(quad.getOperator()=="end_block"):
			filec.write("{}")
		filec.write("// ("+quad.toString()+")")
		filec.write("\n")

	filec.write("}")

def append_int_file():
	programInt=programid+".int"
	filec=open(programInt,"w")
	for quad in quadList:
		filec.write(quad.toString()+"\n")

def printQuadList():	#prints quads
	for quad in quadList:
		quad.toString()

def cond(op):
	if (op==">=" or op=="<=" or op=="=" or op==">" or op=="<" or op=="<>"):
		return True

##### END AUXILIARY FUNCTIONS #####


##### MAIN #####
def main():

	global file_name
	global file
	global filec
	global programid
	global line
	global fileASM
	global scopeLevel

	file_name=sys.argv[1]
	#file_name="example.stl"

	if(file_name[-4:len(file_name)]==".stl") :
		
		programid=file_name[:-4]
		file=open(file_name,"r")
		programc=programid+".asm"
		fileASM=open(programc,"w")
		fileASM.write("\t.data\nnewline: .asciiz "+'"\\n"'+"\n\t.text\n")
		fileASM.write("L:\n\tj Lmain\n")

		if(program()):
			if(not trash()) :
				print("... lexical and syntax analysis passed, ",line," lines...")
			else :
				print("Error at line (",line,"): Trash after endprogram.")
				exit()
		append_int_file()
		
		
		
		
		#printQuadList()
##### END MAIN #####

programStartQuad=-1
programFrameLength=-1
inLoop=False
scopesToString=[]
scopeList=[]
programOffset=0
scopeLevel=0
Eplace=""
w=""
quadList=empty_list()
label=-1	# etiketa tetradas
ntmp="T_"	# prosorinh metavliti
ntmp_num=0	# arithmos prosorinis metavlitis
line=1	# grammi error
main()


import konlpy
from konlpy.tag import Kkma
from konlpy.utils import pprint
from kpsg_signature import *
from lex_rule import *
from phrase_rule import *

#Read verbset by transitivity 

intr_v_set = open('verbset/intr.txt',encoding="utf-8").read()
intr_v_set = intr_v_set.split('\n')

acc_tr_v_set = open('verbset/acc_tr.txt',encoding="utf-8").read()
acc_tr_v_set = acc_tr_v_set.split('\n')

dat_tr_v_set = open('verbset/dat_tr.txt',encoding="utf-8").read()
dat_tr_v_set = dat_tr_v_set.split('\n')

di_v_set = open('verbset/ditr.txt',encoding="utf-8").read()
di_v_set = di_v_set.split('\n')


#Parser 
parser = Kkma()


#################################################  Functions to apply Lexical rules

def LEXEME_LIST(string):
   ParsedSent=parser.pos(string)
   AVM_SET=[]
   for lexeme in ParsedSent:
      AVM_SET.append(GetAVM(lexeme))
   return AVM_SET

   
def lex_rule_apply(a):
	length = len(a)
	for i in range(0,length):
		if i >= len(a)-1:
			break
		out = lex_rule(a[i],a[i+1])
		#print(i)
		#print(out)
		if type(out)!=tuple:
			del a[i]
			del a[i]
			a.insert(i,out)
	return a

#===== Recursively apply lex_rule_apply until no units can be combined through lex_rule

def LEX_RULE(string):
        AVM_SET = LEXEME_LIST(string)
        output=lex_rule_apply(AVM_SET)
        while len(output)>1:
                new_output = lex_rule_apply(output)
                if new_output != output:
                        output = new_output
                elif len(output)==1:
                        return output
                else:
                        break
        return output

#################################################  Functions to apply Phrase rules



def phrase_rule_apply(a):
	length = len(a)
	for i in range(0,length):
		if i >= len(a)-1:
			break
		out = phrase_rule(a[i],a[i+1])
		if type(out)!=tuple:
			del a[i]
			del a[i]
			a.insert(i,out)
	return a


#===== Recursively apply phrase_rule_apply until no units can be combined through phrase_rule


def PHRASE_RULE(input):
   if len(input)==1:
      return (input)
   output = phrase_rule_apply(input)
   if len(output)==1:
      return output
   while len(output)>1:
      new_output = phrase_rule_apply(output)
      if len(output)==1:
         return output
      else:
         ori_num=len(new_output)
         new_output = phrase_rule_apply(new_output)
         new_num = len(new_output)
         if ori_num == new_num:
            break
      return new_output


#################################################  Function to printout grammar function of the given string
                
def cat(string):
   WORDS = LEX_RULE(string)
   OUTPUT = PHRASE_RULE(WORDS)
   print(OUTPUT[0].constraint)



#################################################  Function to transform the lexeme into a constraint(AVM)
#												   The function takse a tuple of (Lexeme,POS) as an input


def GetAVM(input):
        
   if input[1].startswith('VV') or input[1].startswith('VX'):
           
           if input[0] in intr_v_set:
              retVal = V_INTR_LXM()
              retVal.constraint['orth'] = input[0]
              return retVal

           if input[0] in acc_tr_v_set:
              retVal = V_ACC_TR_LXM()
              retVal.constraint['orth'] = input[0]
              return retVal

           if input[0] in dat_tr_v_set:
              retVal = V_DAT_TR_LXM()
              retVal.constraint['orth'] = input[0]
              return retVal


   if input[1].startswith("VA"):
      retVal = ADJ_LXM()
      retVal.constraint['orth'] = input[0]
      return retVal

   if input[1].startswith("EF"):
      retVal = V_ENDING_M_LXM()
      retVal.constraint['orth'] = input[0]
      return retVal
   
   if input[1].startswith("EP"):
      retVal = V_NON_ENDING_M_LXM()
      retVal.constraint['orth'] = input[0]
      return retVal

   if input[1].startswith("JKS") or input[1].startswith('JX') :
      retVal = N_M_nom_LXM()
      retVal.constraint['orth'] = input[0]
      return retVal

   if input[1].startswith("JKO"):
      retVal = N_M_acc_LXM()
      retVal.constraint['orth'] = input[0]
      return retVal

   if input[1].startswith("JKM"):
      retVal = N_M_dat_LXM()
      retVal.constraint ['orth']= input[0]
      return retVal

   if input[1]=="NNP" or input[1] =="NNG" or input[1]=='NP':
      retVal = N_WORD()
      retVal.constraint['orth'] = input[0]
      return retVal

   if input[1]=="MAG":
      retVal = ADV_WORD()
      retVal.constraint['orth'] = input[0]
      return retVal

   if input[1] == "ETD":
      retVal = ADJ_M_LXM()
      retVal.constraint['orth'] = input[0]
      return retVal

   if input[1] == "ECD":
      retVal = ADV_M_LXM()
      retVal.constraint['orth'] = input[0]
      return retVal


   


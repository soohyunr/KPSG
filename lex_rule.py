#lexical rules
from kpsg_signature import *

def lex_rule(a,b): 

#################################################  Nominal Rules

   if a.constraint['type']=='N_WORD' and issubclass(type(b),N_M_LXM):
      if a.constraint['syn']['val']['marking'].unify(b.constraint['syn'])!=None:
         a.constraint['orth'] += ','+b.constraint['orth']
         a.constraint['type']='PHRASE'
         a.constraint['syn']['val']['marking']=[]
         a.constraint['syn']['head']['case'] = b.constraint['syn']['head']['case']
         return a


#################################################  Verbal Rules

#Case1: a is V_LXM and b is V_ENGING_M_LXM
   elif issubclass(type(a),V_LXM)  and b.constraint['type'] is 'V_ENDING_M_LXM':
      if a.constraint['syn']['val']['marking'].unify(b.constraint['syn'])!=None:
         a.constraint['orth'] += ','+b.constraint['orth']
         a.constraint['syn']['val']['marking']=[]
         a.constraint['type']='PHRASE'
         return a


#Case2: a is V_NON_ENDING_LXM is and b is V_NON_ENDING_LXM
   elif a.constraint['type'] is'V_NON_ENDING_M_LXM' and b.constraint['type'] is 'V_NON_ENDING_M_LXM':
      if a.constraint['syn'].unify(b.constraint['syn'])!=None:
         a.constraint['orth'] += ','+b.constraint['orth']
         return a


#Case3: a is V_NON_ENDING_M_LXM is and b is V_ENDING_M_LXM
   elif a.constraint['type'] is'V_NON_ENDING_M_LXM'  and b.constraint['type'] is 'V_ENDING_M_LXM':
      if a.constraint['syn']['val']['marking'].unify(b.constraint['syn'])!=None:
         a.constraint['orth'] += ','+b.constraint['orth']
         a.constraint['syn']['val']['marking']=[]
         a.constraint['type']='V_ENDING_M_LXM'
         return a


#################################################  ADJ Rules

   elif a.constraint['type'] is 'ADJ_LXM' and b.constraint['type'] is 'ADJ_M_LXM':
      if a.constraint['syn']['val']['marking'].unify(b.constraint['syn'])!=None:
         a.constraint['orth'] += ','+b.constraint['orth']
         a.constraint['type']='WORD'
         a.constraint['syn']['val']['marking']=[]
         a.constraint['syn']['val']['mod']=N().constraint
         a.constraint['syn']['head']=ADJECTIVE().constraint
         return a

#################################################  ADV Rules
      
   elif a.constraint['type'] is 'ADJ_LXM' and b.constraint['type'] is 'ADV_M_LXM':
      if a.constraint['syn']['val']['marking'].unify(b.constraint['syn'])!=None:
         a.constraint['orth'] += ','+b.constraint['orth']
         a.constraint['type']='WORD'
         a.constraint['syn']['val']['marking']=[]
         a.constraint['syn']['val']['mod'] = V().constraint
         a.constraint['syn']['head']=ADVERB().constraint
         return a

   else:
      return a,b

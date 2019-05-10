#corresponding to hpsg_frag2.pl

from konlpy.tag import Kkma
parser = Kkma()

from nltk.featstruct import FeatStruct
from nltk.sem.logic import Variable, VariableExpression, Expression

## ========================   POS

class POS():
   def __init__(self):
      self.constraint = FeatStruct(pos = Variable('?a'))

class NOUN(POS):
   def __init__(self):
      POS.__init__(self)
      self.constraint['pos'] = 'noun'
      self.constraint['case'] = Variable('?b')

class DET(POS):
   def __init__(self):
      POS.__init__(self)
      self.constraint['pos'] = 'det'

class VERB(POS):
   def __init__(self):
      POS.__init__(self)
      self.constraint['pos'] = 'verb'

class ADJECTIVE(POS):
   def __init__(self):
      POS.__init__(self)
      self.constraint['pos'] = 'adjective'


class ADVERB(POS):
   def __init__(self):
      POS.__init__(self)
      self.constraint['pos'] = 'adverb'


class MARKER(POS):
   def __init__(self):
      POS.__init__(self)
      self.constraint['pos'] = 'marker'
      self.constraint['mark'] =Variable('?c')


class COMPLEMENTIZER(POS):
   def __init__(self):
      POS.__init__(self)
      self.constraint = self.constraint.unify(FeatStruct(pos = 'complementizer'))
      
#####========================================================== SIGN
      
class VALENCE():
   def __init__(self):
      self.constraint= FeatStruct(spr = Variable('?d'),comps = Variable('?e'), marking = Variable('?f'),mod = Variable('?g'))


class SYN():
   def __init__(self):
      self.constraint = FeatStruct(val=VALENCE().constraint, head = POS().constraint)


class SIGN():
   def __init__(self):
      self.constraint = FeatStruct(type = Variable('?h'), orth = Variable('?i') ,syn = SYN().constraint)


class SYN_SIGN(SIGN):
   def __init__(self):
      SIGN.__init__(self)
      self.constraint['type']="SYN_SIGN"


class LEX_SIGN(SIGN):
   def __init__(self):
      SIGN.__init__(self)
      self.constraint['type']="LEX_SIGN"


class PHRASE(SYN_SIGN):
   def __init__(self):
      SYN_SIGN.__init__(self)
      self.constraint['type']="PHRASE"

class WORD(SYN_SIGN,LEX_SIGN):
   def __init__(self):
      SYN_SIGN.__init__(self)
      LEX_SIGN.__init__(self)
      self.constraint['type']="WORD"
      
class LEXEME(LEX_SIGN):
   def __init__(self):
      LEX_SIGN.__init__(self)
      self.constraint['type']="LEXEME"


#####========================================================== WORD_Subclasses

#####  ========================  NOUN WORD
      
class N_WORD(WORD):
   def __init__(self):
      WORD.__init__(self)
      self.constraint['syn']['head']= NOUN().constraint
      self.constraint['syn']['val']['comps']=[]
      self.constraint['syn']['val']['spr']=[]
      self.constraint['syn']['val']['mod']=[]
      self.constraint['syn']['val']['marking']=N_M_LXM().constraint
      self.constraint['type']="N_WORD"


#####  ========================  ADVERN WORD
      
class ADV_WORD(WORD):
   def __init__(self):
      WORD.__init__(self)
      self.constraint['syn']['head']= ADVERB().constraint
      self.constraint['syn']['val']['comps']=[]
      self.constraint['syn']['val']['spr']=[]
      self.constraint['syn']['val']['marking']=[]
      self.constraint['syn']['val']['mod'] = V().constraint
      self.constraint['type']="ADV_WORD"


#####========================================================== LEXEME_Subclasses

##### ======================== MAERKER LXM
      
class M_LXM(LEXEME): #Marker lexeme
   def __init__(self):
      LEXEME.__init__(self)
      self.constraint['syn']['head']=MARKER().constraint
      self.constraint['syn']['val']['comps']=[]
      self.constraint['syn']['val']['spr']=[]
      self.constraint['syn']['val']['mod'] =[]
      self.constraint['syn']['val']['marking'] =Variable('?j')
      self.constraint['type']="M_LXM"

      
class N_M_LXM(M_LXM):
   def __init__(self):
      M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='noun'
      self.constraint['syn']['head']['case'] = Variable('?k') #nom/acc/dat
      self.constraint['type']="N_M_LXM"


class N_M_nom_LXM(N_M_LXM):
   def __init__(self):
      N_M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='noun'
      self.constraint['syn']['head']['case'] = 'nom' #nom/acc/dat
      self.constraint['type']="N_M_nom_LXM"
      

class N_M_acc_LXM(N_M_LXM):
   def __init__(self):
      N_M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='noun'
      self.constraint['syn']['head']['case'] = 'acc' #nom/acc/dat
      self.constraint['type']="N_M_acc_LXM"


class N_M_dat_LXM(N_M_LXM):
   def __init__(self):
      N_M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='noun'
      self.constraint['syn']['head']['case'] = 'dat' #nom/acc/dat
      self.constraint['type']="N_M_dat_LXM"
      

class V_M_LXM(M_LXM):
   def __init__(self):
      M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='verb'
      self.constraint['type']="V_M_LXM"


      
class V_ENDING_M_LXM(V_M_LXM):
   def __init__(self):
      V_M_LXM.__init__(self)
      self.constraint['syn']['val']['marking']=[]
      self.constraint['type']="V_ENDING_M_LXM"
      

class V_NON_ENDING_M_LXM(V_M_LXM):
   def __init__(self):
      V_M_LXM.__init__(self)
      self.constraint['syn']['val']['marking']= V_ENDING_M_LXM().constraint
      self.constraint['syn']['head']['mark']='verb'
      self.constraint['type']="V_NON_ENDING_M_LXM"


class ADJ_M_LXM(M_LXM):
   def __init__(self):
      M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='adjective'
      self.constraint['syn']['val']['marking']=[]
      self.constraint['type']="ADJ_M_LXM"


class ADV_M_LXM(M_LXM):
   def __init__(self):
      M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='adverb'
      self.constraint['syn']['val']['marking']=[]
      self.constraint['type']="ADV_M_LXM"


class NOUN_M_LXM(M_LXM):
   def __init__(self):
      M_LXM.__init__(self)
      self.constraint['syn']['head']['mark']='adverb'
      self.constraint['syn']['val']['marking']=[]
      self.constraint['type']="ADV_M_LXM"

      
##### ======================== VERB LXM
      
class V_LXM(LEXEME):
   def __init__(self):
      LEXEME.__init__(self)
      self.constraint['syn']['head']=VERB().constraint
      self.constraint['syn']['val']['comps']=Variable('?l')
      self.constraint['syn']['val']['mod'] = []
      spr = NP()
      spr.constraint['syn']['head']['case']='nom'
      self.constraint['syn']['val']['spr']=spr.constraint
      self.constraint['syn']['val']['marking']=V_ENDING_M_LXM().constraint
      self.constraint['type']="V_LXM"

class V_INTR_LXM(V_LXM):
   def __init__(self):
      V_LXM.__init__(self)
      self.constraint['syn']['val']['comps']=[]
      self.constraint['type']="V_INTR_LXM"

class V_TR_LXM(V_LXM):
   def __init__(self):
      V_LXM.__init__(self)
      comp = NP()
      self.constraint['syn']['val']['comps']=comp.constraint
      self.constraint['type']="V_TR_LXM"

class V_ACC_TR_LXM(V_LXM):
   def __init__(self):
      V_TR_LXM.__init__(self)
      self.constraint['syn']['val']['comps']['syn']['head']['case']='acc'
      self.constraint['type']="V_ACC_TR_LXM"

class V_DAT_TR_LXM(V_LXM):
   def __init__(self):
      V_TR_LXM.__init__(self)
      self.constraint['syn']['val']['comps']['syn']['head']['case']='dat'
      self.constraint['type']="V_DAT_TR_LXM"


class V_DI_LXM(V_LXM):
   def __init__(self):
      V_LXM.__init__(self)
      self.constraint['syn']['head']=VERB().constraint

      comp1 = NP()
      comp1.constraint['syn']['head']['case']='acc'
      comp2 = NP()
      comp2.constraint['syn']['head']['case']='dat'
      self.constraint['syn']['val']['comps']=comp1.constraint,comp2.constraint
      self.constraint['type']="V_DI_LXM"


##### ======================== ADJ LXM

class ADJ_LXM(LEXEME):
   def __init__(self):
      LEXEME.__init__(self)
      self.constraint['syn']['head']=Variable('?m')
      self.constraint['syn']['val']['spr']=[]
      self.constraint['syn']['val']['comps']=[]
      self.constraint['syn']['val']['mod'] = Variable('?n')
      self.constraint['syn']['val']['marking']=M_LXM().constraint
      self.constraint['type']="ADJ_LXM"


#####========================================================== MACRO



class NP():
   def __init__(self):
      self.constraint = FeatStruct(type = 'PHRASE',orth = Variable('?o'),
                                   syn=FeatStruct(head = NOUN().constraint ,
                                                  val=FeatStruct(spr=[],comps=[],mod = [],marking= [])))

class N():
   def __init__(self):
      self.constraint = FeatStruct(type = Variable('?p'), orth = Variable('?o'),
                                   syn=FeatStruct(head = NOUN().constraint ,
                                                  val=FeatStruct(spr=[],comps=[],mod = [],marking= Variable('?q'))))

class V():
   def __init__(self):
      self.constraint = FeatStruct(type = 'PHRASE',orth = Variable('?p'),
                                   syn=FeatStruct(head = VERB().constraint ,
                                                  val=FeatStruct(spr=Variable('?q'),comps=Variable('?r'),mod = [],marking= [])))


class VP():
   def __init__(self):
      self.constraint = FeatStruct(type = 'PHRASE',orth = Variable('?s'),
                                   syn=FeatStruct(head = VERB().constraint,
                                                  val=FeatStruct(spr=[],mod = [],comps=[],marking= [])))



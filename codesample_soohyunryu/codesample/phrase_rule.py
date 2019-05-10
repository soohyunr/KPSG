def phrase_rule(a,b):
   
   #Head_specifier_rule
   
   if b.constraint['syn']['val']['comps'] == [] and b.constraint['syn']['val']['spr']!= [] and b.constraint['syn']['val']['spr'].unify(a.constraint)!=None:
      b.constraint['orth'] = a.constraint['orth']+',' +b.constraint['orth']
      b.constraint['syn']['val']['spr']=[]
      return b

   #Head_comp_rule
   
   if b.constraint['syn']['val']['comps']!=[] and b.constraint['syn']['val']['comps'].unify(a.constraint)!=None:
      b.constraint['orth'] = a.constraint['orth']+','+b.constraint['orth']
      b.constraint['syn']['val']['comps']=[]
      return b

   
   #Modifier_rule
   
   if a.constraint['syn']['val']['mod']!= [] and a.constraint['syn']['val']['mod'].unify(b.constraint)!=None:
      b.constraint['orth'] = a.constraint['orth']+','+b.constraint['orth']
      return b

   else:
      return a,b







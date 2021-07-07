formula = "K4(ON(SO3)2)2"

if formula[-1].islower == True or formula[-1].isupper == True:
    formula += '1'
dic = {}
lst = []
c = ''

i = 0
while i < len(formula):
    if formula[i].isupper() == True:

#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

reload(sys)  
sys.setdefaultencoding('utf8')

#Lectura del fichero de texto
f = open ('instrumentos.txt')
freqdist = nltk.FreqDist()
words=nltk.word_tokenize(f.read())
fd = nltk.FreqDist(word.lower() for word in words)
print len(fd)
fdf= fd.most_common(150)

print 'Palabras del texto ordenadas por frecuencia'
t=''
for w in fdf:
    t='('+w[0]+','+str(w[1])+') '
    print t
#print t


dict ={}

dict['más']='ADV'

dict['su']='ADJ'

dict['.']='PUNT'
dict[',']='PUNT'

dict['la']='ART'
dict['las']='ART'
dict['el']='ART'
dict['los']='ART'
dict['lo']='ART'

dict['un']='DET'
dict['una']='DET'
dict['su']='DET'
dict['sus']='DET'

dict['a']='PREP'
dict['con']='PREP'
dict['de']='PREP'
dict['desde']='PREP'
dict['en']='PREP'
dict['entre']='PREP'
dict['para']='PREP'
dict['por']='PREP'
dict['sin']='PREP'

dict['que']='CONJ'
dict['y']='CONJ'
dict['o']='CONJ'

dict['se']='PRON'

#Aquí hay se añaden las palabras del diccionario y sus etiquetas




p=[
    (r'.+mente$',  'ADV'),

    (r'.+da$',     'VMP00SF'),
    (r'.+das$',    'VMP00SF'),
    (r'.+do$',     'VMP00SF'),
    (r'.+dos$',    'VMP00SF'),

    (r'.*ar$',     'VMN0000'),
    (r'.*er$',     'VMN0000'),
    (r'.*ir$',     'VMN0000'),

    # Primera conjugación

    (r'.*amos$',   'VMIP1P0'),
    (r'.*áis$',    'VMIP2P0'),

    (r'.*aba$',    'VMII1S0'),
    (r'.*abas$',   'VMII2S0'),
    (r'.*aba$',    'VMII3S0'),
    (r'.*ábamos$', 'VMII1P0'),
    (r'.*abais$',  'VMII2P0'),
    (r'.*aban$',   'VMII3P0'),

    (r'.*é$',      'VMIS1S0'),
    (r'.*aste$',   'VMIS2S0'),
    (r'.*ó$',      'VMIS3S0'),
    (r'.*amos$',   'VMIS1P0'),
    (r'.*asteis$', 'VMIS2P0'),
    (r'.*aron$',   'VMIS3P0'),

    (r'.*aré$',    'VMIF1S0'),
    (r'.*arás$',   'VMIF2S0'),
    (r'.*ará$',    'VMIF3S0'),
    (r'.*aremos$', 'VMIF1P0'),
    (r'.*aréis$',  'VMIF2P0'),
    (r'.*arán$',   'VMIF3P0'),
    
    (r'.*aría$',   'VMCP1S0'),
    (r'.*arías$',  'VMCP2S0'),
    (r'.*aría$',   'VMCP3S0'),
    (r'.*aríamos$','VMCP1P0'),
    (r'.*aríais$', 'VMCP2P0'),
    (r'.*arían$',  'VMCP3P0'),

    # Segunda conjugación
    (r'.*emos$',   'VMIP1P0'),
    (r'.*éis$',    'VMIP2P0'),

    (r'.*ía$',    'VMII1S0'),
    (r'.*ías$',   'VMII2S0'),
    (r'.*íamos$', 'VMII1P0'),
    (r'.*íais$',  'VMII2P0'),
    (r'.*ían$',   'VMII3P0'),

    (r'.*í$',    'VMII1S0'),
    (r'.*iste$',   'VMII2S0'),
    (r'.*ió$', 'VMII1P0'),
    (r'.*imos$',  'VMII2P0'),
    (r'.*isteis$',   'VMII3P0'),
    (r'.*ieron$',   'VMII3P0'),

    (r'.*eré$',   ''),
    (r'.*erás$',   ''),
    (r'.*erá$',   ''),
    (r'.*eremos$',   ''),
    (r'.*eréis$',   ''),
    (r'.*erán$',   ''),

    (r'.*ería$',   ''),
    (r'.*erías$',   ''),
    (r'.*ería$',   ''),
    (r'.*eríamos$',   ''),
    (r'.*eríais$',   ''),
    (r'.*erían$',   ''),
    
    (r'.*a$','NCFS'),
    (r'.*as$','NCFP'),
    #(r'.*os$','NCMP'),
    (r'.*s$','NCMP'),
    (r'.*$','NCMS'),
    #Aquí hay se añaden los patrones necesarios
    ]



rt=nltk.RegexpTagger(p)
taggedText=rt.tag(words)
for item in taggedText:
    if dict.has_key(item[0]):
        print item[0]+' '+dict[item[0]]
    else:
        print item[0]+' '+item[1]
    


sys.exit()

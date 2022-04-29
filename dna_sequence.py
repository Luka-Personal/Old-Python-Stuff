import re
d = {}

text = open('dna_sequences.txt').read()
while True:
 for some in [ x for x in re.split(r'\s+', text) if x]:

  if some.startswith('>'):
    key = some
    d[key] = ''
  else:
    value = d[key] + some
    d[key] = value

 for key in list(d):
    if key != key.replace('>', ''):
        d[key.replace('>', '')] = d[key]
        del d[key]

 c = input("\n"+"შეიყვანეთ სასურველი ID. (პროგრამიდან გასვლისთვის შეიყვანეთ exit): ")
 g=c.lower()
 if g=="exit":
   break
 temp_leqsikoni = d.get(c, None)

 print("\n"+ temp_leqsikoni if temp_leqsikoni else "\n"+"ასეთი ID-ით ვერ მოიძებნა დნმ სტრიქონი.")
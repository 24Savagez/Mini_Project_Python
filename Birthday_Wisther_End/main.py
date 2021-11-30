def auto_conjugate(subject, be, *verb1):
  verb_ing = ''
  for verb in (verb1):
    if verb[-3:] != 'ing':
      verb += 'ing'
      verb_ing += verb + " "
    else:
      verb_ing += verb + " " 
  print(subject, be, verb_ing[:-1].replace(' ',', ')+".")

auto_conjugate('i', 'am', 'working','eat','drink', 'cry', 'sleeping', 'read', 'walking')
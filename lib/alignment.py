import paradigm
import segment

# Try:
# knife = Form('naif')
# knives = Form('naivz')
# print "Alignment of /naif/ and /naivz/:", alignment.align_forms(knife, knives)

### PUBLIC FUNCTIONS ###

def align(form1, form2):
  '''Align two strings from their left edge
    Make sure that the empty slots are filled up with None, and that the two forms in order'''
  longer = form1 if len(form1) > len(form2) else form2
  zipped = []
  for i in range(len(longer)):
    try:
      zipped.append( (form1[i], form2[i]) )
    except IndexError:
      if longer == form1:
        zipped.append( (form1[i], None) )
      else:
        zipped.append( (None, form2[i]) )
  return zipped

def align_forms(form1, form2):
  '''Align two forms directly'''
  return align(form1.segments(), form2.segments())
  
def align_forms_with_ipa(form1, form2):
  '''Like align forms, but give back IPA strings instead of segment objects'''
  return map(lambda p: tuple(map(segment.try_ipa, (p[0], p[1]))), align_forms(form1, form2))

def align_forms_with_scores(form1, form2):
  '''Like align_forms, but give back an array of scores instead'''
  return map(lambda p: segment.similarity(segment.try_ipa(p[0]), segment.try_ipa(p[1])), align_forms(form1, form2))
  
  
  
import paradigm
import segment as seg

# Try:
# knife = Paradigm('naif', [('naivz', 0.9), ('naifs', 0.1)], ortho='knife', freq=2000)
# print "The word <" + knife.ortho + "> has frequency", knife.freq
# knife_sg = knife.base; knife_pl = knife.best_derivative()
# print "The best plural of /naif/ is:", map(lambda x: x.ipa, knife_pl.segments())
# print "Alignment of /naif/ and /naivz/:", alignment.align_forms_with_ipa(knife_sg, knife_pl)
# print "Alignment scores for /naif/ and /naivz/:", alignment.align_forms_with_scores(knife_sg, knife_pl)

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
        zipped.append( (form1[i], seg.Segment('')) )
      else:
        zipped.append( (seg.Segment(''), form2[i]) )
  return [zipped]

def align_forms(form1, form2):
  '''Align two forms directly'''
  return align(form1.segments(), form2.segments())
  
def align_forms_with_ipa(form1, form2):
  '''Like align forms, but give back IPA strings instead of segment objects'''
  new_forms = []
  for alignment in align_forms(form1, form2):
    new_forms.append(map(lambda x: tuple(map(lambda y: y.ipa, x)), alignment))
  return new_forms

  # return map(lambda p: tuple(map(lambda x: x.ipa, (p[0], p[1]))), align_forms(form1, form2))

def align_forms_with_scores(form1, form2):
  '''Like align_forms, but give back an array of scores instead'''
  return map(lambda x: map(lambda p: seg.similarity(*p), x), align_forms(form1, form2))
  
  
  
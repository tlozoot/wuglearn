import paradigm

# Try:
# knife = Form('naif')
# knives = Form('naivz')
# print "Alignment of /naif/ and /naivz/:", alignment.align_forms(knife, knives)

### PUBLIC FUNCTIONS ###

# Align two forms
# Make sure that the empty slots are filled up with None, and that the two forms in order
def align(form1, form2):
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

# Align two forms directly
def align_forms(form1, form2):
  return align(form1.segments(), form2.segments())
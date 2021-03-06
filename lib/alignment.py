import paradigm
import segment as seg

# Try:
# knife = Paradigm('naif', [('naivz', 0.9), ('naifs', 0.1)], ortho='knife', freq=2000)
# print "The word <" + knife.ortho + "> has frequency", knife.freq
# knife_sg = knife.base; knife_pl = knife.best_derivative()
# print "The best plural of /naif/ is:", map(lambda x: x.ipa, knife_pl.segments())
# print "Alignment of /naif/ and /naivz/:", alignment.align_forms_with_ipa(knife_sg, knife_pl)
# print "Alignment scores for /naif/ and /naivz/:", alignment.align_forms_with_scores(knife_sg, knife_pl)

''' Alignments are of the form [ (s1, t1), (s2, t2), ... ] '''

### PUBLIC FUNCTIONS ###

def align(seg_list1, seg_list2):
    '''Align two segment lists from their left edge
        Make sure that the empty slots are filled up with None, and that the two forms in order'''
    longer = seg_list1 if len(seg_list1) > len(seg_list2) else seg_list2
    zipped = []
    for i in range(len(longer)):
        try:
            zipped.append( (seg_list1[i], seg_list2[i]) )
        except IndexError:
            if longer == seg_list1:
                zipped.append( (seg_list1[i], seg.Segment('')) )
            else:
                zipped.append( (seg.Segment(''), seg_list2[i]) )
    return [zipped]

def align_forms(form1, form2):
    '''Align two forms directly'''
    return align(form1.segments(), form2.segments())
    
def align_with_ipa(form1, form2):
    return [ [ tuple(map(lambda s: s.ipa, p)) for p in a] for a in align(form1, form2) ]
    
def align_forms_with_ipa(form1, form2):
    '''Like align forms, but give back IPA strings instead of segment objects'''
    return [ [ tuple(map(lambda s: s.ipa, p)) for p in a ] for a in align_forms(form1, form2) ]

def align_forms_with_scores(form1, form2):
    '''Like align_forms, but give back an array of scores instead'''
    return [ [ seg.similarity(*p) for p in a ] for a in align_forms(form1, form2) ]
# coding=utf8

import alignment
import constraint as cons

def learn_constraints(word_list):
    '''Learn the faithfulness and markedness constraints based on a word list'''
    for con in cons.faithfuls + cons.markeds:
        for paradigm in word_list:
            for derivative in paradigm.derivatives:
                for a in alignment.align_forms(paradigm.base, derivative.form):
                    if con.type == 'faithfulness':
                        score = con.func(paradigm.base, derivative.form, a)
                    elif con.type == 'markedness':
                        score = con.func(derivative.form)                    
                    con.scores[derivative.form.to_u()] = (score * derivative.probability)
                

def test_wugs(wug_list):
    '''Get some wug plurals out of the constraints'''
    for wug in wug_list:
        for derivative in wug.derivatives:
            for a in alignment.align_forms(wug.base, derivative):
                for con in cons.faithfuls + cons.markeds:
                    if con.type == 'faithfulness':
                        score = con.func(wug.base, derivative, a)
                    elif con.type == 'markedness':
                        score = con.func(derivative)                
                    wug.scores[derivative.to_u()][con.func.__name__] = score * con.avg_score()
            

def write_output(word_list, wug_list):
    '''Output our sweet table... for R, since we have a nice web interface'''
    import constraint as cons # Why is this necessary??
    constraints = cons.faithfuls + cons.markeds
    outfile = open('learner_output.txt', 'w')
    outfile.write("Real words:\n")
    outfile.write("Paradigm\tVoiciness\tDerivative\tProb\t")
    outfile.write("\t".join(map(lambda x: x.func.__name__, constraints)) + "\tAverage\n")
    for paradigm in word_list:
        for derivative in paradigm.derivatives:
            outfile.write("\t".join([paradigm.base.to_u(), str(paradigm.voiciness()), derivative.form.to_u(), str(derivative.prob), '']))
            for cons in constraints:
                outfile.write(str(cons.scores[derivative.form.to_u()]) + "\t") 
            outfile.write("\n")
    outfile.write("\nAVERAGES:\t\t\t\t")
    for cons in constraints:
        outfile.write(str(cons.avg_score()) + "\t")
    outfile.write("\n\nWugs:\n")
    for wug in wug_list:
        for derivative in wug.derivatives:
            outfile.write("\t".join([wug.base.to_u(), str(wug.voiciness()), derivative.to_u(), str(wug.prob(derivative)), '']))
            for cons in constraints:
                outfile.write(str(wug.scores[derivative.to_u()][cons.func.__name__]) + "\t")
            outfile.write(str(wug.avg_score(derivative)) + "\n")    
    

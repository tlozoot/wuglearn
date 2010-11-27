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
            

def print_table(word_list, wug_list):
    '''Output our sweet table... to be replaced by a web interface'''
    import constraint as cons # Why is this necessary?
    constraints = cons.faithfuls + cons.markeds
    print "Paradigm\t        derivative\tp\t" ,
    print "\t".join(map(lambda x: x.func.__name__, constraints)), "\tAverage"
    for paradigm in word_list:
        print paradigm.base.to_u()
        for derivative in paradigm.derivatives:
            symbol = ' ☞ ' if derivative.form == paradigm.best_derivative() else '     '
            print "\t\t", symbol, derivative.form.to_u(), "\t", derivative.prob, "\t" ,
            for cons in constraints:
                print cons.scores[derivative.form.to_u()], "\t\t", 
            print
    print "\nAVERAGES\t\t\t\t",
    for cons in constraints:
        print cons.avg_score(), "\t\t",
    print "\n\nWUGS\n"
    for wug in wug_list:
        print wug.base.to_u(),
        for derivative in wug.derivatives:
            symbol = ' ☞ ' if derivative == wug.best_derivative() else '     '
            print "\t\t", symbol, derivative.to_u(), "\t", round(wug.prob(derivative), 4), "\t",
            for cons in constraints:
                print round(wug.scores[derivative.to_u()][cons.func.__name__], 4), "\t\t",
            print wug.avg_score(derivative)
    
    

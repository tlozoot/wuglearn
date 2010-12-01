datadir = "~/Documents/wuglearn/"
chartdir = "~/Documents/wuglearn/charts/"

# load data
setwd(datadir)
wugs = read.csv("learner_output.txt", sep="\t")
#summary(wugs)
#nrow(wugs)

u.wugs = unique(wugs[,c("Base","Ortho","HumanVoice","MinGenVoice","PredictedVoice")])
#nrow(u.wugs)
# done loading data


# prepare for making charts
setwd(chartdir)
chartmode = "pdf"
chartmode = "screen"
myfont = "Doulos SIL"; pointsize=10
myfont = "Linux Libertine"; pointsize=12
quartz.fnc = function(cwidth,cheight,cname) {
	if(chartmode=="screen") {
		quartz(width=cwidth,height=cheight)
	}
	if(chartmode=="pdf") {
		quartz(width=cwidth,height=cheight,type="pdf",file=cname)
	}
}
# done preparing for charts

# correlation tests
cor.test(u.wugs$HumanVoice, u.wugs$PredictedVoice)
cor.test(u.wugs$HumanVoice, u.wugs$MinGenVoice)

# plotting humans vs. wuglearn
quartz.fnc(cwidth=8,cheight=8,cname="r.dfgd.pdf")
par(family=myfont,ps=pointsize,mar=c(5,5,3,3));
plot(u.wugs$HumanVoice ~ u.wugs$PredictedVoice, type="n")
text(u.wugs$HumanVoice ~ u.wugs$PredictedVoice, label=u.wugs$Base)
abline(lm(u.wugs$HumanVoice ~ u.wugs$PredictedVoice))
if (chartmode=="pdf") {dev.off()}














































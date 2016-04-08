# -*- coding: utf-8 -*-
import matplotlib.pyplot as plot
from numpy import *
import time

class aln:
	
	def __init__(self,nomfichier):
		fichier = open(nomfichier,"r")
		
		self.start1=[]
		self.start2=[]
		self.stop1=[]
		self.stop2=[]
		self.alnlen=[]
		self.direct=[]
		
		for line in fichier.readlines() :
			l=line.strip().split(",")
			self.start1.append(l[6])
			self.start2.append(l[8])
			self.stop1.append(l[7])
			self.stop2.append(l[9])
			self.alnlen.append(l[3])
			if l[9]<l[8] :
				self.direct.append(-1)
			else :
				self.direct.append(1)
		fichier.close()
	
	def updateAln(self,start1,start2,stop1,stop2,alnlen,direct):
		self.start1=start1
		self.start2=start2
		self.stop1=stop1
		self.stop2=stop2
		self.alnlen=alnlen
		self.direct=direct
		
	def dotPlot(self,titre):
		plot.figure()
		#~ for i in range(len(sequence['start1'])):
			#~ if(sequence['dir'][i]==-1):
				#~ plot.plot([sequence['start1'][i],sequence['stop1'][i]],[sequence['start2'][i],sequence['stop2'][i]],color='black') 
			#~ else:
				#~ plot.plot([sequence['start1'][i],sequence['stop1'][i]],[sequence['start2'][i],sequence['stop2'][i]],color='red') 
		for i in range(len(self.start1)) :
			if self.direct[i]==-1 :
				plot.plot([self.start1[i],self.stop1[i]],[self.start2[i],self.stop2[i]])
			else :
				plot.plot([self.start1[i],self.stop1[i]],[self.stop2[i],self.start2[i]])

		plot.title(titre)
		plot.xlabel("2012")
		plot.ylabel("1348")
		plot.show()
		
	def filtre_taille(self,seuil):
		l=range(len(self.start1))
		l.reverse()
		for i in l :
			if int(self.alnlen[i])<seuil :
				del self.start1[i]
				del self.stop1[i]
				del self.start2[i]
				del self.stop2[i]
				del self.alnlen[i]
				del self.direct[i]
		
		print "Nb de segment apres filtrage : %d"%len(self.start1)

a=aln("1348vsCO92.csv")
a.dotPlot("Sans filtre")
a.filtre_taille(3000)
a.dotPlot("Filtre 1")

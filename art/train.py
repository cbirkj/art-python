#!/usr/bin/env python

import math
import numpy as np
import pandas as pd

class FuzzyArt:

	def __init__(self,x,rho,beta,alpha,nep):
		
		# Parameters
		self.rho = rho			# Free Parameter
		self.beta = beta		# Choice Parameter
		self.alpha = alpha		# Learning Rate
		self.nep = nep			# Number of epochs
		
		# Initilize arrays for training
		self.min = np.ones((len(x[0])*2,1))
		self.normI = np.ones((len(x[0])*2,1))
		self.normT = np.ones((len(x[0])*2,1))
		self.ch = np.zeros((len(x)*2,1))
		self.m = np.zeros((len(x)*2,1))	
		
	def match_choice(self,c,norm,normI,normT):
	
		"""
        Checks match criterion
        Compute choice equation
        Discovers best choice

        :param norm: minimum of input and templates
        :param normI: norm of input
        
        :return: returns category choice location
        """
        
		self.m[c] = norm/normI
		if self.m[c] < self.rho:
			self.ch[c] = 0
		else:
			self.ch[c] = norm/(self.beta + normT)
		
		return self.ch.argmax(axis=0)	
		
	def create(self,I,T,nc,j):
		"""
		Create new template
		
		:param I:		Input
		:param T: 		Template
		:param nc:		Number of Categories
		:param j:		Input matrix iteration value
		
		:return T:		Template matrix with new template
		"""
		
		for i in range(len(I)):
			T[i,nc-1] = I[i,j]
		return T
		
	def update(self,I,T,j,cmax):
		"""
		Update new template
		
		:param I:		Input
		:param T: 		Template
		:param cmax:	Maximum choice template location
		:param j:		Input matrix iteration value
		
		:return T:		Template matrix with update template
		"""
	
		for i in range(len(I)):
			T[i,cmax] = min(I[i,j],T[i,cmax])
		return T
	
	def template_options_loop(self,cmax,chmax,ch,nc):
		
		"""
		Match Criterion
		
		:param cmax:	Maximum choice (initialized to be -1)
		:param chmax:	Match Criterion (initialized to be -1)
		:param ch:		Template choice
		:param nc:		Number of Categories	
		
		:return cmax:	Maximum choice template location		
		
		while loop end when
		-> 
		"""
		
		neg = 0
		while chmax == -1:
			if self.m[ch] >= self.rho:
				chmax = self.ch[ch]
				cmax = ch
			elif neg == nc:
				chmax = 0
			else:
				self.ch[ch] = -1
				ch = self.ch.argmax(axis=0)
			
			neg += 1
		
		return cmax
			
	
	def art_train(self,I,T):
		"""
		Train ART - Create Template Matrix
		
		:param I:		Input
		:param T: 		Template
		:param cmax:	Maximum choice (initialized to be -1)
		:param chmax:	Match Criterion (initialized to be -1)
		"""
	
		''' Set first template as first input '''
		T[:,0] = I[:,0]
		
		for ep in range(self.nep):
			''' Initialize number of templates (nc) and loop (j) '''
			nc,j = 1,0
			
			while j < len(I[0]):
			
				for c in range(0,nc):
					''' Initialize chmax and cmax '''
					chmax = -1
					cmax = -1
				
					''' i loops through rows of matrix '''
					for i in range(len(I)):
						''' min of input (I[j]) and template (T[c]) '''
						self.min[i] = min(I[i,j],T[i,c])
						''' calculate the magnitude of min ''' 
						norm = self.min.sum()
						''' calculate the magnitude of I and T '''
						normI = I[:,j].sum()
						normT = T[:,c].sum()

					''' calculate choice & match '''
					ch = self.match_choice(c,norm,normI,normT)
					
				cmax = self.template_options_loop(cmax,chmax,ch,nc)
				
				if cmax == -1:
					''' Create New Template ''' 
					nc += 1
					T = self.create(I,T,nc,j)
				else:
					''' Update Existing Template ''' 
					T = self.update(I,T,j,cmax)
				
				j += 1
		
		return np.transpose(T[:,:nc])
	

def art_train(x,rho=0.9,beta=0.000001,alpha=1.0,nep=1):

	I = np.transpose(np.hstack([x,1 - x]))
	T = np.ones((len(x[0])*2,len(x)*2))
	
	ann = FuzzyArt(x,rho,beta,alpha,nep)
	T = ann.art_train(I,T)
	
	return T



if __name__ == '__main__':
    art_train()
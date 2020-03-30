#!/usr/bin/env python

import math
import numpy as np
import pandas as pd

class FuzzyArt:

	"""
	Test using ART Neural Network
		
	:param y: 			Input data
	:param I: 			Normalized & Complement Coded Input data
	:param rho:			Free parameter
	:param beta:		Choice Parameter
	:param alpha:		Learning Rate
	:param nep:			Number of epochs

	"""

	def __init__(self,y,I,T,rho,beta,alpha,nep):
		
		# Parameters
		self.rho = rho			# Free Parameter
		self.beta = beta		# Choice Parameter
		self.alpha = alpha		# Learning Rate
		self.nep = nep			# Number of epochs
		
		# Initilize arrays for training
		self.min = np.ones((len(y[0])*2,1))
		self.normI = np.ones((len(y[0])*2,1))
		self.normT = np.ones((len(y[0])*2,1))
		self.ch = np.zeros((len(y)*2,1))
		self.m = np.zeros((len(y)*2,1))
		
		# Initialize Input - Category Designation
		self.icaddt = np.zeros((1,len(y)))
		self.IC =  np.vstack([self.icaddt,I])
					
	
	def art_test_function(self,I,T):
		"""
		Test ART - Find Template(s)
		
		:param I:		Input
		:param T: 		Template
		"""

		''' Set first template as first input '''
		Tt = np.ones((len(I[0]),len(T)))
		
		for ep in range(self.nep):
			''' Initialize number loop (j) '''
			j = 0
			
			while j < len(I[0]):
			
				for c in range(len(T[0])):
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

					self.ch[c] = norm/(self.beta + normT)
					ch = self.ch.argmax(axis=0)
					self.m[c] = norm/normI
					
				if self.m[ch] >= self.rho:
					if self.ch[ch] > chmax:
						chmax = self.ch[ch]
						cmax = ch
						
				if cmax == -1:
					self.IC[0,j] = -1
					for i in range(len(T)):
						Tt[j,i] = 1
				else:
					self.IC[0,j] = ch
					for i in range(len(T)):
						Tt[j,i] = T[i,ch]
				
				j += 1
				
			cat = np.transpose(self.IC[:1,:])
		return cat
	

def data_test(y,T,rho=0.9,beta=0.000001,alpha=1.0,nep=1):

	I = np.transpose(np.hstack([y,1 - y]))
	T = np.transpose(T)
	
	ann = FuzzyArt(y,I,T,rho,beta,alpha,nep)
	cat = ann.art_test_function(I,T)
	
	C = np.hstack([cat,y])
	C = pd.DataFrame(C)
	C = C.rename(columns = {0:'Template'})

	return C



#if __name__ == '__main__':
#    art_test()
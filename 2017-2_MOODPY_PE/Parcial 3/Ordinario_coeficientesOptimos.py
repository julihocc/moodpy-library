#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:13:36 2017

@author: jdk2py
"""

import toMoodle as me
import numpy as np
import pandas as pd

#np.ranom.seed(1234)

carpeta = "Ordinario_coeficientesOptimos"

def impr(f, b=False):
    if b:
        print(str(f))


# In[2]:

def optCoefs(x, y):
    xmean=np.mean(x)
    ymean=np.mean(y)
    betan = np.sum((x-xmean)*(y-ymean))
    betad = np.sum((x-xmean)**2)
    beta=betan/betad
    alpha=ymean-beta*xmean
    
    return alpha, beta


totalPruebas = 0
imprimir = False
for test in range(totalPruebas):
    np.random.seed(1234)
    mx, a,b = np.random.randint(low=-100,high=100,size=3)
    sx, sr = np.random.poisson(10, size = 2)
    x=sx*np.random.randn(30)+mx
    res=sr*np.random.randn(30)
    y=a+b*x+res
    impr(optCoefs(x,y), imprimir)
    (alf, bet) = optCoefs(x,y)
    
    xTy = np.transpose([x,y])
    df1 = pd.DataFrame(xTy)
    df1.columns=(["X","Y"])
    impr(df1.head(), imprimir)
    html1 = df1.to_html()
    impr(html1, False)    

def generador(lista=[], imprimir=False): 
    impr("test:"+str(test+1)+32*"-", imprimir)
    nfilas = 10
    mx, a,b = np.random.randint(low=-100,high=100,size=3)
    sx, sr = np.random.poisson(10, size = 2)
    x=sx*np.random.randn(nfilas)+mx
    res=sr*np.random.randn(nfilas)
    y=a+b*x+res
    impr(optCoefs(x,y), imprimir)
    (alf, bet) = optCoefs(x,y)
    
    xTy = np.transpose([x,y])
    df1 = pd.DataFrame(xTy)
    df1.columns=(["X","Y"])
    impr(df1.head(), imprimir)
    html1 = df1.to_html()
    impr(html1, imprimir)   
    
    linea=[]    
    ejercicio = "<p> Calcule los coeficiente óptimos de la regresión lineal </p>"
    ejercicio += "$$ y = \\alpha + \\beta x $$ "
    ejercicio += "<p> con los datos de entrada X y de salida Y </p>"
    ejercicio += str(html1)
    
    linea.append(ejercicio)
    
    MC = "$$\\alpha$$ = "+me.NM(alf)
    MC += "$$\\beta$$ = "+me.NM(bet)
    #"<p> Estadístico chi-cuadrado ="+me.NM(chi2)+"</p>"
 
    #print MC
    linea.append(MC)

    #print(linea)
    lista.append(linea)
    


# In[5]:

bloques=15*3
ejercicios=[]

for k in range(bloques):
    generador(ejercicios)
mil_exes=[]; mil_sol=[]
for elemento in ejercicios:
    #print(elemento)
    mil_exes.append(elemento[0])
    mil_sol.append(elemento[1])
    
me.ExeToMoodle(carpeta, mil_exes, mil_sol)
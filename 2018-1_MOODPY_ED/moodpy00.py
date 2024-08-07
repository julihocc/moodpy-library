# -*- coding: utf-8 -*-

import datetime as dt
import time
import numpy as np
import os
#from sage.all import *

from sympy import pprint
from sympy import symbols
from sympy import latex
from sympy import solve
from sympy.matrices import *

import datetime as dt
import base64
import matplotlib.pyplot as plt
import os
import time

###to numeric question
def NM(x, entero=False, percent=False):    
    if entero:        
        x = int(x)
        sx = str(x)
        stol=str(0)
        return "{1:NM:="+sx+"}"
    if percent:
        x+=x*100.0
    else:
        sx = str(1.0*x)    
        tol = x*0.03
        stol = str(tol)
        #print sx, type(sx)
        return "{1:NM:="+sx+":"+stol+"}"

def wrint(frase, archivo, prueba=0):
  if prueba:
    print(frase)
  else:
    archivo.write(frase+"\n")

def toIm1(nom_grafica):
    return "</p>\n<p>\n<img src=\"@@PLUGINFILE@@/"+nom_grafica+"\" alt=\"\" width=\"783\" height=\"585\" />\n"
                  
def toIm2(nom_grafica, cod_grafica):
    return "<file name=\""+nom_grafica+"\" path=\"/\" encoding=\"base64\">"+cod_grafica+"</file>"
                  

def ExeToMoodle(leyenda, mihtml, penal = 0.5):
    K = len(mihtml)
    assert K!=0
    leyenda=str(leyenda)
    print(32*"-")
    print("Done: {}".format(dt.datetime.now()))
        #print(time.time())
    tiempo=str(time.time())
    foldername=leyenda
    print("Folder: {}".format(foldername))
    filename=leyenda+"-"+tiempo+".xml"
    print("Filename: {}".format(filename))
    print("#exes: {}".format(K))
    #print nombre
    
    if not os.path.isdir(foldername):
        os.makedirs(foldername)
    filename = os.path.join(foldername, filename)
    arx = open(filename, "w")#,  encoding="utf-8")
    
    arx.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    arx.write("<quiz>\n")
    for k in range(K):
      ejercicio=mihtml[k]
      ahora=str(time.time())
      arx.write("<!-- question: 0000000  -->"+"\n")
      arx.write("<question type=\"cloze\">\n")
      arx.write("<name>\n")
      arx.write("<text>"+leyenda+"-"+ahora+"</text>"+"\n")
      arx.write("</name>\n")
      arx.write("<questiontext format=\"html\">\n")
      arx.write(ejercicio)
      #arx.write(cdata(ejercicio))
      #creo que de aquí para abajo, nada cambia
      arx.write("</questiontext>\n")
      arx.write("<generalfeedback format=\"html\">\n")
      arx.write("<text><![CDATA[<pre> </pre>]]></text>\n")
      arx.write("</generalfeedback>\n")
      arx.write("<penalty>{}</penalty>\n".format(str(penal)))
      arx.write("<hidden>0</hidden>\n")
      arx.write("</question>\n")
    arx.write("</quiz>\n")
    arx.close() 

def keys2str(dic):
    dic2 = {}
    for _ in dic.keys():
        dic2[str(_)]=dic[_]
    return dic2

def sol2ans(sol, rat=False):
    ans = {}
    if rat:
        for s in sol.keys():
            print(s, type(s))
            xq = sol[s].as_numer_denom()
            num = "{}n".format(s)
            den = "{}d".format(s)
            print(num,den, xq)
            code = "{}= xq[0]".format(num)
            exec(code)
            code = "ans[\"{}\"]=NM(xn, entero=True)".format(num)
            exec(code)
            code = "ans[\"{}\"]=NM(xd, entero=True)".format(den)
            exec(code)
    return ans

def indSols():
    indicaciones = " <ul> <li> Simplifique las fracciones. </li> \
    <li> Si una solución es entera, utilice el denominador igual con uno. </li> \
    <li> Si la fracción es negativa, indique el signo en el numerador. </li> \
    <li> Ingrese las soluciones de menor a mayor </li> </ul>"    
    return indicaciones

def indFrac():
    indicaciones = " <ul> <li> Simplifique las fracciones. </li> \
    <li> Si la fracción representa entero, utilice el denominador igual con uno. </li> \
    <li> Si la fracción es negativa, indique el signo en el numerador. </li> \
    </ul>"
    return indicaciones

def master(generador, donde, cuantos, prueba = False):
    if prueba:
        bloques = 3
    else:
        bloques = cuantos
    mihtml=[]
    for k in range(bloques):
        ejercicio = generador(prueba)
        mihtml.append(ejercicio)        
    ExeToMoodle(donde, mihtml)

def quick(generador, donde, ready, impr=0):    
    if ready:
        master(generador, donde, ready)
    else:
        print(generador(impr))

def cdata(ejercicio):
    return "<text>\n<![CDATA[\n"+ejercicio+"\n]]>\n</text>"

def tagImg(nom_graf, alt="imagen", width="600", height="400"):
    code = """<p>
    <img src=\"@@PLUGINFILE@@/{}\" alt=\"{}\" width=\"{}\" height=\"{}\" />
    </p>""".format(nom_graf,alt,width,height)
    return code

def fileImg(nom_graf, cod_graf):
    code = """
    <file name=\"{}\" path=\"/\" encoding=\"base64\">{}</file>
    """.format(nom_graf, cod_graf)
    return code

def encodePlot(*args):
    plt.plot(*args)
    tiempo=str(time.time())
    filename=tiempo+".png"
    foldername="./temp"
    if not os.path.isdir(foldername):
        os.makedirs(foldername)
    folderFile = os.path.join(foldername, filename)
    plt.savefig(folderFile)
    plt.close()
    with open(folderFile, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode('utf-8')
    return filename, encoded
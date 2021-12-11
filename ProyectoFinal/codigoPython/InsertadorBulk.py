# -*- coding: utf-8 -*-
"""

@author: crlsc
"""

import sqlalchemy

from io import StringIO
import os


from sqlPython import *
from codigos import *
from dataframes import *

import regex

import time
import pandas as pd
import numpy as np
import csv
import psycopg2


start_time = time.time() #Comenzar contador


# Connection parameters
# Connect to the database
conn = psycopg2.connect(host="localhost",
                        port=5432,
                        user="postgres",
                        password="postgres",
                        database="prFinal")

cursor = conn.cursor()

#Borrar tablas

cursor.execute(dropTagno)
cursor.execute(dropTregion)
cursor.execute(dropTprovincia)
cursor.execute(dropTcomuna)
cursor.execute(dropTdeptoProv)
cursor.execute(dropTestadoEstab)
cursor.execute(dropTdependencia)
cursor.execute(dropTrural)
cursor.execute(dropTestablecimiento)

cursor.execute(dropTense)
cursor.execute(dropTense2)
cursor.execute(dropTgrado)
cursor.execute(dropTjornada)
cursor.execute(dropTtipoCurso)
cursor.execute(dropTdescrCurso)
cursor.execute(dropTcurso)

cursor.execute(dropTgeneroAl)
cursor.execute(dropTintegradoAl)
cursor.execute(dropTdiferencialAl)
cursor.execute(dropTalumno)

cursor.execute(dropTrama)
cursor.execute(dropTsector)
cursor.execute(dropTespecialidad)
cursor.execute(dropTsituacion)
cursor.execute(dropTsituacionR)
cursor.execute(dropTmencion)
cursor.execute(dropTfact_rendimiento)

conn.commit()

#Crear Tablas

cursor.execute(createTagno)
cursor.execute(createTregion)
cursor.execute(createTprovincia)
cursor.execute(createTcomuna)
cursor.execute(createTdeptoProv)
cursor.execute(createTestadoEstab)
cursor.execute(createTdependencia)
cursor.execute(createTrural)
cursor.execute(createTestablecimiento)

cursor.execute(createTense)
cursor.execute(createTense2)
cursor.execute(createTgrado)
cursor.execute(createTjornada)
cursor.execute(createTtipoCurso)
cursor.execute(createTdescrCurso)
cursor.execute(createTcurso)

cursor.execute(createTgeneroAl)
cursor.execute(createTintegradoAl)
cursor.execute(createTdiferencialAl)
cursor.execute(createTalumno)

cursor.execute(createTrama)
cursor.execute(createTsector)
cursor.execute(createTespecialidad)
cursor.execute(createTsituacion)
cursor.execute(createTsituacionR)
cursor.execute(createTmencion)
cursor.execute(createTfact_rendimiento)

conn.commit()


# Convert the dictionary into DataFrame 

def copy_from_stringio(conn, df, table):
    """
    Here we are going save the dataframe in memory 
    and use copy_from() to copy it to the table
    """
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False)
    buffer.seek(0)
    
    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_stringio() done")
    cursor.close()
    
def copy_from_stringioWithIndex(conn, df, table):
    """
    Here we are going save the dataframe in memory 
    and use copy_from() to copy it to the table
    """
    # save dataframe to an in memory buffer
    buffer = StringIO()
    df.to_csv(buffer, index=True, header=False)
    buffer.seek(0)
    
    cursor = conn.cursor()
    try:
        cursor.copy_from(buffer, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_stringio() done")
    cursor.close()
    
def copy_from_file(conn, df, table):
    """
    Here we are going save the dataframe on disk as 
    a csv file, load the csv file  
    and use copy_from() to copy it to the table
    """
    # Save the dataframe to disk
    tmp_df = "./tmp_dataframe.csv"
    df.to_csv(tmp_df, index_label='id', index=False, header=False)
    f = open(tmp_df, 'r')
    cursor = conn.cursor()
    try:
        cursor.copy_from(f, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        os.remove(tmp_df)
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_file() done")
    cursor.close()
    os.remove(tmp_df)

def copy_from_fileWithIndex(conn, df, table):
    """
    Here we are going save the dataframe on disk as 
    a csv file, load the csv file  
    and use copy_from() to copy it to the table
    """
    # Save the dataframe to disk
    tmp_df = "./tmp_dataframe.csv"
    df.to_csv(tmp_df, index_label='id', index=True, header=False)
    f = open(tmp_df, 'r')
    cursor = conn.cursor()
    try:
        cursor.copy_from(f, table, sep=",")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        os.remove(tmp_df)
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("copy_from_file() done")
    cursor.close()
    os.remove(tmp_df)
    
    
#-----------------------------------------------
# Firsts Dataframes code
#-----------------------------------------------   

##################################################

colsEnse = ['cod_ense', 'nom_ense']
lstEnse = []

for i in range(1000):
    if(ense(str(i))=="nope"):
        a=1#no hacer nada
    else:
        print(ense(str(i)))
        lstEnse.append([i,ense(str(i))])

dfEnse = pd.DataFrame(lstEnse, columns=colsEnse)        
print(dfEnse)

##################################################
colsGrado = ['cod_grado', 'cod_ense', 'nom_grado']
lstGrado = []

for i in range(1000):
    for j in range(20):
        if(gradp(str(i),str(j))=="nope"):
            a=1
        else:
            print(gradp(str(i),str(j)))
            lstGrado.append([j,i,gradp(str(i),str(j))])

dfGradp = pd.DataFrame(lstGrado, columns=colsGrado)        
print(dfGradp)


##################################################
colsPro = ['cod_pro', 'nom_pro']
lstPro = []

for i in range(16000):
    if(proRBD(str(i))=="nope"):
        a=1
    else:
        print(proRBD(str(i)))
        lstPro.append([i,proRBD(str(i))])

dfPro = pd.DataFrame(lstPro, columns=colsPro)        
print(dfPro)

##################################################Arreglar ['cod_grad', 'nom_grad', 'cod_ense']

##################################################

colsJ = ['cod_j', 'nom_j']
lstJ = []

for i in range(7):
    if(jornada(str(i))=="nope"):
        a=1
    else:
        print(jornada(str(i)))
        lstJ.append([i,jornada(str(i))])

dfJ = pd.DataFrame(lstJ, columns=colsJ)        
print(dfJ)

##################################################

colsTC = ['cod_TC', 'nom_TC']
lstTC = []

for i in range(99):
    if(tipoCurso(str(i))=="nope"):
        a=1
    else:
        print(tipoCurso(str(i)))
        lstTC.append([i,tipoCurso(str(i))])

dfTC = pd.DataFrame(lstTC, columns=colsTC)        
print(dfTC)

##################################################

colsDC = ['cod_DC', 'nom_DC']
lstDC = []

for i in range(7):
    if(descCurso(str(i))=="nope"):
        a=1
    else:
        print(descCurso(str(i)))
        lstDC.append([i,descCurso(str(i))])

dfDC = pd.DataFrame(lstDC, columns=colsDC)        
print(dfDC)

##################################################

colsGA = ['cod_GA', 'nom_GA']
lstGA = []

for i in range(7):
    if(generoAl(str(i))=="nope"):
        a=1
    else:
        print(generoAl(str(i)))
        lstGA.append([i,generoAl(str(i))])

dfGA = pd.DataFrame(lstGA, columns=colsGA)        
print(dfGA)

##################################################

colsIA = ['cod_IA', 'nom_IA']
lstIA = []

for i in range(7):
    if(intAl(str(i))=="nope"):
        a=1
    else:
        print(intAl(str(i)))
        lstIA.append([i,intAl(str(i))])

dfIA = pd.DataFrame(lstIA, columns=colsIA)        
print(dfIA)

##################################################

colsGDA = ['cod_GDA', 'nom_GDA']
lstGDA = []

for i in range(7):
    if(gdAl(str(i))=="nope"):
        a=1
    else:
        print(gdAl(str(i)))
        lstGDA.append([i,gdAl(str(i))])

dfGDA = pd.DataFrame(lstGDA, columns=colsGDA)        
print(dfGDA)

##################################################

colsRA = ['cod_RA', 'nom_RA']
lstRA = []

for i in range(1000):
    if(rama(str(i))=="nope"):
        a=1
    else:
        print(rama(str(i)))
        lstRA.append([i,rama(str(i))])

dfRA = pd.DataFrame(lstRA, columns=colsRA)        
print(dfRA)

##################################################

colsSec = ['cod_Sec', 'nom_Sec']
lstSec = []

for i in range(1000):
    if(sector(str(i))=="nope"):
        a=1
    else:
        print(sector(str(i)))
        lstSec.append([i,sector(str(i))])

dfSec = pd.DataFrame(lstSec, columns=colsSec)        
print(dfSec)


##################################################

colsEsp = ['cod_Esp', 'nom_Esp']
lstEsp = []

for i in range(93008):
    if(espe(str(i))=="nope"):
        a=1
    else:
        print(espe(str(i)))
        lstEsp.append([i,espe(str(i))])

dfEsp = pd.DataFrame(lstEsp, columns=colsEsp)        
print(dfEsp)


##################################################






# copy the dataframe to SQL
dfAgno = pd.DataFrame(dataAgno) 
dfRegiones = pd.DataFrame(dataRegiones) 
dfProvincia = pd.DataFrame(dataProvincia) 
dfEstadoEstab = pd.DataFrame(dataEstadoEstab) 
dfDepe = pd.DataFrame(dataDepe) 

dfEnse2 = pd.DataFrame(dataEnse2) 

dfSF = pd.DataFrame(dataSirFin) 
dfSFR = pd.DataFrame(dataSirFinR) 

dfMens = pd.DataFrame(dataMen) 


dfRur = pd.DataFrame(dataRural) 
dfInte = pd.DataFrame(dataIntegrado) 
dfDife = pd.DataFrame(dataDiferencial) 


copy_from_stringio(conn, dfAgno, 'agno') # copy the dataframe to SQL
copy_from_stringio(conn, dfRegiones, 'region') # copy the dataframe to SQL
copy_from_stringio(conn, dfProvincia, 'provincia') # copy the dataframe to SQL
copy_from_stringio(conn, dfEstadoEstab, 'estadoEstab') # copy the dataframe to SQL
copy_from_stringio(conn, dfDepe, 'dependencia') # copy the dataframe to SQL
copy_from_stringio(conn, dfEnse, 'ense') # copy the dataframe to SQL
copy_from_stringio(conn, dfEnse2, 'ense2') # copy the dataframe to SQL
copy_from_stringio(conn, dfGradp, 'grado') # copy the dataframe to SQL
copy_from_stringio(conn, dfJ, 'jornada') # copy the dataframe to SQL
copy_from_stringio(conn, dfTC, 'tipoCurso') # copy the dataframe to SQL
copy_from_stringio(conn, dfDC, 'descrCurso') # copy the dataframe to SQL
copy_from_stringio(conn, dfGA, 'generoAl') # copy the dataframe to SQL
copy_from_stringio(conn, dfRA, 'rama') # copy the dataframe to SQL
copy_from_stringio(conn, dfSec, 'sector') # copy the dataframe to SQL
copy_from_stringio(conn, dfEsp, 'especialidad') # copy the dataframe to SQL
copy_from_stringio(conn, dfMens, 'mencion') # copy the dataframe to SQL
copy_from_stringio(conn, dfSF, 'situacion') # copy the dataframe to SQL
copy_from_stringio(conn, dfSFR, 'situacionR') # copy the dataframe to SQL
copy_from_stringio(conn, dfDife, 'diferencialAl') # copy the dataframe to SQL
copy_from_stringio(conn, dfInte, 'integradoAl') # copy the dataframe to SQL
copy_from_stringio(conn, dfRur, 'rural') # copy the dataframe to SQL


#-----------------------------------------------
# Main code
#-----------------------------------------------
cont = 0  
countCurso=0
countRendimiento=0

#funcion para reemplazar los ' de los nombres por '', para no tener errores con el sql
def replaceABwithC(input, pattern, replaceWith): 
    return input.replace(pattern, replaceWith) 


rendCount=0

list_comuna = []
list_depto = []

list_estab = []
list_curso = []
list_alumno = []
list_rendi = []

countCursoInicial=0
countCursoFinal=0

countRenInicial=0
countRenFinal=0

cantidadArchivos=10

for i in range(cantidadArchivos):

    csvAgno=i
    directory = ('Rendimiento por estudiante 201' + str(csvAgno) + '_0.csv')
    
    df = pd.read_csv(directory, encoding="unicode_escape",delimiter=';', low_memory=False)
    
    
    #df2.columns = df.columns.str.upper()
    dfOriginal=df
    
    dfOriginal['CEROS'] = '0'
    dfOriginal['CEROS2'] = '0'
    dfOriginal['CEROS3'] = '0'
    dfOriginal['CEROS4'] = '0'
    dfOriginal['MENOS1'] = '-1'
    dfOriginal['MENOS12'] = '-1'

    countCursoFinal=countCursoFinal+len(dfOriginal)#ejemplo: 3.000.000 + 3.200.100 = 6.200.100
    
    dfOriginal['COD_CURSO'] = np.array(list(range(countCursoInicial,countCursoFinal)))

    countCursoInicial=countCursoInicial+len(dfOriginal) #ejemplo: 3.200.100
    #entonces el siguiente dataframe de curso va a ir del 3.200.100 al 6.200.100

    countRenFinal=countRenFinal+len(dfOriginal)#ejemplo: 3.000.000 + 3.200.100 = 6.200.100
    
    dfOriginal['COD_REN'] = np.array(list(range(countRenInicial,countRenFinal)))

    countRenInicial=countRenInicial+len(dfOriginal) 
    ###########################
    dfOriginal = dfOriginal.replace(',', '.', regex=True)
    dfOriginal = dfOriginal.replace("'", "''", regex=True)
    dfOriginal = dfOriginal.replace('"', "''", regex=True)
    dfOriginal = dfOriginal.replace(' ', "0", regex=True)


    ####COMUNAS#################################################    
    df2=dfOriginal
    df2.columns = df2.columns.str.upper()
    dfComunas = df2.drop_duplicates(subset=["COD_COM_RBD"])
    ####DEPTO#################################################    
    df2=dfOriginal
    df2.columns = df2.columns.str.upper()
    dfDepto = df2
    ####ESTABLECIMIENTOS#################################################    
    df2=dfOriginal
    df2.columns = df2.columns.str.upper()
    dfEstab = df2.drop_duplicates(subset=["RBD"])
    ###CURSOS###########################################################
    df2=dfOriginal
    dfCursos = df2
    
    ###ALUMNOS###########################################################
   
    df2=dfOriginal
    df2.columns = df2.columns.str.upper()
    dfAlumnos = df2.drop_duplicates(subset=["MRUN"])
    ##############################################################

    df2=dfOriginal
    dfRendimiento = df2

    ##############################################################

    agno=-1
    cod_reg_rbd=-1
    cod_pro_rbd=-1
    cod_com_rbd=-1
    nom_com_rbd=-1
    cod_deprov_rbd=-1
    nom_deprov_rbd=-1
    estado_estab=-1
    cod_depe=-1
    rbd=-1
    dgv_rbd=-1
    nom_rbd=-1
    rural_rbd=-1

    cod_ense=-1
    cod_ense2=-1
    cod_grado=-1
    cod_jor=-1
    cod_tip_cur=-1
    cod_des_cur=-1
    let_cur=-1
    cod_curso=-1
    
    gen_alu=-1
    mru=-1
    fec_nac_alu=-1
    int_alu=-1
    gd_alu=-1
    
    cod_rama=-1
    cod_sec=-1
    cod_espe=-1
    sit_fin=-1
    sit_fin_r=-1
    cod_men=-1
    
    cod_reg_alu=-1
    cod_com_alu=-1
    prom_gral=-1
    asistencia=-1
    
    ceros=-1
    ceros2=-1
    ceros3=-1
    ceros4=-1
    menos1=-1
    menos12=-1
    
    cod_rendimiento=-1
    
    countF=0
    header = list(dfOriginal.columns.values)

    # getting length of list
    print(header)
    length = len(header)

    #obtener numero de la columnas
    for h in range(length):
        if (header[h].upper() =="CEROS"):
            ceros=h
        if (header[h].upper() =="CEROS2"):
            ceros2=h
        if (header[h].upper() =="CEROS3"):
            ceros3=h
        if (header[h].upper() =="CEROS4"):
            ceros4=h
        if (header[h].upper() =="MENOS1"):
            menos1=h
        if (header[h].upper() =="MENOS12"):
            menos12=h
        if (header[h].upper() =="AGNO" or header[h] =="\ufeffagno" or header[h] =="\ufeffAGNO" or header[h] =="Ï»¿AGNO"):
            agno=h
        if (header[h].upper() =="RBD"):
            rbd=h
        if (header[h].upper() =="DGV_RBD"):
            dgv_rbd=h
        if (header[h].upper() =="NOM_RBD"):
            nom_rbd=h       
        if (header[h].upper() =="COD_REG_RBD"):
            cod_reg_rbd=h
        if (header[h].upper() =="COD_PRO_RBD"):
            cod_pro_rbd=h
        if (header[h].upper()=="COD_COM_RBD"):
            cod_com_rbd=h
        if (header[h].upper()=="NOM_COM_RBD"): #nombre se usa
            nom_com_rbd=h
        if (header[h].upper()=="COD_DEPROV_RBD"):
            cod_deprov_rbd=h
        if (header[h].upper()=="NOM_DEPROV_RBD"):#nombre se usa
            nom_deprov_rbd=h
        if (header[h].upper()=="COD_DEPE"):
            cod_depe=h
        if (header[h].upper()=="COD_DEPE2"): #depe2 se elimino
            agnox=h       
        if (header[h].upper()=="RURAL_RBD"):
            rural_rbd=h
        if (header[h].upper()=="ESTADO_ESTAB"):
            estado_estab=h
        ################################################
        if (header[h].upper()=="COD_ENSE"):
            cod_ense=h
        if (header[h].upper()=="COD_ENSE2"):
            cod_ense2=h
        if (header[h].upper()=="COD_GRADO"):
            cod_grado=h
        if (header[h].upper()=="LET_CUR"):
            let_cur=h
        if (header[h].upper()=="COD_JOR"):
            cod_jor=h
        if (header[h].upper()=="COD_TIP_CUR"):
            cod_tip_cur=h       
        if (header[h].upper()=="COD_CURSO"):
            cod_curso=h              
        ################################################
        if (header[h].upper()=="MRUN"):
            mrun=h
        if (header[h].upper()=="GEN_ALU"):
            gen_alu=h
        if (header[h].upper()=="FEC_NAC_ALU"):
            fec_nac_alu=h
        if (header[h].upper()=="GD_ALU"):
            gd_alu=h
        if (header[h].upper()=="COD_REG_ALU"):
            cod_reg_alu=h
        if (header[h].upper()=="COD_COM_ALU"):
            cod_com_alu=h
        if (header[h].upper()=="NOM_COM_ALU"): #nombre no se usa
            agnox=h
        ################################################
        if (header[h].upper()=="COD_RAMA"):
            cod_rama=h       
        if (header[h].upper()=="COD_SEC"):
            cod_sec=h
        if (header[h].upper()=="COD_ESPE"):
            cod_espe=h
        if (header[h].upper()=="PROM_GRAL"):
            prom_gral=h
        if (header[h].upper()=="ASISTENCIA"):
            asistencia=h
        if (header[h].upper()=="SIT_FIN"):
            sit_fin=h
        if (header[h].upper()=="SIT_FIN_R" or header[h].upper()=="SIT_FINAL_R" or header[h].upper() =="SIT_FIN_R,"):
            sit_fin_r=h
        if (header[h].upper() =="COD_REN"):
            cod_rendimiento=h
        #distintos a 2015
        if (header[h].upper()=="COD_DES_CUR"):
            cod_des_cur=h
        if (header[h].upper()=="INT_ALU"):
            int_alu=h
        if (header[h].upper()=="COD_MEN"):
            cod_men=h
    
    
    
    # Tabla comuna COD_COM_RBD
    dfComunas2 = dfComunas.iloc[:, [cod_com_rbd,nom_com_rbd]].copy()
    list_comuna.append(dfComunas2)

    #Tabla dept
    if(cod_deprov_rbd != -1):
        dfDepto2 = dfDepto.iloc[:, [cod_deprov_rbd,nom_deprov_rbd]].copy()
        list_depto.append(dfDepto2)
    
    # Tabla establecimiento
    if(cod_pro_rbd != -1):
        if(cod_deprov_rbd != -1):
                dfEstab2 = dfEstab.iloc[:, [rbd,dgv_rbd,nom_rbd,cod_pro_rbd,rural_rbd,estado_estab,cod_depe,cod_reg_rbd,cod_com_rbd,cod_deprov_rbd]].copy()
                list_estab.append(dfEstab2)
        
        else:
            dfEstab2 = dfEstab.iloc[:, [rbd,dgv_rbd,nom_rbd,cod_pro_rbd,rural_rbd,ceros2,cod_depe,cod_reg_rbd,cod_com_rbd,ceros3]].copy()
            list_estab.append(dfEstab2)     
    else:    
        
        dfEstab2 = dfEstab.iloc[:, [rbd,dgv_rbd,nom_rbd,ceros,rural_rbd,ceros2,cod_depe,cod_reg_rbd,cod_com_rbd,ceros3]].copy()
        list_estab.append(dfEstab2)
            
  
    # Tabla curso
    

    if(cod_jor != -1):
        if(cod_ense2 != -1):
            if(cod_des_cur != -1):
                dfCursos2 = dfCursos.iloc[:, [cod_curso,cod_ense,cod_ense2,cod_grado,let_cur,cod_jor,cod_tip_cur,cod_des_cur]].copy()
                list_curso.append(dfCursos2)
                
            else:
                dfCursos2 = dfCursos.iloc[:, [cod_curso,cod_ense,cod_ense2,cod_grado,let_cur,cod_jor,cod_tip_cur,ceros4]].copy()
                list_curso.append(dfCursos2)
                
                
        else:
            dfCursos2 = dfCursos.iloc[:, [cod_curso,cod_ense,ceros,cod_grado,let_cur,cod_jor,cod_tip_cur,ceros4]].copy()
            list_curso.append(dfCursos2)
                
            
        
    else:
        dfCursos2 = dfCursos.iloc[:, [cod_curso,cod_ense,ceros,cod_grado,let_cur,ceros2,ceros3,ceros4]].copy()
        list_curso.append(dfCursos2)
        
    # Tabla alumno
    

    if(int_alu != -1):
        if(gd_alu != -1):
            dfAlumnos2 = dfAlumnos.iloc[:, [mrun,gen_alu,fec_nac_alu,int_alu,gd_alu]].copy()
            list_alumno.append(dfAlumnos2)
        else:
            dfAlumnos2 = dfAlumnos.iloc[:, [mrun,gen_alu,fec_nac_alu,int_alu,menos12]].copy()
            list_alumno.append(dfAlumnos2)
    else:
        if(gd_alu != -1):
            dfAlumnos2 = dfAlumnos.iloc[:, [mrun,gen_alu,fec_nac_alu,menos1,gd_alu]].copy()
            list_alumno.append(dfAlumnos2)
        else:
            dfAlumnos2 = dfAlumnos.iloc[:, [mrun,gen_alu,fec_nac_alu,menos1,menos12]].copy()
            list_alumno.append(dfAlumnos2)

    #tabla fact_rendimiento
    if(cod_men != -1): #si hay men, hay todo
        dfRendimiento2 = dfRendimiento.iloc[:, [cod_rendimiento,agno,rbd,cod_curso,mrun,asistencia,sit_fin,sit_fin_r,cod_men,cod_espe,cod_rama,cod_sec,prom_gral]].copy()
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].str.replace('.', '')
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('1', '10')
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('2', '20')
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('3', '30')
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('4', '40')
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('5', '50')
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('6', '60')
        dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('7', '70')
        list_rendi.append(dfRendimiento2) 

    else:
        if(cod_rama != -1): #si hay rama, todo menos men
            dfRendimiento2 = dfRendimiento.iloc[:, [cod_rendimiento,agno,rbd,cod_curso,mrun,asistencia,sit_fin,sit_fin_r,ceros2,cod_espe,cod_rama,cod_sec,prom_gral]].copy()
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].str.replace('.', '')
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('1', '10')
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('2', '20')
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('3', '30')
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('4', '40')
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('5', '50')
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('6', '60')
            dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('7', '70')
            list_rendi.append(dfRendimiento2)             
            
        else:#no rama
            if(cod_sec != -1): #si sec, si espe
                dfRendimiento2 = dfRendimiento.iloc[:, [cod_rendimiento,agno,rbd,cod_curso,mrun,asistencia,sit_fin,sit_fin_r,ceros2,cod_espe,ceros3,cod_sec,prom_gral]].copy()
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].str.replace('.', '')
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('1', '10')
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('2', '20')
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('3', '30')
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('4', '40')
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('5', '50')
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('6', '60')
                dfRendimiento2["PROM_GRAL"]=dfRendimiento2["PROM_GRAL"].replace('7', '70')
                list_rendi.append(dfRendimiento2)  
    #final ciclo for

############################################################################################
dfComunaMain = pd.DataFrame(columns=['COD_COM_RBD','NOM_COM_RBD'])   

for i in range(cantidadArchivos):
    new_cols = {x: y for x, y in zip(list_comuna[i].columns, dfComunaMain.columns)}
    dfComunaMain = dfComunaMain.append(list_comuna[i].rename(columns=new_cols))
       

print(dfComunaMain)

#merged_estab = pd.concat(dfEstabMain)

#print(merged_estab)

dfComunaMain['COD_COM_RBD'] = dfComunaMain['COD_COM_RBD'].astype(int)

dfComunaMain2 = dfComunaMain.drop_duplicates(subset=['COD_COM_RBD'], keep="first", inplace=False)
copy_from_stringio(conn, dfComunaMain2, 'comuna')

############################################################################################
dfDeptoMain = pd.DataFrame(columns=['COD_DEPROV_RBD','NOM_DEPROV_RBD'])   
dfDeptoProv = pd.DataFrame(dataDeptoProvincia) 
list_depto.append(dfDeptoProv)

for i in range(6):
    new_cols = {x: y for x, y in zip(list_depto[i].columns, dfDeptoMain.columns)}
    dfDeptoMain = dfDeptoMain.append(list_depto[i].rename(columns=new_cols))
       

print(dfDeptoMain)

#merged_estab = pd.concat(dfEstabMain)

#print(merged_estab)

dfDeptoMain['COD_DEPROV_RBD'] = dfDeptoMain['COD_DEPROV_RBD'].astype(int)

dfDeptoMain2 = dfDeptoMain.drop_duplicates(subset=['COD_DEPROV_RBD'], keep="first", inplace=False)
copy_from_stringio(conn, dfDeptoMain2, 'deptoProv')

############################################################################################
dfEstabMain = pd.DataFrame(columns=['RBD','DGV_RBD','NOM_RBD','COD_PRO_RBD','RURAL_RBD','ESTADO_ESTAB','COD_DEPE','COD_REG_RBD','COD_DEPROV_RBD'])   
       
for i in range(cantidadArchivos):
    new_cols = {x: y for x, y in zip(list_estab[i].columns, dfEstabMain.columns)}
    dfEstabMain = dfEstabMain.append(list_estab[i].rename(columns=new_cols))
       

print(dfEstabMain)

#merged_estab = pd.concat(dfEstabMain)

#print(merged_estab)
     
dfEstabMain = dfEstabMain.drop_duplicates(subset=["RBD"])
copy_from_stringio(conn, dfEstabMain, 'establecimiento')

############################################################################################
dfCursoMain = pd.DataFrame(columns=['COD_CURSO','COD_ENSE','COD_ENSE2','COD_GRADO','LET_CUR','COD_JOR','COD_TIP_CUR','COD_DES_CUR'])   

for i in range(cantidadArchivos):
    print(list_curso[i].columns.values)
    copy_from_stringio(conn, list_curso[i], 'curso')

      
############################################################################################
dfAlumnoMain = pd.DataFrame(columns=['MRUN','GEN_ALU','FEC_NAC_ALU','INT_ALU','GD_ALU'])   

for i in range(cantidadArchivos):
    new_cols = {x: y for x, y in zip(list_alumno[i].columns, dfAlumnoMain.columns)}
    dfAlumnoMain = dfAlumnoMain.append(list_alumno[i].rename(columns=new_cols))
       

dfAlumnoMain['MRUN'] = dfAlumnoMain['MRUN'].astype(int)
dfAlumnoMain2 = dfAlumnoMain.drop_duplicates(subset=["MRUN"])   


print(dfAlumnoMain2)
  
copy_from_stringio(conn, dfAlumnoMain2, 'alumno')

############################################################################################
dfRendimientoMain = pd.DataFrame(columns=['COD_REN','AGNO','RBD','COD_CURSO','MRUN','ASISTENCIA','SIT_FIN','SIT_FIN_R','COD_MEN','COD_ESPE','COD_RAMA','COD_SEC','PROM_GRAL'])   


print(list_rendi)

for i in range(cantidadArchivos):
    print(list_rendi[i].columns.values)
    copy_from_stringio(conn, list_rendi[i], 'fact_rendimiento')


conn.close() # close the connection



print("FIN") 
print("--- %s seconds ---" % (time.time() - start_time))










import md5
import time
import uuid
import os

#Tiempo en segundos
MAXTIME = 60

#Contamos por cuantos 0s empieza el resumen
#Count by how many 0s the summary starts with
def count0(s):
    i =0
    count = 0
    while i < len(s):
        if s[i] == "0":
            count += 1
        else:
            break
        i += 1
    return count


def AlteracionFicheroMD5(F):
    #abrimos el fichero original de texto
    #open the original text file
    text = open(F)
    #guardamos en una lista las lineas escritas
    # we save in a list the written lines
    lineas = text.readlines()
    
    #Establecemos los parametros de inicio
    #Let's set the starting parameters
    start = time.time()
    end = time.time()
    max0 = 0

    while True :
        #eliminamos el fichero del intento anterior
        #delete the file from the previous attempt
        try:
            os.remove("nuevoFichero.txt")
        except :
            pass
        #Generamos un string hexadecimal aleatorio
        #Generate a random hexadecimal string
        s = uuid.uuid4().hex
        
        #Creamos nuestro nuevo fichero con permisos de escribit extra 'w+'
         #Create our new file with extra 'w+' write permissions
        newFile = open("nuevoFichero.txt","a")
        #Escribimos las lineas del otro fichero ademas de añadir los 8 primeros caracteres de s
        #Write the lines of the other file plus add the first 8 characters of s
        newFile.writelines(lineas)
        #Combertimos s a un string con un casteo str('')
        newFile.write( str(s)[:8] + " G13" )
        #Cerramos el fichero para guardar los cambios
        #Close the file to save the changes.
        newFile.close()
        #obtenemos su resumen md5 y contamos sus 0s
        #We get your md5 digest and count your 0s.
        brief = md5.md5(newFile.name)
        ceros = count0(str(brief))
        #Si tenemos mas 0s que el maximo anterior actualizamos los valores del resumen y el maximo de 0s
        #If we have more 0s than the previous maximum, we update the values of the summary and the maximum 0s.
        if ceros > max0:
            max0 = ceros
            res = brief
            #Borramos el resultado anterior si existe
             #Delete the previous result if it exists
            try:
                os.remove("./ficheroSemana12.txt")
            except:
                pass
            #Renombramos el fichero para no eliminarlo en la siguiente rotacion
            #Rename the file so as not to delete it in the next rotation.
            os.rename(r"./nuevoFichero.txt",r"./ficheroSemana12.txt")
        #Calculamos el tiempo al terminar
        #We calculate the time at the end
        end = time.time()
        #Sacamos cuanto hemos tardado en segundos
        #if ceros >= 6:
        #    return
        
    #Eliminar el fichero basura en caso de haberlo
    #Delete the junk file if any
    try:
        os.remove("nuevoFichero.txt")
    except :
        pass
    print(res)

AlteracionFicheroMD5("SGSSI-20.CB.12.txt")
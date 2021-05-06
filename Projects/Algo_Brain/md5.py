#Libreria con algoritmos de encriptacion
#Library with encryption algorithms
import hashlib as hs



def md5(filename):
    #Usando el fichero que se habre como variable 'f'
    #Using the file to be opened as variable 'f'.
    with open(filename,"rb") as f:
        #Leemos Byte a Byte
        #We read Byte by Byte
        bytes = f.read() # read file as bytes
        #Cogemos el conjunto de bytes y sacamos el resumen md5
        #We take the set of bytes and extract the md5 digest.
        readable_hash = hs.md5(bytes).hexdigest();
        return readable_hash
print(md5("ficheroSemana12.txt"))
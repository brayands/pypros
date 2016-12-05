#!/usr/bin/env python
# -*- coding: utf8 -*-
import subprocess, glob,  time,  socket, os

import sys
from subprocess import Popen, PIPE

def check_execs(*progs):
    """Check if the programs are installed, if not exit and report."""
    for prog in progs:
        try:
            Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
        except OSError:
            msg = 'The {0} program is necessary to run this script'.format(prog)
            return 1
    return

def main():
    final = 0
    while(final == 0):
        subprocess.call('clear')
        print "Bienvenid@ a PyPros, el script para preprocesar los formatos HAML y SASS"
        print "Lista de preprocesadores:"
        print " 1) Haml"
        print " 2) Sass"
        print " 3) Servidor Local"
        print " 4) Salir"
        op_m = input("Seleccione una opcion: ")
        if(op_m == 1):
            if(check_execs('haml')):
                print "Haml no esta instalado, Adios"
                final = 1
            else:
                subprocess.call('clear')
                print "Bienvenido a Haml el preprocesador de HTML, el cual le permitira tener mayor produccion al momento de crear sus plantillas web"
                print "Que desea compilar ?"
                print " 1) Todos los archivos"
                print " 2) Archivo en especifico"
                op_h = input("Seleccione una opcion: ")
                if(op_h == 1):
                    print("Iniciando el proceso de compilacion por favor espere...")
                    lista = glob.glob("*.haml")
                    if(lista):
                        for archivo in lista:
                            nuevo_archivo = os.path.splitext(archivo)
                            archivo_final = nuevo_archivo[0] + ".html"
                            subprocess.call(['haml', archivo, archivo_final])
                            #os.system('haml '+archivo+" "+archivo_final)
                            print(archivo + " convertido en " + archivo_final)
                        print("Todos los archivos compilados correctamente!!!")
                        time.sleep(5)
                    else:
                        print("No existe ningun archivo .haml en la carpeta")
                        time.sleep(5)
                    
                elif(op_h == 2):
                    nombre_a = raw_input("Ingrese el nombre del archivo con extension .haml: ")
                    if(os.path.isfile(nombre_a)):
                        nombre_b = nombre_a.partition(".haml")
                        nombre_c = nombre_b[0] + ".html"
                        subprocess.call(['haml', nombre_a, nombre_c])
                        #os.system('haml ' + nombre_a + " " + nombre_c)
                        print nombre_a +" se ha compilado correctamente"
                        time.sleep(5)
                    else:
                        print(nombre_a + " no existe en la carpeta")
                        time.sleep(5)
                else:
                    print 'La opcion elegida no esta disponible'
                    time.sleep(5)
        elif(op_m == 2):
            if(check_execs('sass')):
                print "Sass no esta instalado, Adios"
                final = 1
            else:
                subprocess.call("clear")
                print "Bienvenido a Sass el preprocesador de CSS, el cual te permitira utilizar CSS como nunca te habias imaginado"
                print "Que deseas compilar?"
                print " 1) Todos los archivos"
                print " 2) Archivo en especifico"
                op_s = input("Selecciona una opcion: ")
                if(op_s == 1):
                    print("Iniciando proceso de compilacion por favor espere...")
                    lista2 = glob.glob("*.scss")
                    if(lista2):
                        for archivo in lista2:
                            nuevo_archivo = os.path.splitext(archivo)
                            archivo_final = nuevo_archivo[0] + ".css"
                            subprocess.call(['sass','--sourcemap=none', archivo, archivo_final])
                            #os.system('sass --sourcemap=none '+archivo+" "+archivo_final)
                            print(archivo + " convertido en "+ archivo_final)
                        print "Todos los archivos compilados correctamente!!!"
                        time.sleep(5)
                    else:
                        print "No existe ningun archivo .scss en la carpeta"
                        time.sleep(5)
                        
                elif(op_s == 2):
                    nombre_a = raw_input("Ingrese el nombre del archivo con extension .scss: ")
                    if(os.path.isfile(nombre_a)):
                        nombre_b = nombre_a.partition(".scss")
                        nombre_c = nombre_b[0] + ".css"
                        subprocess.call(['sass', '--sourcemap=none', nombre_a, nombre_c])
                        #os.system('sass --sourcemap=none '+nombre_a+" "+ nombre_c)
                        print(nombre_a + " compilado correctamente")
                        time.sleep(5)
                    else:
                        print(nombre_a + " no existe en la carpeta")
                        time.sleep(5)
                else:
                    print("La opcion seleccionada no esta disponible")
        elif(op_m == 3):
            print "Bienvenido a la seccion de servidor local, deseas activarlo ?"
            print " 1) Si"
            print " 2) No"
            op_l = input("Seleccione una opcion: ")
            if(op_l == 1):
                subprocess.call('clear')
                ip = "127.0.0.1"
                port = 8000
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if(sock.connect_ex((ip, port))):
                    print "Servidor local iniciado en http://localhost:8000"
                    subprocess.call(['python', '-m', 'SimpleHTTPServer'])
                else:
                    print "El puerto esta siendo utilizado por otra aplicacion o el servidor ya esta encendido"
                    time.sleep(5)
                
        elif(op_m == 4):
            print "Adios, Gracias por utilizar PyPros :D :D :D :D"
            final = 1

    pass

if __name__ == "__main__":
    ruby = check_execs('ruby')
    haml = check_execs('haml')
    sass = check_execs('sass')
    blender = check_execs('blender')
    if(ruby == 1):
        print "Ruby no se ha encontrado instalado en el sistema, por favor instalarlo"
        final = 1
    if(haml == 1):
        print "Haml no se encuentra instalado en tu sistema, puedes instalarlo con: gem install haml"
    if(sass == 1):
        print "Sass no se encuentra instaldo en tu sistema, puedes instalarlo con: gem install sass"
    main()

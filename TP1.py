import numpy as np
import matplotlib.pyplot as plt
#%%
dir_salida1="C:/Users\Alicia\Desktop\circulacion\k1/" #de esta manera buscamos por donde salen los datos y si o si va la barra al final para que me identificar que debe entrar en la ultima carpeta
dir_salida2="C:/Users\Alicia\Desktop\circulacion\k2/"
dir_salida3="C:/Users\Alicia\Desktop\circulacion\k3/"
Lx=4e6
Ly=2e6
nx=200 #grillas en x
ny=100 #grillas en y
from Cargar import cargar #llamamos a la funcion Cargar para cargar los datos
psi_temp1,vort_temp1,psiF1,vortF1,QG_diag1,QG_curlw1,X,Y,dx,dy=cargar(dir_salida1,Lx,Ly,nx,ny)
from Cargar import cargar
psi_temp2,vort_temp2,psiF2,vortF2,QG_diag2,QG_curlw2,X,Y,dx,dy=cargar(dir_salida2,Lx,Ly,nx,ny)
from Cargar import cargar
psi_temp3,vort_temp3,psiF3,vortF3,QG_diag3,QG_curlw3,X,Y,dx,dy=cargar(dir_salida3,Lx,Ly,nx,ny)
#%% Transformo X e Y de m a Km para poder graficar mas prolijo
X1=X/1000
Y1=Y/1000

#%%dimensionalizamos primero para luego graficar
"""
dimensionalizamos primero para luego graficar
"""
#funcion corriente

beta=1.9e-11  #definimo beta
tau=0.3  #tension del viento
ro=1025  #densidad 
D=2000  #profunidad
U=(2*np.pi*tau)/(ro*D*beta*Lx)  #velocidad 
U1=U*Lx  #velocidad por distancia de la cuenca, se necesita para dimensionalizar ala funcion corriente

psi1=psiF1*U1  #con esto obtenemos la funcion corriente dimensionalizada para k1
psi2=psiF2*U1  #con esto obtenemos la funcion corriente dimensionalizada para k2
psi3=psiF3*U1  #con esto obtenemos la funcion corriente dimensionalizada para k3
#vorticidad 

U2=U/Lx  #dato necessario para dimensionalizar a la vorticidad
vort1=vortF1*U2    #se toma los valores de la matriz de vorticidad y lo dimensionalizamos para k1
vort2=vortF2*U2    #se toma los valores de la matriz de vorticidad y lo dimensionalizamos para k1
vort3=vortF3*U2    #se toma los valores de la matriz de vorticidad y lo dimensionalizamos para k1

#%%
""" 
#funcion corriente
"""
levels_psi=np.arange(-350000,10000,10000)
#Funcion corriente para k1
plt.figure(1,figsize=(10,10))
contor1=plt.contour(X1,Y1,psi1, levels_psi) #ploteamos ya dimensionlizado
plt.clabel(contor1,inline=True,fontsize=7)
plt.title('funcion corriente(m^2/s)')
plt.xlabel('Latitd km')
plt.ylabel('Longitud km')
plt.colorbar()
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 1bk12.png")
#funcion corriente para k2
plt.figure(2,figsize=(10,10))
contor2=plt.contour(X1,Y1,psi2,levels_psi) #ploteamos ya dimensionlizado
plt.clabel(contor2,inline=True,fontsize=7, )
plt.title('funcion corriente(m^2/s)')
plt.xlabel('Latitd km')
plt.ylabel('Longitud km')
plt.colorbar()
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 1bk22.png")
plt.figure(3,figsize=(10,10))
contor3=plt.contour(X1,Y1,psi3, levels_psi) #ploteamos ya dimensionlizado
plt.clabel(contor3,inline=True,fontsize=7)
plt.title('funcion corriente(m^2/s)')
plt.xlabel('Latitd km')
plt.ylabel('Longitud km')
plt.colorbar()
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 1bk32.png")
"""
energia
"""
ener1=np.array(QG_diag1[:,3]) #defino un vector para graficar la 3era columna que es la energia de k1
tiempo1=np.array(QG_diag1[:,0]) #idem pero para el tiempo
ener2=np.array(QG_diag2[:,3]) #defino un vector para graficar la 3era columna que es la energia de k2
tiempo2=np.array(QG_diag2[:,0]) #idem pero para el tiempo
ener3=np.array(QG_diag3[:,3]) #defino un vector para graficar la 3era columna que es la energia de k3
tiempo3=np.array(QG_diag3[:,0]) #idem pero para el tiempo
plt.figure(4,figsize=(10,10))
plt.plot(tiempo1,ener1,'m',label="energia para k1") 
plt.plot(tiempo2,ener2,'r',label="energia para k2") 
plt.plot(tiempo3,ener3,'g',label="energia para k3") 
plt.xlabel('tiempo')
plt.ylabel('Energia cinetica')
plt.legend(loc="lower right")
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 1a.png")


#%% Calculo del transporte
"""
transporte meridional en sv
"""
levels_T=np.arange(-210,60,30)
#trasnporte para k1
vel1=np.diff(psi1,n=1,axis=1)
My1=vel1*D     
Mysv1=My1/1e6  #con esto lo transformamos en SV
plt.figure(5,figsize=(10,10))
plt.contourf(X1[0:199],Y1[0:100],Mysv1, levels_T)
#plt.clabel(cont,inline=True,fontsize=7)  # esto solo lo puedo usar con contour, ya q nose aun como hacerlo para contourf
plt.colorbar()
plt.title('Transporte Meridional en SV ')
plt.xlabel('Longitud en km')
plt.ylabel('Latitud en km')
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 1b1k1.png")

#trasnporte para k2
vel2=np.diff(psi2,n=1,axis=1)
My2=vel2*D     
Mysv2=My2/1e6  #con esto lo transformamos en SV
plt.figure(6,figsize=(10,10))
plt.contourf(X1[0:199],Y1[0:100],Mysv2,levels_T)
#plt.clabel(cont,inline=True,fontsize=7)  # esto solo lo puedo usar con contour, ya q nose aun como hacerlo para contourf
plt.colorbar()
plt.title('Transporte Meridional en SV ')
plt.xlabel('Longitud en km')
plt.ylabel('Latitud en km')
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 1b1k2.png")
#trasnporte para k3
vel3=np.diff(psi3,n=1,axis=1)
My3=vel3*D     
Mysv3=My3/1e6  #con esto lo transformamos en SV
plt.figure(7,figsize=(10,10))
plt.contourf(X1[0:199],Y1[0:100],Mysv3, levels_T)
#plt.clabel(cont,inline=True,fontsize=7)  # esto solo lo puedo usar con contour, ya q nose aun como hacerlo para contourf
plt.colorbar()
plt.title('Transporte Meridional en SV ')
plt.xlabel('Longitud en km')
plt.ylabel('Latitud en km')
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 1b1k3.png")


"""
corte zonal de transporte y la vorticidad
se plotean en mismo grafico
"""
#trasnporte zonal
Mz1=Mysv1[50,:]  #k1
Mz2=Mysv2[50,:]  #k2
Mz3=Mysv3[50,:]  #k3
plt.figure(8,figsize=(10,10))
plt.plot(X1[0:199],Mz1,'m',label="k1")
plt.plot(X1[0:199],Mz2,'r',label="k2")
plt.plot(X1[0:199],Mz3,'g',label="k3")
plt.title('Corte zonal del Transporte Meridional')
plt.xlabel('Longitd en km')
plt.ylabel('transporte meridional Sv')
plt.legend(loc="lower right")
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio1c.png")

#vorticidad
vorti1=vort1[50,:]
vorti2=vort2[50,:]
vorti3=vort3[50,:]
plt.figure(9,figsize=(10,10))
plt.plot(X1,vorti1,'m',label="k1")
plt.plot(X1,vorti2,'r',label="k2")
plt.plot(X1,vorti3,'g',label="k3")
plt.title('Corte zonal de la vorticidad')
plt.xlabel('Longitd en km')
plt.ylabel('Vorticidad(s^-1)')
plt.legend(loc="upper right")
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio1c1.png")

"""
corriente de contorno oeste
"""
#para k1
co1=np.array(Mysv1[50,0:14])
CBO1=np.sum(co1)  #estimacion de la corriente oeste

tot1=np.sum(np.array(Mysv1[50,:]))
#para k2
co2=np.array(Mysv2[50,0:14])
CBO2=np.sum(co2)  #estimacion de la corriente oeste

tot2=np.sum(np.array(Mysv2[50,:]))
#para k3
co3=np.array(Mysv3[50,0:14])
CBO3=np.sum(co3)  #estimacion de la corriente oeste

tot3=np.sum(np.array(Mysv3[50,:]))

#%% graficar el ejerccio 3
#para cada caso debo seleccionar el coeficiente que corresponde
eps1=0.16 # coeficiente de friccion de fondo adimensionalizado 
eps2=0.45
eps3=0.75
#Ec. de stommel para k1
vientozonal1=QG_curlw1[50,:]
vela1=np.diff(psiF1,n=1,axis=1)
plt.figure(10,figsize=(10,10))
plt.plot(X1[0:199],vela1[50,:],'m',label="funcion corriente") # para la leyenda debo definir label
plt.plot(X1,eps1*vortF1[50,:],'g',label="vorticidad")
plt.plot(X1,vientozonal1[0:200],'c',label="rotor del viento")
plt.legend(loc="upper right")  # loc es para localizar la ubicacion de la leyenda 
plt.grid(True)
plt.title('terminos individuales de la Ec. de Stommel')
plt.xlabel('Longitud en km')
plt.ylabel('Terminos adimensionales')
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 3k1.png")

#Ec. de stommel para k2
vientozonal2=QG_curlw2[50,:]
vela2=np.diff(psiF2,n=1,axis=1)
plt.figure(10,figsize=(10,10))
plt.plot(X1[0:199],vela2[50,:],'m',label="funcion corriente") # para la leyenda debo definir label
plt.plot(X1,eps2*vortF2[50,:],'g',label="vorticidad")
plt.plot(X1,vientozonal2[0:200],'c',label="rotor del viento")
plt.legend(loc="upper right")  # loc es para localizar la ubicacion de la leyenda 
plt.grid(True)
plt.title('terminos individuales de la Ec. de Stommel')
plt.xlabel('Longitud en km')
plt.ylabel('Terminos adimensionales')
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 3k2.png")
#Ec. de stommel para k3
vientozonal3=QG_curlw3[50,:]
vela3=np.diff(psiF3,n=1,axis=1)
plt.figure(11,figsize=(10,10))
plt.plot(X1[0:199],vela3[50,:],'m',label="funcion corriente") # para la leyenda debo definir label
plt.plot(X1,eps3*vortF3[50,:],'g',label="vorticidad")
plt.plot(X1,vientozonal3[0:200],'c',label="rotor del viento")
plt.legend(loc="upper right")  # loc es para localizar la ubicacion de la leyenda 
plt.grid(True)
plt.title('terminos individuales de la Ec. de Stommel')
plt.xlabel('Longitud en km')
plt.ylabel('Terminos adimensionales')
plt.savefig("C:/Users\Alicia\Desktop\circulacion\ejercicio 3ck3.png")

#para el caso tres se puede distingir muy bien los parametros, en el contorno oeste la vorticidad es 
#alta y las velocidades son alta. Luego, para el viento se observa que se cumple stommel ya que es cte
#para una Simulacion se toma un valor estimado de los terminos de Stommel



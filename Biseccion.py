import math

expr = input('Ingrese funcion: ')#pide la expresion algebraica en terminos de x y la guarda en variable expr
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))




tol=1.e-2

nmi=100
it=1
fpm=100

while (b-a) > tol and abs(fpm)>tol and it < nmi:

	print("'///////////////////////////////////////////////'",it)
	
	it += 1
	pm=(a+b)/2

	print ("a",a)#'a:',a
	print ("b",b)#'b:',b
	print ("pm",pm)#'pm',pm

	libres=dict(x=a)
	funcs = vars(math)	
	fa=eval(expr, funcs,libres)
	
	libres=dict(x=b)
	funcs = vars(math)
	fb=eval(expr, funcs,libres)
	
	libres=dict(x=pm)
	funcs = vars(math)
	fpm=eval(expr, funcs,libres)
	
	print ("f(a)",fa)#'f(a)',fa
	print ("f(b)",fb)#'f(b)',fb
	print ("f(pm)",fpm)#'f(pm)',fpm
	
	comp=(fa*fpm)
	#print comp

	if comp > 0:
		a = pm
	if comp < 0:
		b = pm

print ("La raiz aproximada: ", pm)#'La raiz aproximada: ',pm
#15000-(x/(1+(x/10-1))*e**(-2*10**(-6)*x*60))
from django.shortcuts import render, redirect
from .models import empresaDatos, comedorDatos, facturaDatos
from habitacion.models import habitacion
from .forms import empresaForm, comedorForm, facturaForm
from django.contrib import messages
# Create your views here.

def home_view( request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    return render(request, "home.html",{})

def addEmpresa(request):
    queryset = empresaDatos.objects.all()

    form = empresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = empresaForm()
        messages.success(request, "Información guardada exitosamente")
        #return redirect("addHab")

    context = {
        'listEmp' : queryset,
        'form' : form
    }
    return render(request,"addEmpresa.html", context)

def addComedor(request):
    queryset = comedorDatos.objects.all()

    form = comedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = comedorForm()
        messages.success(request, "Información guardada exitosamente")
        #return redirect("addHab")

    context = {
        'listComedor' : queryset,
        'form' : form
    }
    return render(request,"addComedor.html", context)

def cargarDatos(request):
    # obteniendo datos 
    queryset = facturaDatos.objects.all()
    rutBuscado = request.GET.get("buscar")
    context = {
            'facDatos' : queryset
        }
    # Buscando empresa 
    if rutBuscado:
        empDatos = empresaDatos.objects.get(rutEmpresa=rutBuscado)
        messages.success(request, "Información cargada exitosamente")
        print(empDatos.nombreEmpresa)
        # if empDatos:

        form = facturaForm(request.POST or None)
        if form.is_valid():
            # se indica que se mantendrán los dos datos seleccionados, pero aún no se guardaran hasta asignar los demás (?)
            obj = facturaForm.save()

            obj.rut_Emp_Fac = empDatos.rutEmpresa
            obj.nombre_Emp_Fac = empDatos.nombreEmpresa
            obj.giro_Emp_Fac = empDatos.giroEmpresa
            obj.dir_Emp_Fac = empDatos.dirEmpresa
            #hab = request.GET['tipo_Hab_Fac']
            hab = habitacion.objects.get(tipoHabitacion=hab)

            serv = comedorDatos.objects.get(tipoPlato=serv)

            obj.valor_Serv_Fac = serv.valorMenu
            obj.valor_Hab_Fac = hab.precio
            obj.total_Fac = serv.valorMenu + hab.precio
            # cuando todos los valores están definidos, se indica que ahora sí puede guardar los datos.
            obj.save(commit=True)
            messages.success(request, "Información guardada exitosamente")


                #id_serv=request.POST['tipo_Serv_Fac']
                #id_hab=request.POST['tipo_Hab_Fac']
            #fac = facturaDatos()
            #fac.rut_Emp_Fac = empDatos.rutEmpresa
            #fac.nombre_Emp_Fac = empDatos.nombreEmpresa
            #fac.giro_Emp_Fac = empDatos.giroEmpresa
            #fac.dir_Emp_Fac = empDatos.dirEmpresa
            #fac.tipo_Serv_Fac = request.POST['tipo_Serv_Fac']
                
            #hab = habitacion.objects.get(id=request.POST['tipo_Hab_Fac'])
            #serv = comedorDatos.objects.get(id=request.POST['tipo_Serv_Fac'])

            #fac.valor_Serv_Fac = serv.valorMenu
            #fac.tipo_Hab_Fac = request.POST['tipo_Hab_Fac']
            #fac.valor_Hab_Fac = hab.precio
            #fac.total_Fac = serv.valorMenu + hab.precio
            #print(fac)
            # fac.save()
            messages.success(request, "Información guardada exitosamente")
        else:
            print("no guarda :c")
            messages.error(request,"CARGA DATOS, PERO NO LOS QUIERE GUARDAR >:C")
        context = {
            'empDatos' : empDatos,
            'form' : form,
            'facDatos' : queryset
        }
    return render(request,"cargarDatos.html", context)
    
        # if form.is_valid():
    #    prod = productosLocal()
     #   prod.nombreProducto = request.POST['nombreProducto']
      #  prod.cantidad = request.POST['cantidad']
       # empresa = empresaDatos.objects.get(rutEmpresa=request.POST['rutEmpresa'])
    #    prod.rutEmpresa = empresa
     #   prod.direccion_local = local.direccion_local
      #  prod.save()
       # form = ProductosLocalForm()
from django.shortcuts import render,redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def getHome(request):
    product = Product.objects.all()
    sumNhap = 0
    sumBan = 0
    for x in product:
        sumNhap += x.gianhap * x.slkbd
        sumBan += x.giaban * x.slb 
    doanhThu = int(sumBan - sumNhap) 
    doanhThu = '{:,}'.format(int(doanhThu)).replace(',', '.')
    sumNhap = '{:,}'.format(int(sumNhap)).replace(',', '.')
    sumBan = '{:,}'.format(int(sumBan)).replace(',', '.')

    return render(request, 'pages/home.html', {'sumNhap': sumNhap, 'sumBan': sumBan, 'doanhThu': doanhThu})

def getManage(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        delete = request.POST.get('delete')
        update = request.POST.get('update')
        slb = request.POST.get('updateSLB')
        sort = request.POST.get('sort')
        if(sort == 'slkct'):
            product = Product.objects.all().order_by('-slk')
            return render(request, 'pages/manage.html', {'product': product})
        if(sort == 'slktc'):
            product = Product.objects.all().order_by('slk')
            return render(request, 'pages/manage.html', {'product': product})
        if(sort == 'gnct'):
            product = Product.objects.all().order_by('-gianhap')
            return render(request, 'pages/manage.html', {'product': product})
        if(sort == 'gntc'):
            product = Product.objects.all().order_by('gianhap')
            return render(request, 'pages/manage.html', {'product': product})
        if(search!= None):
            product = Product.objects.all()
            list = []
            for x in product:
               if search in x.shortDescription:
                   list.append(x)
            return render(request, 'pages/manage.html', {'product': list})
        if(slb!=None):
            productById = Product.objects.get(id=slb)
            if(productById.slk!=0):
               productById.slb = productById.slb +1
               productById.slk = productById.slk -1
               productById.save()
               return redirect('/manage')
            return redirect('/manage')
        if(delete!=None):
            product = get_object_or_404(Product, pk=delete)
            product.delete()
            return redirect('/manage')
        productById = Product.objects.get(id=update)
        return render(request, 'pages/add.html', {'product': productById})
    product = Product.objects.all()
    return render(request, 'pages/manage.html', {'product': product})

def getAdd(request):
    if request.method == 'POST':
        update = request.POST.get('update')
        if(update!=None):
            product = get_object_or_404(Product, pk=update)
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('/manage')
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/manage')
    else:
        form = ProductForm()
    return render(request, 'pages/add.html', {'form': form})

def getOrder(request):
    if request.method == 'POST':
        sort = request.POST.get('sort')
        if(sort == 'slbct'):
            product = Product.objects.all().order_by('-slb')
            list = []
            tong = 0
            for x in product:
                if(x.slb !=0):
                    j=x.slb * x.giaban
                    x.sum = j
                    tong +=j
                    list.append(x)
            return render(request, 'pages/order.html', {'product': list, 'tong':tong})
        if(sort == 'slbtc'):
            product = Product.objects.all().order_by('slb')
            list = []
            tong = 0
            for x in product:
                if(x.slb !=0):
                    j=x.slb * x.giaban
                    x.sum = j
                    tong +=j
                    list.append(x)
            return render(request, 'pages/order.html', {'product': list, 'tong':tong})
        if(sort == 'gbct'):
            product = Product.objects.all().order_by('-giaban')
            list = []
            tong = 0
            for x in product:
                if(x.slb !=0):
                    j=x.slb * x.giaban
                    x.sum = j
                    tong +=j
                    list.append(x)
            return render(request, 'pages/order.html', {'product': list, 'tong':tong})
        if(sort == 'gbtc'):
            product = Product.objects.all().order_by('giaban')
            list = []
            tong = 0
            for x in product:
                if(x.slb !=0):
                    j=x.slb * x.giaban
                    x.sum = j
                    tong +=j
                    list.append(x)
            return render(request, 'pages/order.html', {'product': list, 'tong':tong})
        search = request.POST.get('search')
        if(search!= None):
            product = Product.objects.all()
            list = []
            tong = 0
            for x in product:
               if search in x.shortDescription:
                    if(x.slb !=0):
                        j=x.slb * x.giaban
                        x.sum = j
                        tong +=j
                        list.append(x)
            return render(request, 'pages/order.html', {'product': list, 'tong':tong})
    product = Product.objects.all()
    list = []
    tong = 0
    for x in product:
        if(x.slb !=0):
            j=x.slb * x.giaban
            x.sum = j
            tong +=j
            list.append(x)
    return render(request, 'pages/order.html', {'product': list, 'tong':tong})
from projects.imports import *

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def loginseller(request):
    if 'sessionid' in request.COOKIES:
        seller_id = request.session.get('seller_id', None)
        if seller_id is not None:
            return redirect('homeseller', seller_id=seller_id) 
    if request.method == 'POST':
        form = LoginSellerForm(request.POST)
        if form.is_valid():
            selleremail = form.cleaned_data['selleremail']
            sellerpassword = form.cleaned_data['sellerpassword']

            try:
                seller = Seller.objects.get(selleremail=selleremail)
                if check_password(sellerpassword, seller.sellerpassword):
                    session = Session(session_key=str(seller.id))
                    session.expire_date = timezone.now() + timedelta(days=7)  
                    session.save()
                    request.session['seller_id'] = seller.id
                    request.session['storename'] = seller.storename

                    return redirect('homeseller', seller_id=seller.id)
                else:
                    messages.error(request, 'Wrong password. Kindly try again.')
            except Seller.DoesNotExist:
                messages.error(request, 'Email does not exist.')

    else:
        form = LoginSellerForm()

    return render(request, 'seller/loginseller.html', {'form': form})
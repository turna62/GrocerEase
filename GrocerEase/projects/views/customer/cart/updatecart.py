from projects.imports import *

@csrf_exempt
def updatecart(request):
    if 'customer_id' in request.session:
        customer_id = request.session['customer_id']
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print('Action:', action)
        print('Product:', productId)

        try:
            customer = Customer.objects.get(id=customer_id)
        except Customer.DoesNotExist:
            return JsonResponse({'message': 'Customer not found'}, status=404)

        product = Item.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer=customer, is_cart=True)

        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

        if action == 'add':
            seller = product.seller
            current_quantity = product.itemquantity  # Get the current quantity in seller stock

            if current_quantity > 0:
                if orderItem.quantity <= current_quantity:
                    if current_quantity == 1:
                        # Handle the case where the stock becomes 0
                        product.itemquantity = 0
                        restock_message = " It needs to be restocked."
                    else:
                        # Decrease the quantity by 1
                        product.itemquantity = current_quantity - 1
                        restock_message = ""

                    product.save()
                    orderItem.quantity = (orderItem.quantity + 1)

                    added_datetime = timezone.now()  # Get the current date and time
                    current_datetime = added_datetime + timedelta(hours=6)
                    message = f"Your item '{product.itemtitle}' was added to a customer: {customer.customername}'s cart at {current_datetime}. Current Quantity: {product.itemquantity}. {restock_message}"
                    Notification.objects.create(sender=customer, recipient=seller, item=product, message=message)
            #     else:
            #         # Handle the case where the cart quantity equals or exceeds the available stock
            #         # You can raise an exception or handle it as needed
            # else:
            #     # Handle the case where the item is out of stock

        elif action == 'remove':
            seller = product.seller
            if orderItem.quantity > 0:  # Check if there's something to remove
                orderItem.quantity = (orderItem.quantity - 1)
                current_quantity = product.itemquantity  # Get the current quantity in seller stock

                product.itemquantity = current_quantity + 1

            else: 
               current_quantity = product.itemquantity  # Get the current quantity in seller stock

               product.itemquantity = current_quantity + 1

            product.save()
            added_datetime = timezone.now()
            current_datetime = added_datetime + timedelta(hours=6)
            message = f"Your item '{product.itemtitle}' was removed from a customer: {customer.customername}'s cart at {current_datetime}. Current Quantity: {product.itemquantity}"
            Notification.objects.create(sender=customer, recipient=seller, item=product, message=message)

        orderItem.save()

        if orderItem.quantity <= 0:
                orderItem.delete()
        # else:
        #     # Handle the case where there's nothing to remove
        

    return JsonResponse({'message': 'Item was added'}, safe=False)

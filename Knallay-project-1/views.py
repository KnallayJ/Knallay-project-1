def contract(request, contract_id):

    
    contract=models.Contract.objects.get(id=contract_id)
    carriers=models.Carrier.objects.all()
    customers=models.Customer.objects.all()
    routes=models.Route.objects.all()
    
    
    

    
    context={
        'contract':contract,
        'allcontracts':models.Contract.objects.all(),
        'allcarriers': carriers,
        'allcustomers':customers,
        'comments':contract.comments.all()        
    }
    return render(request, 'contract.html',context)

def edit_contract(request, contract_id):

    def format_datetime_input(astring):
        output = astring.split("/")
        output.append(output[0])
        output.append(output[1])
        output = output[2::]
        return "-".join(output)
    
    
    display_post(request)             
        
    
    contract=models.Contract.objects.get(id=contract_id)
    
    carrier=models.Carrier.objects.get(id=int(request.POST['carrier']))
    
    customer=models.Customer.objects.get(id=int(request.POST['customer']))
    
    
    print(request.POST['trip_number'])
    print(contract.trip_number)
    contract.trip_number=request.POST['trip_number']
    print(contract.trip_number)
    contract.status=request.POST['status']  
    contract.carrier=carrier
    contract.customer=customer
    contract.carrier_cost=request.POST['carrier_cost']
    contract.customer_price=request.POST['customer_price']
    contract.pick_up_time = format_datetime_input(request.POST["pickup_date"]) + " " + str(request.POST["pickup_time"])
    contract.delivery_time = format_datetime_input(request.POST["delivery_date"]) + " " + str(request.POST["delivery_time"])
    
    
    contract.route.start.street=request.POST['pickup_street_address']
    
    contract.route.start.city=request.POST['pickup_city']
    contract.route.start.state=request.POST['pickup_state']
    contract.route.end.street=request.POST['delivery_street_address']
    contract.route.end.city=request.POST['delivery_city']
    contract.route.end.state=request.POST['delivery_state']
    print(contract.trip_number)
        
    contract.save()
    carrier.save()
    customer.save()
    contract.route.start.save()
    contract.route.end.save()
    print(contract.trip_number)
    
    return redirect('contract_detail',contract_id=contract_id)

def archive_contract(request, contract_id):

    if request.POST['hiddenkey'] == 'archive':
        contract=Contract.objects.get(id=contract_id)
        if contract.archived == True:
                contract.archived = False
        else:
            contract.archived = True
        print(contract.archived)
        contract.save()
        print(contract.archived)
        return redirect("/dashboard")

def contract_comment(request, contract_id):

    

    Comment.objects.create(
        content=request.POST['comments'],
        user=logged_user(request), 
        contract= Contract.objects.get(id=contract_id)
    )


    return redirect('contract_detail',contract_id=contract_id)


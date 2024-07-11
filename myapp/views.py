# myapp/views.py
from django.shortcuts import render
from .FAKE_ACC.instagram import process_username
from .FAKE_ACC.app import mainpreprocess

def input_username(request):
    if request.method == 'POST':
        # Get the username from the form submission
        username = request.POST['username']
        
        # Process the username using the process_username function
        process_username(username)
        processed_result = mainpreprocess()
        # Render the "result" HTML template with the processed result
        if(processed_result==0):
            res ="Genuine User"
        else:
            res= "Automated account"
        
        return render(request, 'result.html', {'result': res})
    
    return render(request, 'username_form.html')

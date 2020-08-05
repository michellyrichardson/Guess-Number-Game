from django.shortcuts import render, redirect
import random

# Create your views here.
def numbergame(request):
    number = random.randint(1,100)
    request.session['number'] = number
    if 'number' in request.session:
        request.session['number'] = number

    print(request.session['number'])
    
    return render(request, 'numbergame.html')

def decision(request):
    if request.POST['guess'] == '':
        request.session['result'] = (f'Please insert a number')
        return redirect('/')
    
    guess = request.POST['guess']
    guess = int(guess)
    if guess < request.session['number']:
        print(f'{guess} too low!')
        request.session['result'] = 'Too Low!' 

    elif guess > request.session['number']:
        print(f'{guess} too high!')
        request.session['result'] = 'Too High!'

    if guess == request.session['number']:
        print(f'correct!')
        request.session['result'] = (f'{guess} was the number!')
    
    return redirect('/')

def reset(request):
    print('reset is working!')
    request.session.flush()
    return redirect('/')
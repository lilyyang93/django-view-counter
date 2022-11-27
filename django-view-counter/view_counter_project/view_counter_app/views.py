from django.shortcuts import render
import random 

users = {} #dict to store our cookies(key:value)

def index(request):
    #a user shows up to the page 
    user_id = request.COOKIES.get('user_id') #check the user's cookie 
    user = users.get(user_id) #check the cookie against our records in our cookies dictionary
    if not user: #if we don't have a record of their cookie, they are a first time visitor. Add their cookie, start a session for them, and start tracking their visits
        user_id = str(random.randint(100000,999999))
        users[user_id]= { 
            'count':1,
        }
    else: #if we already have a record of their cookie, update their visit log 
        users[user_id]['count'] += 1
    
    response = render(request, 'pages/index.html', users[user_id])
    response.set_cookie('user_id', user_id) #but in either case, we are setting the cookie so we can remember them when they come back

    return response 


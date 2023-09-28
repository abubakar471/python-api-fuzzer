# error
    the first error that occured while intilizing this app was , while i was importing the requests
    module and to resolve this i just type : pip install requests

# how to test the app
    comment out the "loop()" function and uncomment line 20-24 

# how this app functions
    so what we do first is make a api call to a api with every word exists in the small.txt file in the root directory as an endpoint, than we get the respone. Now we filter out the reponse that have 404 reponse that means that word in small.txt is not existed in our api as an endpoint.
    so we only show the valid endpoints 

# how to run the app
    u can change the api url in requests.get 
    
    in cli type: 
        cat small.txt | python main.py

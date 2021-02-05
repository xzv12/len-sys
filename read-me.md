
any user can create requests and make offers on other users requests with the same account

admin/
api/user/ register/ 
api/user/ login/ 
api/user/ edit-profile/

 
api/ create-request       ---> create loan request , only logged user can make requests  

api/ list-my-requests     ---> list all my requests

api/ list-requests        ---> list other users requests
 
api/ request/<int:pk>     ---> two methods available here
			       get()   --> list all offers created by all users for this request
			       post()  --> create an offer for this request, any user can use this method except request creator


api/ offer/<int:pk>       ---> the only user who can accept any offer is the creator of the request related to this offer
				
				if he accept offer
				if offer creator have enough money
				the request amount will be taken from offer creator balance + lenme fee
				and added to request's creator balance
				the (funde-flag) of the request will be turn to true
				the (accepted-flag) of the offer will be turn to true
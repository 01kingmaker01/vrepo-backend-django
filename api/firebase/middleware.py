
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate(r'D:\project\___VIT___\vit\api\firebase\key.json')
firebase_admin.initialize_app(cred)
    
def simple_middleware(get_response):
  

    def middleware(request):
        # try:
        #     token = request.headers['Authorization']

        #     decoded_token = auth.verify_id_token(token)
        #     print(decoded_token)
        #     # uid = decoded_token['uid']
        # except :
        #     print("No Auth")


        response = get_response(request)
        return response

    return middleware
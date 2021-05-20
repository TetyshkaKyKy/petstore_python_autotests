

base_url = 'https://petstore.swagger.io/v2'

'''
class ApiService:
    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'

    def get(self, url,params=params):
        return requests.get(f'{self.base_url}{url}', )
    def post(self,url,body):
        return requests.post(f'{self.base_url}{url}', data = body,
                             headers={'accept': 'application/json', 'Content-Type': 'application/json'})

class PetApiService(ApiService):
    def __init__(self):
        pass

    def find_pets_by_status(self):
        return requests.get(self.base_url + '/findByStatus')
        
    def create_pets(self):
        '''




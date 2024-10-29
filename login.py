import bcrypt,json

class Login:
    def __init__(self, username, password):
        self.username= username
        self.password= password

    def __hash_pass(self):
        salt=bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        return self.hashed_password
    
    def __hash_verify(self, hashed_password)->bool:
        return bcrypt.checkpw(self.password.encode('utf-8'), hashed_password)
    
    def __get_users(self)->list:
        with open ("login.json", "r") as file:
            data = json.load(file)
        return data

    def create_user(self):
        data=self.__get_users()
        for index in data:
            if self.username in index:
                return 0
        dict={self.username:(self.__hash_pass()).decode('utf-8')}
        data.append(dict)
        with open ("login.json", "w") as file:
            json.dump(data ,file) 
            return 1
    
    def login_user(self):
        data=self.__get_users()
        for index, login in enumerate(data):
            try:
                if self.__hash_verify(((login.get(self.username)).encode('utf-8'))):
                    return 1
            except:pass
        return 0


            


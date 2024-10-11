import bcrypt,json

class Login:
    def __init__(self, username, password):
        self.username= username
        self.password= password

    def __hash_pass(self):
        salt=bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        print(self.hashed_password)
        print(type(self.hashed_password))
        return self.hashed_password
    
    def __hash_verify(self, hashed_password)->bool:
        print("entrou nessa porra")
        return bcrypt.checkpw(self.password.encode('utf-8'), hashed_password)
    
    def __get_users(self)->list:
        with open ("login.json", "r") as file:
            data = json.load(file)
        return data

    def create_user(self):
        data=self.__get_users()
        for index in data:
            if self.username in index:
                print("entrou no if")
                return
        dict={self.username:str(self.__hash_pass())}
        data.append(dict)
        with open ("login.json", "w") as file:
            json.dump(data ,file) 
    
    def login_user(self):
        data=self.__get_users()
        for index, login in enumerate(data):
            try:
                print(((login.get(self.username)).encode('utf-8')))
                if self.__hash_verify(((login.get(self.username)).encode('utf-8'))):
                    print("deu certo cabeça de pika")
            except:
                print("nao deu")


            

p1=Login("gienes", "123456")
p1.login_user()

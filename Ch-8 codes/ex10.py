class NotValidAge(Exception):
    def __str__(self):
        return 'Age Should be greater than 18 years !!'

def driving_licence(age):
    try:
        if age<18:
            raise NotValidAge
    except Exception as e:
        print(e)
    
driving_licence(12)
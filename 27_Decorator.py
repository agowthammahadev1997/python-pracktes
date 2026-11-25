#Pythonలో ఒక Functionకు దాని అసలు Codeను మార్చకుండా అదనపు Functionality జోడించడాన్ని Decorator అంటారు
#wrappers అనేవి ఒక Functionను తీసుకుని దాని Codeను మార్చకుండా అదనపు Functionalityని జోడించే Functions.

# def my_decorator(func):
#     def wrapper():
#         print("Before Function")
#         func()
#         print("After Function")
#     return wrapper

# @my_decorator
# def welcome():
#     print("Welcome to Python")
# welcome()


def logger(func):

    def wrapper():

        print("User is trying to login")

        func()

        print("Login process completed")

    return wrapper


@logger
def login():

    print("User logged in successfully")


login()

# class Klase:
#     a :int = 99
#     def __init__(self) -> None:
#         pass
#     def fun(self):
#         def funkc():
#             def st():
#                 ars = 2
#                 print("sd")
#             d = 5
#             print(d)
#             st()
#         funkc()
#         print(self.a)
# print("asd")
# def funkc():
#     def st():
#         ars = 2
#         ars / 0
#         print("sd")
#     d = 5
#     print(d)
#     st()
# kl = Klase()
# a = 12
# b = 2
# c = a - b
# # https://docs.python.org/3/library/exceptions.html 
# #d = c / 0
# import math
# math.floor(c)
# for i in range(0, 100):
#     i *= 2
#     print(a)
# funkc()
# kl.fun()
# print(a)

# Uzdevums: Atrast kļūdu
# def min(list):
#     a = list[0]
#     for x in range(1, len(list)):
#         if list[x] < a:
#             a = list[x]
#     return a
# print(min([20, 10, 30]))

class Klase:
    a :int = 0
    def __init__(self) -> None:
        raise NotImplementedError("Not implemented!!!")

# def ievadiSkaitli():   
#     while True:
#         try:
#             inp = int(input("Ievadat skaitli: "))
#             return inp
#         except:
#             print("Ievadat pareizu skaitli")
# print(ievadiSkaitli())
class ManaKluda(Exception):
    def __init__(self, obligatsParametrs :str, *args: object) -> None:
        print(f"Atrasta kļūda: {obligatsParametrs}")
        super().__init__(*args)

def kludasFunkc():
    """Summary
    
    Parameters:
      x (int) : first parameter
      y: second parameter
        with longer description
    Raises:
     Exception: if anything bad happens
    Returns:
     None: always   
    """
    import traceback
    try:
        #obj = Klase()
        #inp = int(input(""))
        raise ManaKluda("asdasd", "cits parametrs", "asdasda", "Asdasd")
    except NotImplementedError as ex:
        print("Cita kļūda")
    except OverflowError as e:
        print('????')
    # except ManaKluda as ex:
    #     print(ex.with_traceback())
    except Exception as ex: # catch
        #traceback.print_stack()
        #traceback.print_exc(1)
        print(f"Kļūda: {ex.args}")
        raise ex
import math
math.floor()
try:
    kludasFunkc()
except:
    print("!!!")
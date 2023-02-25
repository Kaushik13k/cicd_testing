# class Calculator:
#     """This class shows the functionality of the calculation wit add, subtract and multiply"""
#
#     def add(self, num1, num2):
#         """This function will be returning the addition of the two numbers"""
#         return num1 + num2
#
#     def subtract(self, num1, num2):
#         """This function will be returning the subtraction of the two numbers"""
#         return num1 - num2
#
#     def multiply(self, num1, num2):
#         """This function will be returning the multiplication of the two numbers"""
#         return num1 * num2
#
#
# print("hello world 3")
# print("hello")

from threading import Thread, Lock
import time

class JointAccount:
  current_balance = 50
  mutex = Lock()

  def dad(self):
    for i in range(1000000):
      self.mutex.acquire()
      self.current_balance += 10
      self.mutex.release()
    print('Dad saved! ')

  def son(self):
    for i in range(1000000):
      self.mutex.acquire()
      self.current_balance -= 20
      if self.current_balance <= 0:
        print('the current balance in the account is: ', self.current_balance)
      self.mutex.release()
    print('Son spend!')

account = JointAccount()
Thread(target=account.dad, args=()).start()
Thread(target=account.son, args=()).start()
time.sleep(5) # Here we are letting both the threads to be done
print("current_balance remaining is: ", account.current_balance)
print("Testing turn 1")
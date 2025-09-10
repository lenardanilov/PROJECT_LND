class CustomerDataClass:
    """Класс для обработки заказов клиента"""

    def __init__(self,customerId,customerName):
        self.CustomerId=customerId
        self.CustomerName=customerName
        self.Orders=[]

    def AddOrder(self,orderObject):
        #Добавляем заказ в список заказов клиента

        self.Orders.append(orderObject)

    def GetTotalAmount(self):
        #Считаем итоговую сумму всех заказов клиента
        
        total=0
        for o in self.Orders:
            total = total + o.amount
        return total


class OrderDataClass:
   """Класс для работы с объектом "заказ" """

   def __init__(self,orderId,amount):
        self.orderId=orderId
        self.amount=amount


def CalculateDiscount(customerObj):
   #Расчет скидки 

   totalAmount = customerObj.GetTotalAmount()
   if totalAmount > 1000:
      discount=totalAmount*0.1
   else:
      discount = 0
   return discount


def PrintCustomerReport(customerObj):
    #Вывод полученных данных

    print("Customer Report for:",customerObj.CustomerName)
    print("Total Orders:", len(customerObj.Orders))
    print("Total Amount:", customerObj.GetTotalAmount())
    print("Discount:",CalculateDiscount(customerObj))

    #Здесь надо будет сделать проверку на 0.
    print("Average Order:",customerObj.GetTotalAmount()/len(customerObj.Orders))



def MainProgram():
   #Основной метод. Выполнение рассчета скидки и вывод полученных данных

   c1=CustomerDataClass(1,"SAP Customer")
   o1=OrderDataClass(101,500)
   o2=OrderDataClass(102,800)
   c1.AddOrder(o1)
   c1.AddOrder(o2)

   PrintCustomerReport(c1)

   c2=CustomerDataClass(2,"Empty Customer")
   PrintCustomerReport(c2) 

#Запус основного метода
MainProgram()
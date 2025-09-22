"""Модуль для обработки заказов клиента."""
class CustomerDataClass:
    """Класс для обработки заказов клиента."""
    def __init__(self,customerid,customername):
        """Инициализация данных."""
        self.CustomerId=customerid
        self.CustomerName=customername
        self.Orders=[]

    def addorder(self,orderobject):
        """Добавляем заказ в список заказов клиента."""
        self.Orders.append(orderobject)

    def gettotalamount(self):
        """Считаем итоговую сумму всех заказов клиента."""
        total=0
        for o in self.Orders:
            total = total + o.amount
        return total


class OrderDataClass:
    """Класс для работы с объектом "заказ"."""

    def __init__(self,orderid,amount):
        """Инициализация данных."""        
        self.orderId=orderid
        self.amount=amount


def calculatediscount(customerobj):
   """Расчет скидки."""
   totalamount = customerobj.gettotalamount()
   
   discount = totalamount * 0.1 if totalamount > 1000 else 0
      
   return discount


def printcustomerreport(customerobj):
    """Вывод полученных данных."""
    print('Customer Report for:',customerobj.CustomerName)
    print('Total Orders:', len(customerobj.Orders))
    print('Total Amount:', customerobj.gettotalamount())
    print('Discount:', calculatediscount(customerobj))

    #проверка на 0 перед делением.
    avr_order = float('0.00')

    if len(customerobj.Orders) != 0:
        avr_order = customerobj.gettotalamount()/len(customerobj.Orders)

        print('Average Order:',avr_order)


def mainprogram():
    """Основной метод. Выполнение рассчета скидки и вывод полученных данных."""
    c1=CustomerDataClass(1,'SAP Customer')
    o1=OrderDataClass(101,500)
    o2=OrderDataClass(102,800)
    c1.addorder(o1)
    c1.addorder(o2)
    printcustomerreport(c1)
    c2=CustomerDataClass(2,'Empty Customer')
    printcustomerreport(c2) 


#Запус основного метода
mainprogram()

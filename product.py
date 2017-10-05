class Product(object):
    def __init__(self,price,itemName,weight,brand,cost):
        self.price =price
        self.itemName =itemName
        self.weight =weight
        self.brand =brand
        self.cost =cost
        self.status = "for sale"
        self.tax = 0

    def sell(self):
        self.status = "Sold"
        # print self.status
        return self

    def addtax(self,tax):
        self.price=self.price +self.price * tax
        # print self.tax
        return self

    def returnItems(self,reason):
        if(reason == "defective"): # if the item is defective
            self.status = "defective"
            self.price = 0
            print "Status:",self.status
            print "Price :" ,self.price
            return self

        elif (reason== "unopened"):    # if the box is unopened
            self.status = "for sale"
            #print "Status :" ,self.status
            #print "Price :" ,self.price
            return self

        elif (reason == "opened"):   # if the box is opened
            self.status = "Used"
            discount = self.price * 0.2 # 20% discount 
            self.price = self.price - discount
            #print "Status :" ,self.status
            #print "Price:" ,self.price
            return self

    def display_info(self):
        print "price:", self.price
        print "itemName:", self.itemName
        print "weight:", self.weight
        print "brand:", self.brand
        print "cost:", self.cost
        print "status:", self.status
        return self 

iphone = Product(999,"phone","150grams","Apple",900)
iphone.sell().addtax(0.4).returnItems("unopened").display_info()
print ''# for space between two products in output :)

android = Product(700,"phone","200grams","sumsung",650)
android.sell().addtax(0.4).returnItems("defective").display_info()
print ''

htc = Product(600,"phone","250grams","High Tech Computer Corporation",550)
htc.sell().addtax(0.4).returnItems("opened").display_info()






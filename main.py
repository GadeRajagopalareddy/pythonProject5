from pymongo import mongoClient #import mongo client to connect
#Creating instance of mongoclient
client = Mongoclient('mongodb://localhost:27027/')
db =client['cse11']
info = db.cse
student1 = {"Reg Num":"2100031211","name":"pfsd"}
student2=[{"REG NUM":"2100030771","NAME":"ABCH"},{"REG NUM":"2100030307","NAME":"ABCH"},{"REG NUM":"2100030771","NAME":"ABCH"}]
#creating document
studentdata=db.student
#Inserting data
#studentdata.insert_one(student1)
#inserting many data
studentdata.insert_many(student2)
#Fetching one data
#print(studentdata.find_one())
#fetching specific data
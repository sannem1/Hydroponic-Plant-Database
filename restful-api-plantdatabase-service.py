import requests



api_url="http://127.0.0.1:5000/insert/find"
data=[{"PlantType": "rose", "DiseaseName":"papa", "DiseaseDetails":"papa", "TreatmentOptions":"papa", "TreatmentDetails":"papa"}]
#post
def insert(dict):
    api_url = "http://127.0.0.1:5000/insert"
    todo = dict
    #get user input anf create a dictionary called todo and use it as the parameter 
    response = requests.post(api_url, json=todo)
    print(response)
    print(response.status_code)

#put
def update(planttype, dict):
    api_url = "http://127.0.0.1:5000/update?filter="
    response = requests.put(api_url + planttype, data=dict)
    print(response)
    print(response.status_code)



#delete
def remove(userinput):
    api_url = "http://127.0.0.1:5000/remove?filter="
    response = requests.delete(api_url + userinput)
    print(response)
    print(response.status_code)

#get
def find(filter):
    api_url = "http://127.0.0.1:5000/find?filter="
    response = requests.get(api_url + filter)
    print(response.json())
    print(response.status_code)

def main():
    choice=0
    while choice!=5:
        choice=int(input("Enter a choice:"))
        if choice==1:
            userinput=input("Enter PlantType: ")
            find(userinput)
        elif choice==2:
            todo={}
            PlantType=input("Enter PlantType: ")
            todo["PlantType"]=PlantType
            DiseaseName=input("Enter DiseaseName: ")
            todo["DiseaseName"]=DiseaseName
            DiseaseDetails=input("Enter DiseaseDetails: ")
            todo["DiseaseDetails"]=DiseaseDetails
            TreatmentOptions=input("Enter TreatmentOptions: ")
            todo["TreatmentOptions"]=TreatmentOptions
            TreatmentDetails=input("Enter TreatmentDetails: ")
            todo["TreatmentDetails"]=TreatmentDetails
            insert(todo)
        elif choice==3:
            todo={}
            PlantType=input("Enter PlantType: ")
            DiseaseName=input("Enter DiseaseName: ")
            todo["DiseaseName"]=DiseaseName
            DiseaseDetails=input("Enter DiseaseDetails: ")
            todo["DiseaseDetails"]=DiseaseDetails
            TreatmentOptions=input("Enter TreatmentOptions: ")
            todo["TreatmentOptions"]=TreatmentOptions
            TreatmentDetails=input("Enter TreatmentDetails: ")
            todo["TreatmentDetails"]=TreatmentDetails
            update(PlantType, todo)
        elif choice==4:
            userinput=input("Enter the Plant you wish to remove: ")
            remove(userinput)
        elif choice==5:
            quit()
        else:
            print("Invalid")
    
main()
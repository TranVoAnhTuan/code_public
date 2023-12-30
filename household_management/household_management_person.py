class BasicPersonalInformation:
    def __init__(self, iD = str, fullName = str, dateOfBirth = str , placeOfBirth = str, placeOfResidence = str, personalIdentification = str):
        self.iD = iD
        self.fullName = fullName
        self.dateOfBirth = dateOfBirth
        self.placeOfBirth = placeOfBirth
        self.placeOfResidence = placeOfResidence
        self.personalIdentification = personalIdentification
    def getInformation(self):
        print(f"""
                        Basic Personal Information:
                        ID: {self.iD} \n
                        Full Name: {self.fullName} \n
                        Date Of Birth: {self.dateOfBirth} \n
                        Place Of Birth: {self.placeOfBirth} \n
                        Place Of Residence: {self.placeOfResidence} \n
                        Personal Identification: {self.personalIdentification} \n
                """)
    def updatePlaceResidence(self, newResidence = str):
        self.placeOfResidence = newResidence

class SocialInsurance(BasicPersonalInformation):
    def __init__(self, iD=str, fullName=str, dateOfBirth=str, placeOfBirth=str, placeOfResidence=str, personalIdentification=str, no = str, nameHospital = str, issueDate = str, expirationDate = str):
        super().__init__(iD, fullName, dateOfBirth, placeOfBirth, placeOfResidence, personalIdentification)
        self.no = no
        self.nameHospital = nameHospital
        self.issueDate = issueDate
        self.expirationDate = expirationDate
    def getInformation(self):
        print(f"""  
                Social Insurance Information: \n
              """) 
        super().getInformation()
        print(f"""            
                No: {self.no} \n
                Name Hospital: {self.nameHospital} \n
                Issue Date: {self.issueDate} \n
                Expiration Date: {self.expirationDate} \n
            """)

class Visa(BasicPersonalInformation):
    def __init__(self, iD=str, fullName=str, dateOfBirth=str, placeOfBirth=str, placeOfResidence=str, personalIdentification=str, no = str, country = str, visaType = str, _class = str, issueDate = str, expirationDate = str):
        super().__init__(iD, fullName, dateOfBirth, placeOfBirth, placeOfResidence, personalIdentification)
        self.no = no
        self.country = country
        self.visaType = visaType
        self._class = _class
        self.issueDate = issueDate
        self.expirationDate = expirationDate
    def getInformation(self):
        print(f"""
                Visa Information: \n
              """)
        super().getInformation()
        print(f"""
                No: {self.no} \n
                Country: {self.country} \n
                Visa Type: {self.visaType} \n
                Class: {self._class} \n
                Issue Date: {self.issueDate} \n
                Expiration Date: {self.expirationDate} \n
              """)         

class Passport(BasicPersonalInformation):
    def __init__(self, iD=str, fullName=str, dateOfBirth=str, placeOfBirth=str, placeOfResidence=str, personalIdentification=str,no = str, issueDate = str, expirationDate = str ):
        super().__init__(iD, fullName, dateOfBirth, placeOfBirth, placeOfResidence, personalIdentification)
        self.no = no
        self.issueDate = issueDate
        self.expirationDate = expirationDate
    def getInformation(self):
        print(f"""
                Passport Information:  \n
              """)
        super().getInformation() 
        print(f"""
                no: {self.no} \n
                issueDate: {self.issueDate} \n
                """)
class DriverSLicense(BasicPersonalInformation):
    def __init__(self, iD=str, fullName=str, dateOfBirth=str, placeOfBirth=str, placeOfResidence=str, personalIdentification=str, no = str, _class = str, issueDate = str, expirationDate = str):
        super().__init__(iD, fullName, dateOfBirth, placeOfBirth, placeOfResidence, personalIdentification)
        self.no = no
        self._class = _class
        self.issueDate = issueDate
        self.expirationDate = expirationDate
    def getInformation(self):
        print(f"""
                Driver's License Information: \n
              """)
        super().getInformation()
        print(f"""
                No: {self.no} \n
                Class: {self._class} \n
                Issue Date: {self.issueDate} \n
                Expiration Date: {self.expirationDate} \n
            """)
        
class Vehicle(BasicPersonalInformation):
    def __init__(self, iD=str, fullName=str, dateOfBirth=str, placeOfBirth=str, placeOfResidence=str, personalIdentification=str, no = str, name = str, type = str, noPlate = str, engineNo = str, chassicNo = str):
        super().__init__(iD, fullName, dateOfBirth, placeOfBirth, placeOfResidence, personalIdentification)
        self.no = no
        self.name = name
        self.type = type
        self.noPlate = noPlate
        self.engineNo = engineNo
        self.chassicNo  = chassicNo
    def getInformation(self):
        print(f"""
                Vehicle Information: \n
              """)
        super().getInformation()
        print(f"""
                No: {self.no} \n
                Name: {self.name} \n
                Type: {self.type} \n
                No Plate: {self.noPlate} \n
                Engine No: {self.engineNo} \n
                Chassic No: {self.chassicNo} \n
            """)
        
class PhoneNumber(BasicPersonalInformation):
    def __init__(self, iD=str, fullName=str, dateOfBirth=str, placeOfBirth=str, placeOfResidence=str, personalIdentification=str, phoneNumber = str, mobileNetworkOperator = str, activeDate = str):
        super().__init__(iD, fullName, dateOfBirth, placeOfBirth, placeOfResidence, personalIdentification)
        self.phoneNumber = phoneNumber
        self.mobileNetworkOperator = mobileNetworkOperator
        self.activeDate = activeDate
    def getInformation(self):
        print(f"""
                Phone Number Information: \n
              """)
        super().getInformation()
        print(f"""
                Phone Number: {self.phoneNumber} \n
                Mobile Networkk Operator: {self.mobileNetworkOperator} \n
                Active Date: {self.activeDate} \n
            """)
        
class Person(BasicPersonalInformation):
    def __init__(self, iD=str, fullName=str, dateOfBirth=str, placeOfBirth=str, placeOfResidence=str, personalIdentification=str, socialInsurance = list(), visa = list(), passport = list(), drivverSLicense = list(), vehicle = list(), phoneNumber = list()):
        super().__init__(iD, fullName, dateOfBirth, placeOfBirth, placeOfResidence, personalIdentification)
        self.socialInsurance = socialInsurance
        self.visa = visa
        self.passport = passport
        self.driverSLicense = drivverSLicense
        self.vehicle = vehicle
        self.phoneNumber = phoneNumber
    def addSocialInsurance(self, newSocialInsurance = object):
        self.socialInsurance.append(newSocialInsurance)
    def addVisa(self, newVisa = object):
        self.visa.append(newVisa)
    def addPassport(self, newPassport = object):
        self.passport.appdend(newPassport)
    def addDriverSLicense(self, newDriverSLicense = object):
        self.driverSLicense.append(newDriverSLicense)
    def addVehicle(self, newVehicle = object):
        self.vehicle.append(newVehicle)
    def addPhoneNumber(self, newPhoneNumber = object):
        self.phoneNumber.append(newPhoneNumber)
    def getInformation(self):
        print(f"""
                Person Information: \n
              """)
        super().getInformation()
            
        # print('test')
        if self.socialInsurance:
            for soIn in self.socialInsurance:
                soIn.getInformation()
        if self.visa:
            for _visa in self.visa:
                _visa.getInformation()
        if self.passport:
            for _passport in self.passport:
                _passport.getInformation()
        if self.driverSLicense:
            for dSL in self.driverSLicense:
                dSL.getInformation()
        if self.vehicle:
            for _vehicle in self.vehicle:
                _vehicle.getInformation()
        if self.phoneNumber:
            for _phoneNumber in self.phoneNumber:
                _phoneNumber.getInformation()
from household_management_household import Household
from household_management_person import Person
from household_management_person import SocialInsurance
from household_management_person import Visa
from household_management_person import Passport
from household_management_person import DriverSLicense
from household_management_person import Vehicle
from household_management_person import PhoneNumber

class Quarter:
  def __init__(self, name = str, household = list()):
    self.name = name
    self.household = household

  def findIDOfHousehold(self, iD = str):
    for findID in self.household:
      if findID.iDOfHousehold  == iD:
        print(findID)
        break
    else:
      print("Non-existent")

  def findIDElectricity(self, iD = str):
    for findIDElectricity in self.household:
      if findIDElectricity.iDElectricity == iD:
        print(findIDElectricity)
        break
    else:
      print("Non-existent")

  def findIDWater(self, iD = str):
    for findIDWater in self.household:
      if findIDWater.iDWater == iD:
        print(findIDWater)
        break
    else:
      print("Non-existent")

  def findIDInternet(self, iD = str):
    for findIDInternet in self.household:
      if findIDInternet.iDInternet == iD:
        print(findIDInternet)
        break
      else:
        print("Non-existent")

  def addHousehold(self, other):
    self.household.append(other)

  def deleteIDOfHousehold(self, iD = str):
    for findID in self.household:
      if findID.iDOfHousehold == iD:
        self.household.remove(findID)
        break
    else:
      print("Non-existent")

# Create a new person object
person = Person(iD="123456789", fullName="John Doe", dateOfBirth="1980-01-01", placeOfBirth="New York, NY", placeOfResidence="Los Angeles, CA", personalIdentification="1234567890")

# Add some social insurance information
person.addSocialInsurance(SocialInsurance(iD="1234567890", fullName="John Doe", dateOfBirth="1980-01-01", placeOfBirth="New York, NY", placeOfResidence="Los Angeles, CA", personalIdentification="1234567890", no="1234567890", nameHospital="Kaiser Permanente", issueDate="2023-10-18", expirationDate="2024-10-18"))

# Add some visa information
person.addVisa(Visa(iD="1234567890", fullName="John Doe", dateOfBirth="1980-01-01", placeOfBirth="New York, NY", placeOfResidence="Los Angeles, CA", personalIdentification="1234567890", no="1234567890", country="United States", visaType="B1/B2", _class="B-2", issueDate="2023-10-18", expirationDate="2024-10-18"))

# Print the person's information
person.getInformation()


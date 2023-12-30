from household_management_person import Person
from household_management_person import SocialInsurance
from household_management_person import Visa
from household_management_person import Passport
from household_management_person import DriverSLicense
from household_management_person import Vehicle
from household_management_person import PhoneNumber

class Household:
  def __init__(self, iDOfHousehold = str, iDElectricity = str, iDWater = str, iDInternet = str, memberOfFamily = list()):
    self.iDOfHousehold = iDOfHousehold
    self.memberOfFamily = memberOfFamily
    self.iDElectricity = iDElectricity
    self.iDWater = iDWater
    self.iDInternet = iDInternet

  def addMember(self, member):
     self.memberOfFamily.append(member)

  def deleteMember(self, memberID):
    for member in self.memberOfFamily:
      if member.iD == memberID:
          self.memberOfFamily.remove(member)
          break
    else:
      print('Non-existent')

  def findMemberID(self, iD):
    for member in self.memberOfFamily:
      if member.iD == iD:
        member.getInformation()
        break
    else:
      print('Non-existent')

  def findMemberSocialInsurance(self, noSocialInsurance):
    checkStop = False
    for member in self.memberOfFamily:
      if checkStop:
        break
      for socialInsurance in member.socialInsurance:
        if socialInsurance.no == noSocialInsurance:
          member.getInformation()
          checkStop = True
          break
    else:
      print('Non-existent')
    
  def findMemberVisa(self, noVisa):
    checkStop = False
    for member in self.memberOfFamily:
      if checkStop:
        break
      for visa in member.visa:
        if visa.no == noVisa:
          member.getInformation()
          checkStop = True
          break
    else:
      print('Non-existent')

  def findMemberPassport(self, noPassport):
    checkStop = False
    for member in self.memberOfFamily:
      if checkStop:
        break
      for passport in member.passport:
        if passport.no == noPassport:
          member.getInformation()
          checkStop = True
          break
    else:
      print('Non-existent')

  def findMemberDriverSLicense(self, noDriverSLicense):
    checkStop = False
    for member in self.memberOfFamily:
      if checkStop:
        break
      for driverSLicense in member.driverSLicense:
        if driverSLicense.no == noDriverSLicense:
          member.getInformation()
          checkStop = True
          break
    else:
      print('Non-existent')

  def findMemberVehicle(self, noPlate):
    checkStop = False
    for member in self.memberOfFamily:
      if checkStop:
        break
      for vehicle in member.vehicle:
        if vehicle.noPlate == noPlate:
          member.getInformation()
          checkStop = True
          break
    else:
      print('Non-existent')    

  def findMemberPhoneNumber(self, phoneNumber):
    checkStop = False
    for member in self.memberOfFamily:
      if checkStop:
        break
      for _phoneNumber in member.phoneNumber:
        if _phoneNumber.no == phoneNumber:
          member.getInformation()
          checkStop = True
          break
    else:
      print('Non-existent')

  def getInformation(self):
    print('Household Information: \n')
    print(f"""
              ID of household: {self.iDOfHousehold} \n
              ID Electricity: {self.iDElectricity} \n
              ID Water: {self.iDWater} \n
              ID Internet: {self.iDInternet} \n
          """)
    print("Members of household: \n")
    for member in self.memberOfFamily:
      print(f'{member.fullName} \n')
      
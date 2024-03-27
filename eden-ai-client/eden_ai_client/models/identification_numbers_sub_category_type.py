from enum import Enum


class IdentificationNumbersSubCategoryType(str, Enum):
    DRIVERLICENSENUMBER = "DriverLicenseNumber"
    NATIONALHEALTHSERVICE = "NationalHealthService"
    NATIONALIDENTIFICATIONNUMBER = "NationalIdentificationNumber"
    PASSPORTNUMBER = "PassportNumber"
    RESIDENTREGISTRATIONNUMBER = "ResidentRegistrationNumber"
    SOCIALSECURITYNUMBER = "SocialSecurityNumber"

    def __str__(self) -> str:
        return str(self.value)

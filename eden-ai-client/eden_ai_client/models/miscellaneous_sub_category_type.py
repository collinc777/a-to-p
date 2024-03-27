from enum import Enum


class MiscellaneousSubCategoryType(str, Enum):
    AWSKEYS = "AWSKeys"
    AZUREKEYS = "AzureKeys"
    IP = "IP"
    LICENSEPLATE = "LicensePlate"
    MAC = "MAC"
    PASSWORD = "Password"
    URL = "URL"
    VEHICLEIDENTIFICATIONNUMBER = "VehicleIdentificationNumber"
    VOTERNUMBER = "VoterNumber"

    def __str__(self) -> str:
        return str(self.value)

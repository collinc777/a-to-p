from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resume_location import ResumeLocation


T = TypeVar("T", bound="ResumeEducationEntry")


@_attrs_define
class ResumeEducationEntry:
    """
    Attributes:
        title (str):
        start_date (str):
        end_date (str):
        location (ResumeLocation):
        establishment (str):
        description (str):
        gpa (str):
        accreditation (str):
    """

    title: str
    start_date: str
    end_date: str
    location: "ResumeLocation"
    establishment: str
    description: str
    gpa: str
    accreditation: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        start_date = self.start_date

        end_date = self.end_date

        location = self.location.to_dict()

        establishment = self.establishment

        description = self.description

        gpa = self.gpa

        accreditation = self.accreditation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "start_date": start_date,
                "end_date": end_date,
                "location": location,
                "establishment": establishment,
                "description": description,
                "gpa": gpa,
                "accreditation": accreditation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resume_location import ResumeLocation

        d = src_dict.copy()
        title = d.pop("title")

        start_date = d.pop("start_date")

        end_date = d.pop("end_date")

        location = ResumeLocation.from_dict(d.pop("location"))

        establishment = d.pop("establishment")

        description = d.pop("description")

        gpa = d.pop("gpa")

        accreditation = d.pop("accreditation")

        resume_education_entry = cls(
            title=title,
            start_date=start_date,
            end_date=end_date,
            location=location,
            establishment=establishment,
            description=description,
            gpa=gpa,
            accreditation=accreditation,
        )

        resume_education_entry.additional_properties = d
        return resume_education_entry

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

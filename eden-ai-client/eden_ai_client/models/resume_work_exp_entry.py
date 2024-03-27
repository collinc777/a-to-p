from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.resume_location import ResumeLocation


T = TypeVar("T", bound="ResumeWorkExpEntry")


@_attrs_define
class ResumeWorkExpEntry:
    """
    Attributes:
        title (str):
        start_date (str):
        end_date (str):
        company (str):
        location (ResumeLocation):
        description (str):
        industry (str):
    """

    title: str
    start_date: str
    end_date: str
    company: str
    location: "ResumeLocation"
    description: str
    industry: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title

        start_date = self.start_date

        end_date = self.end_date

        company = self.company

        location = self.location.to_dict()

        description = self.description

        industry = self.industry

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "start_date": start_date,
                "end_date": end_date,
                "company": company,
                "location": location,
                "description": description,
                "industry": industry,
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

        company = d.pop("company")

        location = ResumeLocation.from_dict(d.pop("location"))

        description = d.pop("description")

        industry = d.pop("industry")

        resume_work_exp_entry = cls(
            title=title,
            start_date=start_date,
            end_date=end_date,
            company=company,
            location=location,
            description=description,
            industry=industry,
        )

        resume_work_exp_entry.additional_properties = d
        return resume_work_exp_entry

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

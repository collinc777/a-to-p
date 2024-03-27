from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resume_location import ResumeLocation
    from ..models.resume_personal_name import ResumePersonalName


T = TypeVar("T", bound="ResumePersonalInfo")


@_attrs_define
class ResumePersonalInfo:
    """
    Attributes:
        name (ResumePersonalName):
        address (ResumeLocation):
        self_summary (str):
        objective (str):
        date_of_birth (str):
        place_of_birth (str):
        current_profession (str):
        gender (str):
        nationality (str):
        martial_status (str):
        current_salary (str):
        phones (Union[Unset, List[str]]):
        mails (Union[Unset, List[str]]):
        urls (Union[Unset, List[str]]):
        fax (Union[Unset, List[str]]):
    """

    name: "ResumePersonalName"
    address: "ResumeLocation"
    self_summary: str
    objective: str
    date_of_birth: str
    place_of_birth: str
    current_profession: str
    gender: str
    nationality: str
    martial_status: str
    current_salary: str
    phones: Union[Unset, List[str]] = UNSET
    mails: Union[Unset, List[str]] = UNSET
    urls: Union[Unset, List[str]] = UNSET
    fax: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.to_dict()

        address = self.address.to_dict()

        self_summary = self.self_summary

        objective = self.objective

        date_of_birth = self.date_of_birth

        place_of_birth = self.place_of_birth

        current_profession = self.current_profession

        gender = self.gender

        nationality = self.nationality

        martial_status = self.martial_status

        current_salary = self.current_salary

        phones: Union[Unset, List[str]] = UNSET
        if not isinstance(self.phones, Unset):
            phones = self.phones

        mails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.mails, Unset):
            mails = self.mails

        urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.urls, Unset):
            urls = self.urls

        fax: Union[Unset, List[str]] = UNSET
        if not isinstance(self.fax, Unset):
            fax = self.fax

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "address": address,
                "self_summary": self_summary,
                "objective": objective,
                "date_of_birth": date_of_birth,
                "place_of_birth": place_of_birth,
                "current_profession": current_profession,
                "gender": gender,
                "nationality": nationality,
                "martial_status": martial_status,
                "current_salary": current_salary,
            }
        )
        if phones is not UNSET:
            field_dict["phones"] = phones
        if mails is not UNSET:
            field_dict["mails"] = mails
        if urls is not UNSET:
            field_dict["urls"] = urls
        if fax is not UNSET:
            field_dict["fax"] = fax

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resume_location import ResumeLocation
        from ..models.resume_personal_name import ResumePersonalName

        d = src_dict.copy()
        name = ResumePersonalName.from_dict(d.pop("name"))

        address = ResumeLocation.from_dict(d.pop("address"))

        self_summary = d.pop("self_summary")

        objective = d.pop("objective")

        date_of_birth = d.pop("date_of_birth")

        place_of_birth = d.pop("place_of_birth")

        current_profession = d.pop("current_profession")

        gender = d.pop("gender")

        nationality = d.pop("nationality")

        martial_status = d.pop("martial_status")

        current_salary = d.pop("current_salary")

        phones = cast(List[str], d.pop("phones", UNSET))

        mails = cast(List[str], d.pop("mails", UNSET))

        urls = cast(List[str], d.pop("urls", UNSET))

        fax = cast(List[str], d.pop("fax", UNSET))

        resume_personal_info = cls(
            name=name,
            address=address,
            self_summary=self_summary,
            objective=objective,
            date_of_birth=date_of_birth,
            place_of_birth=place_of_birth,
            current_profession=current_profession,
            gender=gender,
            nationality=nationality,
            martial_status=martial_status,
            current_salary=current_salary,
            phones=phones,
            mails=mails,
            urls=urls,
            fax=fax,
        )

        resume_personal_info.additional_properties = d
        return resume_personal_info

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

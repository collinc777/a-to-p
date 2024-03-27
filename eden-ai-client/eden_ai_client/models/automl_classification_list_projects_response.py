from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.automl_classification_project import AutomlClassificationProject


T = TypeVar("T", bound="AutomlClassificationListProjectsResponse")


@_attrs_define
class AutomlClassificationListProjectsResponse:
    """
    Attributes:
        projects (List['AutomlClassificationProject']):
    """

    projects: List["AutomlClassificationProject"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        projects = []
        for projects_item_data in self.projects:
            projects_item = projects_item_data.to_dict()
            projects.append(projects_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "projects": projects,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.automl_classification_project import AutomlClassificationProject

        d = src_dict.copy()
        projects = []
        _projects = d.pop("projects")
        for projects_item_data in _projects:
            projects_item = AutomlClassificationProject.from_dict(projects_item_data)

            projects.append(projects_item)

        automl_classification_list_projects_response = cls(
            projects=projects,
        )

        automl_classification_list_projects_response.additional_properties = d
        return automl_classification_list_projects_response

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

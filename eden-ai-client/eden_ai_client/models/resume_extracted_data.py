from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resume_education import ResumeEducation
    from ..models.resume_lang import ResumeLang
    from ..models.resume_personal_info import ResumePersonalInfo
    from ..models.resume_skill import ResumeSkill
    from ..models.resume_work_exp import ResumeWorkExp


T = TypeVar("T", bound="ResumeExtractedData")


@_attrs_define
class ResumeExtractedData:
    """
    Attributes:
        personal_infos (ResumePersonalInfo):
        education (ResumeEducation):
        work_experience (ResumeWorkExp):
        languages (Union[Unset, List['ResumeLang']]):
        skills (Union[Unset, List['ResumeSkill']]):
        certifications (Union[Unset, List['ResumeSkill']]):
        courses (Union[Unset, List['ResumeSkill']]):
        publications (Union[Unset, List['ResumeSkill']]):
        interests (Union[Unset, List['ResumeSkill']]):
    """

    personal_infos: "ResumePersonalInfo"
    education: "ResumeEducation"
    work_experience: "ResumeWorkExp"
    languages: Union[Unset, List["ResumeLang"]] = UNSET
    skills: Union[Unset, List["ResumeSkill"]] = UNSET
    certifications: Union[Unset, List["ResumeSkill"]] = UNSET
    courses: Union[Unset, List["ResumeSkill"]] = UNSET
    publications: Union[Unset, List["ResumeSkill"]] = UNSET
    interests: Union[Unset, List["ResumeSkill"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        personal_infos = self.personal_infos.to_dict()

        education = self.education.to_dict()

        work_experience = self.work_experience.to_dict()

        languages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.languages, Unset):
            languages = []
            for languages_item_data in self.languages:
                languages_item = languages_item_data.to_dict()
                languages.append(languages_item)

        skills: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.skills, Unset):
            skills = []
            for skills_item_data in self.skills:
                skills_item = skills_item_data.to_dict()
                skills.append(skills_item)

        certifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certifications, Unset):
            certifications = []
            for certifications_item_data in self.certifications:
                certifications_item = certifications_item_data.to_dict()
                certifications.append(certifications_item)

        courses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.courses, Unset):
            courses = []
            for courses_item_data in self.courses:
                courses_item = courses_item_data.to_dict()
                courses.append(courses_item)

        publications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.publications, Unset):
            publications = []
            for publications_item_data in self.publications:
                publications_item = publications_item_data.to_dict()
                publications.append(publications_item)

        interests: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.interests, Unset):
            interests = []
            for interests_item_data in self.interests:
                interests_item = interests_item_data.to_dict()
                interests.append(interests_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "personal_infos": personal_infos,
                "education": education,
                "work_experience": work_experience,
            }
        )
        if languages is not UNSET:
            field_dict["languages"] = languages
        if skills is not UNSET:
            field_dict["skills"] = skills
        if certifications is not UNSET:
            field_dict["certifications"] = certifications
        if courses is not UNSET:
            field_dict["courses"] = courses
        if publications is not UNSET:
            field_dict["publications"] = publications
        if interests is not UNSET:
            field_dict["interests"] = interests

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.resume_education import ResumeEducation
        from ..models.resume_lang import ResumeLang
        from ..models.resume_personal_info import ResumePersonalInfo
        from ..models.resume_skill import ResumeSkill
        from ..models.resume_work_exp import ResumeWorkExp

        d = src_dict.copy()
        personal_infos = ResumePersonalInfo.from_dict(d.pop("personal_infos"))

        education = ResumeEducation.from_dict(d.pop("education"))

        work_experience = ResumeWorkExp.from_dict(d.pop("work_experience"))

        languages = []
        _languages = d.pop("languages", UNSET)
        for languages_item_data in _languages or []:
            languages_item = ResumeLang.from_dict(languages_item_data)

            languages.append(languages_item)

        skills = []
        _skills = d.pop("skills", UNSET)
        for skills_item_data in _skills or []:
            skills_item = ResumeSkill.from_dict(skills_item_data)

            skills.append(skills_item)

        certifications = []
        _certifications = d.pop("certifications", UNSET)
        for certifications_item_data in _certifications or []:
            certifications_item = ResumeSkill.from_dict(certifications_item_data)

            certifications.append(certifications_item)

        courses = []
        _courses = d.pop("courses", UNSET)
        for courses_item_data in _courses or []:
            courses_item = ResumeSkill.from_dict(courses_item_data)

            courses.append(courses_item)

        publications = []
        _publications = d.pop("publications", UNSET)
        for publications_item_data in _publications or []:
            publications_item = ResumeSkill.from_dict(publications_item_data)

            publications.append(publications_item)

        interests = []
        _interests = d.pop("interests", UNSET)
        for interests_item_data in _interests or []:
            interests_item = ResumeSkill.from_dict(interests_item_data)

            interests.append(interests_item)

        resume_extracted_data = cls(
            personal_infos=personal_infos,
            education=education,
            work_experience=work_experience,
            languages=languages,
            skills=skills,
            certifications=certifications,
            courses=courses,
            publications=publications,
            interests=interests,
        )

        resume_extracted_data.additional_properties = d
        return resume_extracted_data

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

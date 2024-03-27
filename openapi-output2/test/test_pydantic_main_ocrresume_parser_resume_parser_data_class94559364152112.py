# coding: utf-8

"""
Eden AI

Your project description

The version of the OpenAPI document: 2.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from openapi_client.models.pydantic_main_ocrresume_parser_resume_parser_data_class94559364152112 import (
    PydanticMainOcrresumeParserResumeParserDataClass94559364152112,
)


class TestPydanticMainOcrresumeParserResumeParserDataClass94559364152112(
    unittest.TestCase
):
    """PydanticMainOcrresumeParserResumeParserDataClass94559364152112 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> PydanticMainOcrresumeParserResumeParserDataClass94559364152112:
        """Test PydanticMainOcrresumeParserResumeParserDataClass94559364152112
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PydanticMainOcrresumeParserResumeParserDataClass94559364152112`
        """
        model = PydanticMainOcrresumeParserResumeParserDataClass94559364152112()
        if include_optional:
            return PydanticMainOcrresumeParserResumeParserDataClass94559364152112(
                extracted_data = openapi_client.models.resume_extracted_data.ResumeExtractedData(
                    personal_infos = openapi_client.models.resume_personal_info.ResumePersonalInfo(
                        name = openapi_client.models.resume_personal_name.ResumePersonalName(
                            first_name = '', 
                            last_name = '', 
                            raw_name = '', 
                            middle = '', 
                            title = '', 
                            prefix = '', 
                            sufix = '', ), 
                        address = openapi_client.models.resume_location.ResumeLocation(
                            formatted_location = '', 
                            postal_code = '', 
                            region = '', 
                            country = '', 
                            country_code = '', 
                            raw_input_location = '', 
                            street = '', 
                            street_number = '', 
                            appartment_number = '', 
                            city = '', ), 
                        self_summary = '', 
                        objective = '', 
                        date_of_birth = '', 
                        place_of_birth = '', 
                        phones = [
                            ''
                            ], 
                        mails = [
                            ''
                            ], 
                        urls = [
                            ''
                            ], 
                        fax = [
                            ''
                            ], 
                        current_profession = '', 
                        gender = '', 
                        nationality = '', 
                        martial_status = '', 
                        current_salary = '', ), 
                    education = openapi_client.models.resume_education.ResumeEducation(
                        total_years_education = 56, 
                        entries = [
                            openapi_client.models.resume_education_entry.ResumeEducationEntry(
                                title = '', 
                                start_date = '', 
                                end_date = '', 
                                location = openapi_client.models.resume_location.ResumeLocation(
                                    formatted_location = '', 
                                    postal_code = '', 
                                    region = '', 
                                    country = '', 
                                    country_code = '', 
                                    raw_input_location = '', 
                                    street = '', 
                                    street_number = '', 
                                    appartment_number = '', 
                                    city = '', ), 
                                establishment = '', 
                                description = '', 
                                gpa = '', 
                                accreditation = '', )
                            ], ), 
                    work_experience = openapi_client.models.resume_work_exp.ResumeWorkExp(
                        total_years_experience = '', 
                        entries = [
                            openapi_client.models.resume_work_exp_entry.ResumeWorkExpEntry(
                                title = '', 
                                start_date = '', 
                                end_date = '', 
                                company = '', 
                                location = , 
                                description = '', 
                                industry = '', )
                            ], ), 
                    languages = [
                        openapi_client.models.resume_lang.ResumeLang(
                            name = '', 
                            code = '', )
                        ], 
                    skills = [
                        openapi_client.models.resume_skill.ResumeSkill(
                            name = '', 
                            type = '', )
                        ], 
                    certifications = [
                        openapi_client.models.resume_skill.ResumeSkill(
                            name = '', 
                            type = '', )
                        ], 
                    courses = [
                        
                        ], 
                    publications = [
                        
                        ], 
                    interests = [
                        
                        ], ),
                original_response = None,
                status = 'success'
            )
        else:
            return PydanticMainOcrresumeParserResumeParserDataClass94559364152112(
                extracted_data = openapi_client.models.resume_extracted_data.ResumeExtractedData(
                    personal_infos = openapi_client.models.resume_personal_info.ResumePersonalInfo(
                        name = openapi_client.models.resume_personal_name.ResumePersonalName(
                            first_name = '', 
                            last_name = '', 
                            raw_name = '', 
                            middle = '', 
                            title = '', 
                            prefix = '', 
                            sufix = '', ), 
                        address = openapi_client.models.resume_location.ResumeLocation(
                            formatted_location = '', 
                            postal_code = '', 
                            region = '', 
                            country = '', 
                            country_code = '', 
                            raw_input_location = '', 
                            street = '', 
                            street_number = '', 
                            appartment_number = '', 
                            city = '', ), 
                        self_summary = '', 
                        objective = '', 
                        date_of_birth = '', 
                        place_of_birth = '', 
                        phones = [
                            ''
                            ], 
                        mails = [
                            ''
                            ], 
                        urls = [
                            ''
                            ], 
                        fax = [
                            ''
                            ], 
                        current_profession = '', 
                        gender = '', 
                        nationality = '', 
                        martial_status = '', 
                        current_salary = '', ), 
                    education = openapi_client.models.resume_education.ResumeEducation(
                        total_years_education = 56, 
                        entries = [
                            openapi_client.models.resume_education_entry.ResumeEducationEntry(
                                title = '', 
                                start_date = '', 
                                end_date = '', 
                                location = openapi_client.models.resume_location.ResumeLocation(
                                    formatted_location = '', 
                                    postal_code = '', 
                                    region = '', 
                                    country = '', 
                                    country_code = '', 
                                    raw_input_location = '', 
                                    street = '', 
                                    street_number = '', 
                                    appartment_number = '', 
                                    city = '', ), 
                                establishment = '', 
                                description = '', 
                                gpa = '', 
                                accreditation = '', )
                            ], ), 
                    work_experience = openapi_client.models.resume_work_exp.ResumeWorkExp(
                        total_years_experience = '', 
                        entries = [
                            openapi_client.models.resume_work_exp_entry.ResumeWorkExpEntry(
                                title = '', 
                                start_date = '', 
                                end_date = '', 
                                company = '', 
                                location = , 
                                description = '', 
                                industry = '', )
                            ], ), 
                    languages = [
                        openapi_client.models.resume_lang.ResumeLang(
                            name = '', 
                            code = '', )
                        ], 
                    skills = [
                        openapi_client.models.resume_skill.ResumeSkill(
                            name = '', 
                            type = '', )
                        ], 
                    certifications = [
                        openapi_client.models.resume_skill.ResumeSkill(
                            name = '', 
                            type = '', )
                        ], 
                    courses = [
                        
                        ], 
                    publications = [
                        
                        ], 
                    interests = [
                        
                        ], ),
                status = 'success',
        )
        """

    def testPydanticMainOcrresumeParserResumeParserDataClass94559364152112(self):
        """Test PydanticMainOcrresumeParserResumeParserDataClass94559364152112"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.texttopic_extractiontextanonymizationtextmoderationtextnamed_entity_recognitiontextkeyword_extractiontextsyntax_analysistextsentiment_analysis_text_analysis_request import (
    TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
)
from ...types import Response


def _get_kwargs(
    *,
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/text/keyword_extraction",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = BadRequest.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = Error.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = Error.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = NotFoundResponse.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Keyword Extraction

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**emvista**|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|0.7 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request
    |**corticalio**|`v1.3.0`|0.97 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Achinese**|`ace`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Ayacucho Quechua**|`quy`|
    |**Balinese**|`ban`|
    |**Bambara**|`bm`|
    |**Banjar**|`bjn`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bosnian**|`bs`|
    |**Buginese**|`bug`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Atlas Tamazight**|`tzm`|
    |**Central Aymara**|`ayr`|
    |**Central Kanuri**|`knc`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Chokwe**|`cjk`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**Dyula**|`dyu`|
    |**Dzongkha**|`dz`|
    |**Eastern Yiddish**|`ydd`|
    |**Egyptian Arabic**|`arz`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Halh Mongolian**|`khk`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabiyè**|`kbp`|
    |**Kabuverdianu**|`kea`|
    |**Kabyle**|`kab`|
    |**Kachin**|`kac`|
    |**Kamba (Kenya)**|`kam`|
    |**Kannada**|`kn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kimbundu**|`kmb`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latgalian**|`ltg`|
    |**Latvian**|`lv`|
    |**Ligurian**|`lij`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Luba-Katanga**|`lu`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Magahi**|`mag`|
    |**Maithili**|`mai`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manipuri**|`mni`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mesopotamian Arabic**|`acm`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Moroccan Arabic**|`ary`|
    |**Mossi**|`mos`|
    |**Najdi Arabic**|`ars`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Nigerian Fulfulde**|`fuv`|
    |**North Azerbaijani**|`azj`|
    |**North Levantine Arabic**|`apc`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Uzbek**|`uzn`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nuer**|`nus`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Plateau Malagasy**|`plt`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sicilian**|`scn`|
    |**Silesian**|`szl`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Azerbaijani**|`azb`|
    |**South Levantine Arabic**|`ajp`|
    |**Southern Pashto**|`pbt`|
    |**Southern Sotho**|`st`|
    |**Southwestern Dinka**|`dik`|
    |**Spanish**|`es`|
    |**Standard Latvian**|`lvs`|
    |**Standard Malay**|`zsm`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Ta'izzi-Adeni Arabic**|`acq`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamashek**|`tmh`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tok Pisin**|`tpi`|
    |**Tosk Albanian**|`als`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Tunisian Arabic**|`aeb`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Twi**|`tw`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Venetian**|`vec`|
    |**Vietnamese**|`vi`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**West Central Oromo**|`gaz`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (world)**|`ar-001`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Keyword Extraction

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**emvista**|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|0.7 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request
    |**corticalio**|`v1.3.0`|0.97 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Achinese**|`ace`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Ayacucho Quechua**|`quy`|
    |**Balinese**|`ban`|
    |**Bambara**|`bm`|
    |**Banjar**|`bjn`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bosnian**|`bs`|
    |**Buginese**|`bug`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Atlas Tamazight**|`tzm`|
    |**Central Aymara**|`ayr`|
    |**Central Kanuri**|`knc`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Chokwe**|`cjk`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**Dyula**|`dyu`|
    |**Dzongkha**|`dz`|
    |**Eastern Yiddish**|`ydd`|
    |**Egyptian Arabic**|`arz`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Halh Mongolian**|`khk`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabiyè**|`kbp`|
    |**Kabuverdianu**|`kea`|
    |**Kabyle**|`kab`|
    |**Kachin**|`kac`|
    |**Kamba (Kenya)**|`kam`|
    |**Kannada**|`kn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kimbundu**|`kmb`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latgalian**|`ltg`|
    |**Latvian**|`lv`|
    |**Ligurian**|`lij`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Luba-Katanga**|`lu`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Magahi**|`mag`|
    |**Maithili**|`mai`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manipuri**|`mni`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mesopotamian Arabic**|`acm`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Moroccan Arabic**|`ary`|
    |**Mossi**|`mos`|
    |**Najdi Arabic**|`ars`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Nigerian Fulfulde**|`fuv`|
    |**North Azerbaijani**|`azj`|
    |**North Levantine Arabic**|`apc`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Uzbek**|`uzn`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nuer**|`nus`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Plateau Malagasy**|`plt`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sicilian**|`scn`|
    |**Silesian**|`szl`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Azerbaijani**|`azb`|
    |**South Levantine Arabic**|`ajp`|
    |**Southern Pashto**|`pbt`|
    |**Southern Sotho**|`st`|
    |**Southwestern Dinka**|`dik`|
    |**Spanish**|`es`|
    |**Standard Latvian**|`lvs`|
    |**Standard Malay**|`zsm`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Ta'izzi-Adeni Arabic**|`acq`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamashek**|`tmh`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tok Pisin**|`tpi`|
    |**Tosk Albanian**|`als`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Tunisian Arabic**|`aeb`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Twi**|`tw`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Venetian**|`vec`|
    |**Vietnamese**|`vi`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**West Central Oromo**|`gaz`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (world)**|`ar-001`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Keyword Extraction

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**emvista**|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|0.7 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request
    |**corticalio**|`v1.3.0`|0.97 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Achinese**|`ace`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Ayacucho Quechua**|`quy`|
    |**Balinese**|`ban`|
    |**Bambara**|`bm`|
    |**Banjar**|`bjn`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bosnian**|`bs`|
    |**Buginese**|`bug`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Atlas Tamazight**|`tzm`|
    |**Central Aymara**|`ayr`|
    |**Central Kanuri**|`knc`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Chokwe**|`cjk`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**Dyula**|`dyu`|
    |**Dzongkha**|`dz`|
    |**Eastern Yiddish**|`ydd`|
    |**Egyptian Arabic**|`arz`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Halh Mongolian**|`khk`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabiyè**|`kbp`|
    |**Kabuverdianu**|`kea`|
    |**Kabyle**|`kab`|
    |**Kachin**|`kac`|
    |**Kamba (Kenya)**|`kam`|
    |**Kannada**|`kn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kimbundu**|`kmb`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latgalian**|`ltg`|
    |**Latvian**|`lv`|
    |**Ligurian**|`lij`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Luba-Katanga**|`lu`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Magahi**|`mag`|
    |**Maithili**|`mai`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manipuri**|`mni`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mesopotamian Arabic**|`acm`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Moroccan Arabic**|`ary`|
    |**Mossi**|`mos`|
    |**Najdi Arabic**|`ars`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Nigerian Fulfulde**|`fuv`|
    |**North Azerbaijani**|`azj`|
    |**North Levantine Arabic**|`apc`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Uzbek**|`uzn`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nuer**|`nus`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Plateau Malagasy**|`plt`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sicilian**|`scn`|
    |**Silesian**|`szl`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Azerbaijani**|`azb`|
    |**South Levantine Arabic**|`ajp`|
    |**Southern Pashto**|`pbt`|
    |**Southern Sotho**|`st`|
    |**Southwestern Dinka**|`dik`|
    |**Spanish**|`es`|
    |**Standard Latvian**|`lvs`|
    |**Standard Malay**|`zsm`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Ta'izzi-Adeni Arabic**|`acq`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamashek**|`tmh`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tok Pisin**|`tpi`|
    |**Tosk Albanian**|`als`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Tunisian Arabic**|`aeb`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Twi**|`tw`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Venetian**|`vec`|
    |**Vietnamese**|`vi`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**West Central Oromo**|`gaz`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (world)**|`ar-001`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BadRequest, Error, NotFoundResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeywordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Keyword Extraction

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Version|Price|Billing unit|
    |----|-------|-----|------------|
    |**amazon**|`boto3 (v1.15.18)`|1.0 (per 1000000 char)|300 char
    |**ibm**|`v1 (2021-08-01)`|0.3 (per 1000000 char)|10000 char
    |**microsoft**|`v3.1`|1.0 (per 1000000 char)|1000 char
    |**emvista**|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**openai**|`v3.0.0`|20.0 (per 1000000 token)|1 token
    |**tenstorrent**|`v1.0.0`|0.7 (per 1000000 char)|1000 char
    |**nlpcloud**|`v1`|25.0 (per 1000 request)|1 request
    |**corticalio**|`v1.3.0`|0.97 (per 1000 request)|1 request


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Achinese**|`ace`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Asturian**|`ast`|
    |**Awadhi**|`awa`|
    |**Ayacucho Quechua**|`quy`|
    |**Balinese**|`ban`|
    |**Bambara**|`bm`|
    |**Banjar**|`bjn`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Bhojpuri**|`bho`|
    |**Bosnian**|`bs`|
    |**Buginese**|`bug`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Central Atlas Tamazight**|`tzm`|
    |**Central Aymara**|`ayr`|
    |**Central Kanuri**|`knc`|
    |**Central Khmer**|`km`|
    |**Central Kurdish**|`ckb`|
    |**Chhattisgarhi**|`hne`|
    |**Chinese**|`zh`|
    |**Chokwe**|`cjk`|
    |**Crimean Tatar**|`crh`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dutch**|`nl`|
    |**Dyula**|`dyu`|
    |**Dzongkha**|`dz`|
    |**Eastern Yiddish**|`ydd`|
    |**Egyptian Arabic**|`arz`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Friulian**|`fur`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Haitian**|`ht`|
    |**Halh Mongolian**|`khk`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Hindi**|`hi`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Irish**|`ga`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabiyè**|`kbp`|
    |**Kabuverdianu**|`kea`|
    |**Kabyle**|`kab`|
    |**Kachin**|`kac`|
    |**Kamba (Kenya)**|`kam`|
    |**Kannada**|`kn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kimbundu**|`kmb`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Kongo**|`kg`|
    |**Korean**|`ko`|
    |**Lao**|`lo`|
    |**Latgalian**|`ltg`|
    |**Latvian**|`lv`|
    |**Ligurian**|`lij`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lombard**|`lmo`|
    |**Luba-Katanga**|`lu`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Magahi**|`mag`|
    |**Maithili**|`mai`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manipuri**|`mni`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Mesopotamian Arabic**|`acm`|
    |**Minangkabau**|`min`|
    |**Modern Greek (1453-)**|`el`|
    |**Moroccan Arabic**|`ary`|
    |**Mossi**|`mos`|
    |**Najdi Arabic**|`ars`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Nigerian Fulfulde**|`fuv`|
    |**North Azerbaijani**|`azj`|
    |**North Levantine Arabic**|`apc`|
    |**Northern Kurdish**|`kmr`|
    |**Northern Uzbek**|`uzn`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nuer**|`nus`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Oriya (macrolanguage)**|`or`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Plateau Malagasy**|`plt`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Romanian**|`ro`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Samoan**|`sm`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sicilian**|`scn`|
    |**Silesian**|`szl`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Azerbaijani**|`azb`|
    |**South Levantine Arabic**|`ajp`|
    |**Southern Pashto**|`pbt`|
    |**Southern Sotho**|`st`|
    |**Southwestern Dinka**|`dik`|
    |**Spanish**|`es`|
    |**Standard Latvian**|`lvs`|
    |**Standard Malay**|`zsm`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Ta'izzi-Adeni Arabic**|`acq`|
    |**Tagalog**|`tl`|
    |**Tajik**|`tg`|
    |**Tamashek**|`tmh`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tok Pisin**|`tpi`|
    |**Tosk Albanian**|`als`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Tunisian Arabic**|`aeb`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Twi**|`tw`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Venetian**|`vec`|
    |**Vietnamese**|`vi`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**West Central Oromo**|`gaz`|
    |**Wolof**|`wo`|
    |**Xhosa**|`xh`|
    |**Yoruba**|`yo`|
    |**Yue Chinese**|`yue`|
    |**Zulu**|`zu`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Arabic (world)**|`ar-001`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Chinese (Taiwan)**|`zh-TW`|
    |**Chinese (Traditional)**|`zh-Hant`|
    |**Persian (Afghanistan)**|`fa-AF`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Portugal)**|`pt-PT`|

    </details>

    Args:
        body (TexttopicExtractiontextanonymizationtextmoderationtextnamedEntityRecognitiontextkeyw
            ordExtractiontextsyntaxAnalysistextsentimentAnalysisTextAnalysisRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BadRequest, Error, NotFoundResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed

from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bad_request import BadRequest
from ...models.error import Error
from ...models.not_found_response import NotFoundResponse
from ...models.textsummarize_summarize_request import TextsummarizeSummarizeRequest
from ...types import Response


def _get_kwargs(
    *,
    body: TextsummarizeSummarizeRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/text/summarize",
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
    body: TextsummarizeSummarizeRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Summarize

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request
    |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char
    |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token
    |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char
    |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request
    |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Awadhi**|`awa`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dhivehi**|`dv`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Maithili**|`mai`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Min Nan Chinese**|`nan`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romance languages**|`roa`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Seselwa Creole French**|`crs`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|
    |**me**|`me`|
    |**ra**|`ra`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Brazil)**|`pt-br`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Portuguese (Portugal)**|`pt-pt`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`summarize-medium`|
    ||`summarize-xlarge`|

    </details><details><summary>alephalpha</summary>





    |Name|Value|
    |----|-----|
    |**alephalpha**|`luminous-base`|
    ||`luminous-base-control`|
    ||`luminous-extended`|
    ||`luminous-extended-control`|
    ||`luminous-supreme`|
    ||`luminous-supreme-control`|

    </details><details><summary>nlpcloud</summary>





    |Name|Value|
    |----|-----|
    |**nlpcloud**|`bart-large-cnn`|
    ||`chatdolphin`|
    ||`fast-gpt-j`|
    ||`finetuned-llama-2-70b`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextsummarizeSummarizeRequest):

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
    body: TextsummarizeSummarizeRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Summarize

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request
    |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char
    |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token
    |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char
    |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request
    |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Awadhi**|`awa`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dhivehi**|`dv`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Maithili**|`mai`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Min Nan Chinese**|`nan`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romance languages**|`roa`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Seselwa Creole French**|`crs`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|
    |**me**|`me`|
    |**ra**|`ra`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Brazil)**|`pt-br`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Portuguese (Portugal)**|`pt-pt`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`summarize-medium`|
    ||`summarize-xlarge`|

    </details><details><summary>alephalpha</summary>





    |Name|Value|
    |----|-----|
    |**alephalpha**|`luminous-base`|
    ||`luminous-base-control`|
    ||`luminous-extended`|
    ||`luminous-extended-control`|
    ||`luminous-supreme`|
    ||`luminous-supreme-control`|

    </details><details><summary>nlpcloud</summary>





    |Name|Value|
    |----|-----|
    |**nlpcloud**|`bart-large-cnn`|
    ||`chatdolphin`|
    ||`fast-gpt-j`|
    ||`finetuned-llama-2-70b`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextsummarizeSummarizeRequest):

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
    body: TextsummarizeSummarizeRequest,
) -> Response[Union[BadRequest, Error, NotFoundResponse]]:
    """Summarize

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request
    |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char
    |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token
    |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char
    |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request
    |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Awadhi**|`awa`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dhivehi**|`dv`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Maithili**|`mai`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Min Nan Chinese**|`nan`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romance languages**|`roa`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Seselwa Creole French**|`crs`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|
    |**me**|`me`|
    |**ra**|`ra`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Brazil)**|`pt-br`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Portuguese (Portugal)**|`pt-pt`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`summarize-medium`|
    ||`summarize-xlarge`|

    </details><details><summary>alephalpha</summary>





    |Name|Value|
    |----|-----|
    |**alephalpha**|`luminous-base`|
    ||`luminous-base-control`|
    ||`luminous-extended`|
    ||`luminous-extended-control`|
    ||`luminous-supreme`|
    ||`luminous-supreme-control`|

    </details><details><summary>nlpcloud</summary>





    |Name|Value|
    |----|-----|
    |**nlpcloud**|`bart-large-cnn`|
    ||`chatdolphin`|
    ||`fast-gpt-j`|
    ||`finetuned-llama-2-70b`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextsummarizeSummarizeRequest):

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
    body: TextsummarizeSummarizeRequest,
) -> Optional[Union[BadRequest, Error, NotFoundResponse]]:
    """Summarize

     <details><summary><strong style='color: #0072a3; cursor: pointer'>Available
    Providers</strong></summary>



    |Provider|Model|Version|Price|Billing unit|
    |----|----|-------|-----|------------|
    |**connexun**|-|`v1.0`|2.0 (per 1000 request)|1 request
    |**microsoft**|-|`v3.1`|2.0 (per 1000000 char)|1000 char
    |**openai**|-|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-4**|`v3.0.0`|60.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-1106**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo**|`v3.0.0`|2.0 (per 1000000 token)|1 token
    |**openai**|**gpt-3.5-turbo-16k**|`v3.0.0`|4.0 (per 1000000 token)|1 token
    |**emvista**|-|`v1.0`|1.0 (per 1000000 char)|1000 char
    |**cohere**|-|`2022-12-06`|2.0 (per 1000000 token)|1 token
    |**alephalpha**|-|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base**|`1.12.0`|1.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended**|`1.12.0`|1.5 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme**|`1.12.0`|50.0 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-base-control**|`1.12.0`|1.25 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-extended-control**|`1.12.0`|1.8 (per 1000000 char)|1 char
    |**alephalpha**|**luminous-supreme-control**|`1.12.0`|62.5 (per 1000000 char)|1 char
    |**nlpcloud**|-|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**bart-large-cnn**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**fast-gpt-j**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**finetuned-llama-2-70b**|`v1`|25.0 (per 1000 request)|1 request
    |**nlpcloud**|**chatdolphin**|`v1`|25.0 (per 1000 request)|1 request
    |**ai21labs**|-|`v1`|0.005 (per 1000 char)|1000 char
    |**anthropic**|**claude-3-haiku-20240307-v1:0**|`bedrock-2023-05-31`|1.25 (per 1000000 token)|1
    token
    |**anthropic**|**claude-3-sonnet-20240229-v1:0**|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1
    token
    |**anthropic**|**claude-instant-v1**|`bedrock-2023-05-31`|2.4 (per 1000000 token)|1 token
    |**anthropic**|**claude-v2**|`bedrock-2023-05-31`|24.0 (per 1000000 token)|1 token
    |**anthropic**|-|`bedrock-2023-05-31`|15.0 (per 1000000 token)|1 token


    </details>

    <details><summary>Supported Languages</summary>





    |Name|Value|
    |----|-----|
    |**Abkhazian**|`ab`|
    |**Acoli**|`ach`|
    |**Afar**|`aa`|
    |**Afrikaans**|`af`|
    |**Akan**|`ak`|
    |**Albanian**|`sq`|
    |**American Sign Language**|`ase`|
    |**Amharic**|`am`|
    |**Arabic**|`ar`|
    |**Aragonese**|`an`|
    |**Argentine Sign Language**|`aed`|
    |**Armenian**|`hy`|
    |**Assamese**|`as`|
    |**Avaric**|`av`|
    |**Avestan**|`ae`|
    |**Awadhi**|`awa`|
    |**Aymara**|`ay`|
    |**Azerbaijani**|`az`|
    |**Bambara**|`bm`|
    |**Bashkir**|`ba`|
    |**Basque**|`eu`|
    |**Belarusian**|`be`|
    |**Bemba (Zambia)**|`bem`|
    |**Bengali**|`bn`|
    |**Berber languages**|`ber`|
    |**Bhojpuri**|`bho`|
    |**Bihari languages**|`bh`|
    |**Bislama**|`bi`|
    |**Bosnian**|`bs`|
    |**Brazilian Sign Language**|`bzs`|
    |**Breton**|`br`|
    |**Bulgarian**|`bg`|
    |**Burmese**|`my`|
    |**Catalan**|`ca`|
    |**Cebuano**|`ceb`|
    |**Celtic languages**|`cel`|
    |**Central Bikol**|`bcl`|
    |**Central Khmer**|`km`|
    |**Chamorro**|`ch`|
    |**Chechen**|`ce`|
    |**Chilean Sign Language**|`csg`|
    |**Chinese**|`zh`|
    |**Church Slavic**|`cu`|
    |**Chuukese**|`chk`|
    |**Chuvash**|`cv`|
    |**Colombian Sign Language**|`csn`|
    |**Congo Swahili**|`swc`|
    |**Cornish**|`kw`|
    |**Corsican**|`co`|
    |**Cree**|`cr`|
    |**Croatian**|`hr`|
    |**Czech**|`cs`|
    |**Danish**|`da`|
    |**Dhivehi**|`dv`|
    |**Dogri (macrolanguage)**|`doi`|
    |**Dutch**|`nl`|
    |**Dzongkha**|`dz`|
    |**Efik**|`efi`|
    |**English**|`en`|
    |**Esperanto**|`eo`|
    |**Estonian**|`et`|
    |**Ewe**|`ee`|
    |**Faroese**|`fo`|
    |**Fijian**|`fj`|
    |**Finnish**|`fi`|
    |**Finnish Sign Language**|`fse`|
    |**Fon**|`fon`|
    |**French**|`fr`|
    |**Fulah**|`ff`|
    |**Ga**|`gaa`|
    |**Galician**|`gl`|
    |**Ganda**|`lg`|
    |**Georgian**|`ka`|
    |**German**|`de`|
    |**Gilbertese**|`gil`|
    |**Guarani**|`gn`|
    |**Gujarati**|`gu`|
    |**Gun**|`guw`|
    |**Haitian**|`ht`|
    |**Hausa**|`ha`|
    |**Hebrew**|`he`|
    |**Herero**|`hz`|
    |**Hiligaynon**|`hil`|
    |**Hindi**|`hi`|
    |**Hiri Motu**|`ho`|
    |**Hungarian**|`hu`|
    |**Icelandic**|`is`|
    |**Ido**|`io`|
    |**Igbo**|`ig`|
    |**Iloko**|`ilo`|
    |**Indonesian**|`id`|
    |**Interlingua (International Auxiliary Language Association)**|`ia`|
    |**Interlingue**|`ie`|
    |**Inuktitut**|`iu`|
    |**Inupiaq**|`ik`|
    |**Irish**|`ga`|
    |**Isoko**|`iso`|
    |**Isthmus Zapotec**|`zai`|
    |**Italian**|`it`|
    |**Japanese**|`ja`|
    |**Javanese**|`jv`|
    |**Kabyle**|`kab`|
    |**Kalaallisut**|`kl`|
    |**Kannada**|`kn`|
    |**Kanuri**|`kr`|
    |**Kaonde**|`kqn`|
    |**Kashmiri**|`ks`|
    |**Kazakh**|`kk`|
    |**Kikuyu**|`ki`|
    |**Kinyarwanda**|`rw`|
    |**Kirghiz**|`ky`|
    |**Komi**|`kv`|
    |**Kongo**|`kg`|
    |**Konkani (macrolanguage)**|`kok`|
    |**Korean**|`ko`|
    |**Kuanyama**|`kj`|
    |**Kurdish**|`ku`|
    |**Kwangali**|`kwn`|
    |**Lao**|`lo`|
    |**Latin**|`la`|
    |**Latvian**|`lv`|
    |**Limburgan**|`li`|
    |**Lingala**|`ln`|
    |**Lithuanian**|`lt`|
    |**Lozi**|`loz`|
    |**Luba-Katanga**|`lu`|
    |**Luba-Lulua**|`lua`|
    |**Lunda**|`lun`|
    |**Luo (Kenya and Tanzania)**|`luo`|
    |**Lushai**|`lus`|
    |**Luvale**|`lue`|
    |**Luxembourgish**|`lb`|
    |**Macedonian**|`mk`|
    |**Maithili**|`mai`|
    |**Malagasy**|`mg`|
    |**Malay (macrolanguage)**|`ms`|
    |**Malayalam**|`ml`|
    |**Maltese**|`mt`|
    |**Manx**|`gv`|
    |**Maori**|`mi`|
    |**Marathi**|`mr`|
    |**Marshallese**|`mh`|
    |**Mexican Sign Language**|`mfs`|
    |**Min Nan Chinese**|`nan`|
    |**Modern Greek (1453-)**|`el`|
    |**Mongolian**|`mn`|
    |**Morisyen**|`mfe`|
    |**Mossi**|`mos`|
    |**Nauru**|`na`|
    |**Navajo**|`nv`|
    |**Ndonga**|`ng`|
    |**Nepali (macrolanguage)**|`ne`|
    |**Niuean**|`niu`|
    |**North Ndebele**|`nd`|
    |**Northern Sami**|`se`|
    |**Norwegian**|`no`|
    |**Norwegian Bokmål**|`nb`|
    |**Norwegian Nynorsk**|`nn`|
    |**Nyaneka**|`nyk`|
    |**Nyanja**|`ny`|
    |**Occitan (post 1500)**|`oc`|
    |**Ojibwa**|`oj`|
    |**Oriya (macrolanguage)**|`or`|
    |**Oromo**|`om`|
    |**Ossetian**|`os`|
    |**Pali**|`pi`|
    |**Pangasinan**|`pag`|
    |**Panjabi**|`pa`|
    |**Papiamento**|`pap`|
    |**Pedi**|`nso`|
    |**Persian**|`fa`|
    |**Peruvian Sign Language**|`prl`|
    |**Pijin**|`pis`|
    |**Pohnpeian**|`pon`|
    |**Polish**|`pl`|
    |**Portuguese**|`pt`|
    |**Pushto**|`ps`|
    |**Quechua**|`qu`|
    |**Romance languages**|`roa`|
    |**Romanian**|`mo`|
    |**Romanian**|`ro`|
    |**Romansh**|`rm`|
    |**Rundi**|`rn`|
    |**Russian**|`ru`|
    |**Ruund**|`rnd`|
    |**Samoan**|`sm`|
    |**San Salvador Kongo**|`kwy`|
    |**Sango**|`sg`|
    |**Sanskrit**|`sa`|
    |**Santali**|`sat`|
    |**Sardinian**|`sc`|
    |**Scottish Gaelic**|`gd`|
    |**Serbian**|`sr`|
    |**Seselwa Creole French**|`crs`|
    |**Shan**|`shn`|
    |**Shona**|`sn`|
    |**Sichuan Yi**|`ii`|
    |**Sicilian**|`scn`|
    |**Sindhi**|`sd`|
    |**Sinhala**|`si`|
    |**Slovak**|`sk`|
    |**Slovenian**|`sl`|
    |**Somali**|`so`|
    |**South Ndebele**|`nr`|
    |**Southern Sotho**|`st`|
    |**Spanish**|`es`|
    |**Spanish Sign Language**|`ssp`|
    |**Sranan Tongo**|`srn`|
    |**Sundanese**|`su`|
    |**Swahili (macrolanguage)**|`sw`|
    |**Swati**|`ss`|
    |**Swedish**|`sv`|
    |**Tagalog**|`tl`|
    |**Tahitian**|`ty`|
    |**Tajik**|`tg`|
    |**Tamil**|`ta`|
    |**Tatar**|`tt`|
    |**Telugu**|`te`|
    |**Tetela**|`tll`|
    |**Tetun Dili**|`tdt`|
    |**Thai**|`th`|
    |**Tibetan**|`bo`|
    |**Tigrinya**|`ti`|
    |**Tiv**|`tiv`|
    |**Tok Pisin**|`tpi`|
    |**Tonga (Tonga Islands)**|`to`|
    |**Tonga (Zambia)**|`toi`|
    |**Tsonga**|`ts`|
    |**Tswana**|`tn`|
    |**Tumbuka**|`tum`|
    |**Turkish**|`tr`|
    |**Turkmen**|`tk`|
    |**Tuvalu**|`tvl`|
    |**Twi**|`tw`|
    |**Tzotzil**|`tzo`|
    |**Uighur**|`ug`|
    |**Ukrainian**|`uk`|
    |**Umbundu**|`umb`|
    |**Urdu**|`ur`|
    |**Uzbek**|`uz`|
    |**Venda**|`ve`|
    |**Venezuelan Sign Language**|`vsl`|
    |**Vietnamese**|`vi`|
    |**Volapük**|`vo`|
    |**Wallisian**|`wls`|
    |**Walloon**|`wa`|
    |**Waray (Philippines)**|`war`|
    |**Welsh**|`cy`|
    |**Western Frisian**|`fy`|
    |**Wolaytta**|`wal`|
    |**Wolof**|`wo`|
    |**Wu Chinese**|`wuu`|
    |**Xhosa**|`xh`|
    |**Yapese**|`yap`|
    |**Yiddish**|`yi`|
    |**Yoruba**|`yo`|
    |**Yucateco**|`yua`|
    |**Yue Chinese**|`yue`|
    |**Zande (individual language)**|`zne`|
    |**Zhuang**|`za`|
    |**Zulu**|`zu`|
    |**me**|`me`|
    |**ra**|`ra`|

    </details><details><summary>Supported Detailed Languages</summary>





    |Name|Value|
    |----|-----|
    |**Auto detection**|`auto-detect`|
    |**Chinese (Simplified)**|`zh-Hans`|
    |**Portuguese (Brazil)**|`pt-BR`|
    |**Portuguese (Brazil)**|`pt-br`|
    |**Portuguese (Portugal)**|`pt-PT`|
    |**Portuguese (Portugal)**|`pt-pt`|

    </details><details><summary>Supported Models</summary><details><summary>openai</summary>





    |Name|Value|
    |----|-----|
    |**openai**|`gpt-3.5-turbo`|
    ||`gpt-3.5-turbo-1106`|
    ||`gpt-3.5-turbo-16k`|
    ||`gpt-4`|

    </details><details><summary>cohere</summary>





    |Name|Value|
    |----|-----|
    |**cohere**|`summarize-medium`|
    ||`summarize-xlarge`|

    </details><details><summary>alephalpha</summary>





    |Name|Value|
    |----|-----|
    |**alephalpha**|`luminous-base`|
    ||`luminous-base-control`|
    ||`luminous-extended`|
    ||`luminous-extended-control`|
    ||`luminous-supreme`|
    ||`luminous-supreme-control`|

    </details><details><summary>nlpcloud</summary>





    |Name|Value|
    |----|-----|
    |**nlpcloud**|`bart-large-cnn`|
    ||`chatdolphin`|
    ||`fast-gpt-j`|
    ||`finetuned-llama-2-70b`|

    </details><details><summary>anthropic</summary>





    |Name|Value|
    |----|-----|
    |**anthropic**|`claude-3-sonnet-20240229-v1:0`|
    ||`claude-instant-v1`|
    ||`claude-v2`|

    </details>

    </details>

    Args:
        body (TextsummarizeSummarizeRequest):

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

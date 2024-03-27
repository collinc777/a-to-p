# openapi_client.TextToSpeechAsyncApi

All URIs are relative to *https://api.edenai.run/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audio_audio_text_to_speech_async_create**](TextToSpeechAsyncApi.md#audio_audio_text_to_speech_async_create) | **POST** /audio/text_to_speech_async | Text to Speech launch job
[**audio_audio_text_to_speech_async_destroy**](TextToSpeechAsyncApi.md#audio_audio_text_to_speech_async_destroy) | **DELETE** /audio/text_to_speech_async | Text To Speech delete Jobs
[**audio_audio_text_to_speech_async_retrieve**](TextToSpeechAsyncApi.md#audio_audio_text_to_speech_async_retrieve) | **GET** /audio/text_to_speech_async | Text To Speech list jobs
[**audio_audio_text_to_speech_async_retrieve2**](TextToSpeechAsyncApi.md#audio_audio_text_to_speech_async_retrieve2) | **GET** /audio/text_to_speech_async/{public_id} | Text To Speech Get Job Results


# **audio_audio_text_to_speech_async_create**
> LaunchAsyncJobResponse audio_audio_text_to_speech_async_create(providers, text, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, settings=settings, language=language, option=option, rate=rate, pitch=pitch, volume=volume, audio_format=audio_format, sampling_rate=sampling_rate)

Text to Speech launch job

<details><summary><strong style='color: #0072a3; cursor: pointer'>Available Providers</strong></summary>    |Provider|Model|Version|Price|Billing unit| |----|----|-------|-----|------------| |**lovoai**|-|`v1`|0.16 (per 1000 char)|1 char |**amazon**|-|`boto3 (v1.15.18)`|4.0 (per 1000000 char)|1 char |**amazon**|**Neural**|`boto3 (v1.15.18)`|16.0 (per 1000000 char)|1 char   </details>  <details><summary>Supported Languages</summary>      |Name|Value| |----|-----| |**Afrikaans**|`af`| |**Albanian**|`sq`| |**Amharic**|`am`| |**Arabic**|`ar`| |**Armenian**|`hy`| |**Azerbaijani**|`az`| |**Basque**|`eu`| |**Bengali**|`bn`| |**Bosnian**|`bs`| |**Burmese**|`my`| |**Catalan**|`ca`| |**Central Khmer**|`km`| |**Chinese**|`zh`| |**Croatian**|`hr`| |**Czech**|`cs`| |**Danish**|`da`| |**Dutch**|`nl`| |**English**|`en`| |**Estonian**|`et`| |**Filipino**|`fil`| |**Finnish**|`fi`| |**French**|`fr`| |**Galician**|`gl`| |**Georgian**|`ka`| |**German**|`de`| |**Hebrew**|`he`| |**Hindi**|`hi`| |**Hungarian**|`hu`| |**Icelandic**|`is`| |**Indonesian**|`id`| |**Irish**|`ga`| |**Italian**|`it`| |**Japanese**|`ja`| |**Javanese**|`jv`| |**Kazakh**|`kk`| |**Korean**|`ko`| |**Lao**|`lo`| |**Latvian**|`lv`| |**Lithuanian**|`lt`| |**Macedonian**|`mk`| |**Malay (macrolanguage)**|`ms`| |**Malayalam**|`ml`| |**Maltese**|`mt`| |**Mandarin Chinese**|`cmn`| |**Marathi**|`mr`| |**Mongolian**|`mn`| |**Nepali (macrolanguage)**|`ne`| |**Norwegian Bokmål**|`nb`| |**Persian**|`fa`| |**Polish**|`pl`| |**Portuguese**|`pt`| |**Pushto**|`ps`| |**Romanian**|`ro`| |**Russian**|`ru`| |**Serbian**|`sr`| |**Sinhala**|`si`| |**Slovak**|`sk`| |**Slovenian**|`sl`| |**Somali**|`so`| |**Spanish**|`es`| |**Standard Arabic**|`arb`| |**Sundanese**|`su`| |**Swahili (macrolanguage)**|`sw`| |**Swedish**|`sv`| |**Tamil**|`ta`| |**Telugu**|`te`| |**Thai**|`th`| |**Turkish**|`tr`| |**Ukrainian**|`uk`| |**Urdu**|`ur`| |**Uzbek**|`uz`| |**Vietnamese**|`vi`| |**Welsh**|`cy`| |**Wu Chinese**|`wuu`| |**Xhosa**|`xh`| |**Yue Chinese**|`yue`| |**Zulu**|`zu`|  </details><details><summary>Supported Detailed Languages</summary>      |Name|Value| |----|-----| |**Afrikaans (South Africa)**|`af-ZA`| |**Albanian (Albania)**|`sq-AL`| |**Amharic (Ethiopia)**|`am-ET`| |**Arabic (Algeria)**|`ar-DZ`| |**Arabic (Bahrain)**|`ar-BH`| |**Arabic (Egypt)**|`ar-EG`| |**Arabic (Iraq)**|`ar-IQ`| |**Arabic (Jordan)**|`ar-JO`| |**Arabic (Kuwait)**|`ar-KW`| |**Arabic (Lebanon)**|`ar-LB`| |**Arabic (Libya)**|`ar-LY`| |**Arabic (Morocco)**|`ar-MA`| |**Arabic (Oman)**|`ar-OM`| |**Arabic (Qatar)**|`ar-QA`| |**Arabic (Saudi Arabia)**|`ar-SA`| |**Arabic (Tunisia)**|`ar-TN`| |**Arabic (United Arab Emirates)**|`ar-AE`| |**Armenian (Armenia)**|`hy-AM`| |**Azerbaijani (Azerbaijan)**|`az-AZ`| |**Bangla (India)**|`bn-IN`| |**Basque (Spain)**|`eu-ES`| |**Bosnian (Bosnia & Herzegovina)**|`bs-BA`| |**Burmese (Myanmar (Burma))**|`my-MM`| |**Cantonese (China)**|`yue-CN`| |**Catalan (Spain)**|`ca-ES`| |**Chinese (China)**|`zh-CN`| |**Chinese (China)**|`zh-CN-henan`| |**Chinese (China)**|`zh-CN-shandong`| |**Chinese (China)**|`zh-CN-sichuan`| |**Chinese (Hong Kong SAR China)**|`zh-HK`| |**Chinese (Taiwan)**|`zh-TW`| |**Croatian (Croatia)**|`hr-HR`| |**Czech (Czechia)**|`cs-CZ`| |**Danish (Denmark)**|`da-DK`| |**Dutch (Belgium)**|`nl-BE`| |**Dutch (Netherlands)**|`nl-NL`| |**English (Australia)**|`en-AU`| |**English (Canada)**|`en-CA`| |**English (Curaçao)**|`en-AN`| |**English (Hong Kong SAR China)**|`en-HK`| |**English (India)**|`en-IN`| |**English (Ireland)**|`en-IE`| |**English (Kenya)**|`en-KE`| |**English (New Zealand)**|`en-NZ`| |**English (Nigeria)**|`en-NG`| |**English (Philippines)**|`en-PH`| |**English (Singapore)**|`en-SG`| |**English (South Africa)**|`en-ZA`| |**English (Tanzania)**|`en-TZ`| |**English (United Kingdom)**|`en-GB`| |**English (United States)**|`en-US`| |**Estonian (Estonia)**|`et-EE`| |**Filipino (Philippines)**|`fil-PH`| |**Finnish (Finland)**|`fi-FI`| |**French (Belgium)**|`fr-BE`| |**French (Canada)**|`fr-CA`| |**French (France)**|`fr-FR`| |**French (Switzerland)**|`fr-CH`| |**Galician (Spain)**|`gl-ES`| |**Georgian (Georgia)**|`ka-GE`| |**German (Austria)**|`de-AT`| |**German (Germany)**|`de-DE`| |**German (Switzerland)**|`de-CH`| |**Hebrew (Israel)**|`he-IL`| |**Hindi (India)**|`hi-IN`| |**Hungarian (Hungary)**|`hu-HU`| |**Icelandic (Iceland)**|`is-IS`| |**Indonesian (Indonesia)**|`id-ID`| |**Irish (Ireland)**|`ga-IE`| |**Italian (Italy)**|`it-IT`| |**Japanese (Japan)**|`ja-JP`| |**Javanese (Indonesia)**|`jv-ID`| |**Kazakh (Kazakhstan)**|`kk-KZ`| |**Khmer (Cambodia)**|`km-KH`| |**Korean (South Korea)**|`ko-KR`| |**Lao (Laos)**|`lo-LA`| |**Latvian (Latvia)**|`lv-LV`| |**Lithuanian (Lithuania)**|`lt-LT`| |**Macedonian (North Macedonia)**|`mk-MK`| |**Malay (Malaysia)**|`ms-MY`| |**Malayalam (India)**|`ml-IN`| |**Maltese (Malta)**|`mt-MT`| |**Mandarin Chinese (China)**|`cmn-CN`| |**Marathi (India)**|`mr-IN`| |**Mongolian (Mongolia)**|`mn-MN`| |**Nepali (Nepal)**|`ne-NP`| |**Norwegian Bokmål (Norway)**|`nb-NO`| |**Pashto (Afghanistan)**|`ps-AF`| |**Persian (Iran)**|`fa-IR`| |**Polish (Poland)**|`pl-PL`| |**Portuguese (Brazil)**|`pt-BR`| |**Portuguese (Portugal)**|`pt-PT`| |**Romanian (Romania)**|`ro-RO`| |**Russian (Russia)**|`ru-RU`| |**Serbian (Serbia)**|`sr-RS`| |**Sinhala (Sri Lanka)**|`si-LK`| |**Slovak (Slovakia)**|`sk-SK`| |**Slovenian (Slovenia)**|`sl-SI`| |**Somali (Somalia)**|`so-SO`| |**Spanish (Argentina)**|`es-AR`| |**Spanish (Bolivia)**|`es-BO`| |**Spanish (Chile)**|`es-CL`| |**Spanish (Colombia)**|`es-CO`| |**Spanish (Costa Rica)**|`es-CR`| |**Spanish (Cuba)**|`es-CU`| |**Spanish (Ecuador)**|`es-EC`| |**Spanish (El Salvador)**|`es-SV`| |**Spanish (Equatorial Guinea)**|`es-GQ`| |**Spanish (Guatemala)**|`es-GT`| |**Spanish (Mexico)**|`es-MX`| |**Spanish (Nicaragua)**|`es-NI`| |**Spanish (Panama)**|`es-PA`| |**Spanish (Paraguay)**|`es-PY`| |**Spanish (Puerto Rico)**|`es-PR`| |**Spanish (Spain)**|`es-ES`| |**Spanish (United States)**|`es-US`| |**Spanish (Uruguay)**|`es-UY`| |**Spanish (Venezuela)**|`es-VE`| |**Sundanese (Indonesia)**|`su-ID`| |**Swahili (Kenya)**|`sw-KE`| |**Swahili (Tanzania)**|`sw-TZ`| |**Swedish (Sweden)**|`sv-SE`| |**Tamil (India)**|`ta-IN`| |**Tamil (Malaysia)**|`ta-MY`| |**Tamil (Singapore)**|`ta-SG`| |**Telugu (India)**|`te-IN`| |**Thai (Thailand)**|`th-TH`| |**Turkish (Turkey)**|`tr-TR`| |**Ukrainian (Ukraine)**|`uk-UA`| |**Urdu (India)**|`ur-IN`| |**Urdu (Pakistan)**|`ur-PK`| |**Uzbek (United Kingdom)**|`uz-UK`| |**Vietnamese (Vietnam)**|`vi-VN`| |**Welsh (United Kingdom)**|`cy-GB`| |**Wu Chinese (China)**|`wuu-CN`| |**Xhosa (South Africa)**|`xh-ZA`| |**Zulu (South Africa)**|`zu-ZA`|  </details><details><summary>Supported Models</summary><details><summary>lovoai</summary>      |Name|Value| |----|-----| |**lovoai**|`af-ZA_Albertus Ruan`| ||`af-ZA_Danelle Wessel`| ||`am-ET_Abai Berhe`| ||`am-ET_Cherenet Tesfaye`| ||`ar-AE_Mansour Ahmed`| ||`ar-AE_Maryam Khan`| ||`ar-BH_Fatima Kumar`| ||`ar-BH_Omar Hassan`| ||`ar-DZ_Samia Touati`| ||`ar-DZ_Zuthimalin Brahimi`| ||`ar-EG_Ahmed Gamal`| ||`ar-EG_Reem Salah`| ||`ar-IQ_Aveen Majid`| ||`ar-IQ_Ismail Hashem`| ||`ar-JO_Fatima Jaber`| ||`ar-JO_Yousef Saleh`| ||`ar-KW_Areej Nair`| ||`ar-KW_Khaled Al Azmi`| ||`ar-LB_Abdel El Din`| ||`ar-LB_Eessa Kadifa`| ||`ar-LY_Abir Salem`| ||`ar-LY_Ahsan Omar`| ||`ar-MA_Hamid Bennani`| ||`ar-MA_Salma Naciri`| ||`ar-OM_Jabbar Singh`| ||`ar-OM_Zahra Sultan`| ||`ar-QA_Faizur Kumar`| ||`ar-QA_Noora Hussain`| ||`ar-SA_Majidah Khan`| ||`ar-SA_Omar Aziz`| ||`ar-SY_Oraida El-Assad`| ||`ar-SY_Rabah Ibrahim`| ||`ar-TN_Donia Cherif`| ||`ar-TN_Karim Dridi`| ||`ar-YE_Mansour Kasim`| ||`ar-YE_Mehdi Bawazeer`| ||`az-AZ_Ugur Quliyeva`| ||`az_AZ_Zeynab Cafarova`| ||`bg-BG_Damyan Ivanov`| ||`bg-BG_Fidanka Georgiev`| ||`bn-BD_Pranshu Akter`| ||`bn-BD_Vaagdevi Khatun`| ||`bn-IN_Gazi Mondal`| ||`bn-IN_Wali Ghosh`| ||`bs-BA_Esma Dodik`| ||`bs-BA_Ismet Rakic`| ||`ca-ES_Amada Fernando`| ||`ca-ES_Carmen Santiago`| ||`ca-ES_Miguel Torres`| ||`cs-CZ_Jana Rosicky`| ||`cs-CZ_Tomas Malecek`| ||`cy-GB_Branwen Jones`| ||`cy-GB_Elen Hughes`| ||`da-DK_Bjarne Jensen`| ||`da-DK_Helge Nielsen`| ||`de-AT_Lena Gruber`| ||`de-AT_Wilhelm Wagner`| ||`de-CH_Adolfus Meier`| ||`de-CH_Lara Keller`| ||`de-DE_Ada Weber`| ||`de-DE_Anna Schmidt`| ||`de-DE_Emma Muller`| ||`de-DE_Gerda Becker`| ||`de-DE_Hans Schulz`| ||`de-DE_Heidi Schneider`| ||`de-DE_Johanna Meyer`| ||`de-DE_Joshua Bauer`| ||`de-DE_Julian Koch`| ||`de-DE_Karl Hummels`| ||`de-DE_Maria Fischer`| ||`de-DE_Oliver Richter`| ||`de-DE_Otto Schaefer`| ||`de-DE_Petra Hoffman`| ||`de-DE_Walter Kimmich`| ||`el-GR_Petros Andino`| ||`el-GR_Thalia Klisiaris`| ||`en-AU_Amelia Taylor`| ||`en-AU_Charlotte Brown`| ||`en-AU_Darrell Robinson`| ||`en-AU_George Thompson`| ||`en-AU_Georgie Smith`| ||`en-AU_Isla Johnson`| ||`en-AU_Jake Nguyen`| ||`en-AU_Keegan Walker`| ||`en-AU_Kelly Opie`| ||`en-AU_Kevin Turner`| ||`en-AU_Mia White`| ||`en-AU_Nancy Jones`| ||`en-AU_Ryan Murphy`| ||`en-AU_Willow Martin`| ||`en-CA_Emily Salo`| ||`en-CA_Eric Fidyk`| ||`en-GB_Abigail Fraser`| ||`en-GB_Annie Smith`| ||`en-GB_Gertrude Baker`| ||`en-GB_Ian Kensington`| ||`en-GB_Kane Tooney`| ||`en-GB_Kelsey Michaels`| ||`en-GB_Kerrington Pacey`| ||`en-GB_Lizzy Wright`| ||`en-GB_Marcus O'Donell`| ||`en-GB_Nathaniel Jacobs`| ||`en-GB_Samuel Lee-Richards`| ||`en-GB_T.S. Cooper`| ||`en-GB_Theresa King`| ||`en-GB_William Tripp`| ||`en-HK_Heather Yiu`| ||`en-HK_Kevin Lau`| ||`en-IE_Aoife Byrne`| ||`en-IE_Bill Parkin`| ||`en-IN_Isha Singh`| ||`en-IN_Prabhdeep Patel`| ||`en-KE_Almasi Otieno`| ||`en-KE_Chitundu Mwangi`| ||`en-NG_Blessing Musa`| ||`en-NG_Kehinde Sade`| ||`en-NZ_Benson Duncan`| ||`en-NZ_Destiny Mitchell`| ||`en-PH_Angel dela Cruz`| ||`en-PH_Francis Reynaldo`| ||`en-SG_Chris Tan`| ||`en-SG_Rachel Ng`| ||`en-TZ_Busara Charles`| ||`en-TZ_Darweshi Juma`| ||`en-US_Alysha Imani`| ||`en-US_Betty Parker`| ||`en-US_Catherine Zania`| ||`en-US_Christopher Navarrez`| ||`en-US_Clara Ho`| ||`en-US_Eric Gonzalez`| ||`en-US_Heather Everett`| ||`en-US_Jamal Starke`| ||`en-US_Jasonna Johnson`| ||`en-US_Kaylee Montana`| ||`en-US_Ken hunter`| ||`en-US_Kim Howard`| ||`en-US_Kyle Moreno`| ||`en-US_Leroy Alshak`| ||`en-US_Micah Washington`| ||`en-US_Molly Richardson`| ||`en-US_Peter Lee`| ||`en-US_Phil Gough`| ||`en-US_Phoebe Nicholson`| ||`en-US_Samantha Hawthorne`| ||`en-US_Sean Orson`| ||`en-US_Serena Yang`| ||`en-US_Shannon Mechare`| ||`en-US_Thelma Browne`| ||`en-US_Tim Hardway`| ||`en-ZA_Cody Fergudson`| ||`en-ZA_Elna VanDijk`| ||`es-AR_Hyacinthe Castro`| ||`es-AR_Lautaro Gomez`| ||`es-BO_Elena Lopez`| ||`es-BO_Juan Perez`| ||`es-CL_Francisca Batistuta`| ||`es-CL_Gabriel Rodriguez`| ||`es-CO_Lorenzo Vazquez`| ||`es-CO_Sofia Garcia`| ||`es-CR_Guadalupe Suarez`| ||`es-CR_Sebastian Ramos`| ||`es-CU_Isabel Molina`| ||`es-CU_Luis Ortega`| ||`es-DO_Gabriela Serrano`| ||`es-DO_Raul Dominguez`| ||`es-EC_Angelina Romero`| ||`es-EC_Christian Diaz`| ||`es-EN_Carmen Martinela`| ||`es-ES_Andres Marin`| ||`es-ES_Emiliano Delgado`| ||`es-ES_Esmeralda Molina`| ||`es-ES_Hector Gavi`| ||`es-ES_Leo Gil`| ||`es-ES_Liliana Sanz`| ||`es-ES_Maria Ruiz`| ||`es-ES_Martin Enrique`| ||`es-ES_Miranda Navarro`| ||`es-ES_Pablo Iniesta`| ||`es-ES_Silvia Alvarez`| ||`es-ES_Teresa Iglesias`| ||`es-ES_Valentina Blanco`| ||`es-GQ_Elena Rubio`| ||`es-GQ_Teo Jimenez`| ||`es-GT_Ceciah Mendoza`| ||`es-GT_Paolo Ortiz`| ||`es-HN_Juana Flores`| ||`es-HN_Roberto Gutierrez`| ||`es-MX_Agata Albiol`| ||`es-MX_Darion Nunez`| ||`es-MX_Elias Lorenzo`| ||`es-MX_Elvira de Paul`| ||`es-MX_Enzo Paqueta`| ||`es-MX_Ezequiel Pacheco`| ||`es-MX_Iago Domingo`| ||`es-MX_Irene Vasquez`| ||`es-MX_Julieta Aguilar`| ||`es-MX_Lia Medina`| ||`es-MX_Nil Alvarez`| ||`es-MX_Pedro Rojas`| ||`es-MX_Rosa Valdoza`| ||`es-MX_Valencia Alba`| ||`es-MX_Veronica Mairal`| ||`es-NI_Abril Santacruz`| ||`es-NI_Lorenzo Llorente`| ||`es-PA_Liberto Marcos`| ||`es-PA_Yolanda Ezequiel`| ||`es-PE_Margarita de Fuentes`| ||`es-PE_Rey Sancho`| ||`es-PR_Alex de Santos`| ||`es-PR_Carlota Almiron`| ||`es-PY_Karina Diego`| ||`es-PY_Victor Mariela`| ||`es-SV_Jacinta Vela`| ||`es-SV_Marina Llorente`| ||`es-US_Jodrigo Alonso`| ||`es-US_Laia Paloma`| ||`es-US_Sergio Morata`| ||`es-UY_Lia Valentina`| ||`es-UY_Luis Ramon`| ||`es-VE_Manuel Rojos`| ||`es-VE_Sofia Vargas`| ||`et-EE_Barba Sepp`| ||`et-EE_Eduk Tamm`| ||`eu-ES_Markel Zubiri`| ||`eu-ES_Nahia Texpare`| ||`fa-IR_Bizhan Gilgamesh`| ||`fa-IR_Yasmina Hakimi`| ||`fi-FI_Anneli Niemnien`| ||`fi-FI_Kristiina Koskinen`| ||`fi-FI_Tapanni Korhonen`| ||`fil-PH_Amihan Reyes`| ||`fil-PH_Dennis de Saul`| ||`fr-BE_Louis Maes`| ||`fr-BE_Noah Peeters`| ||`fr-CA_Cherise DuPont`| ||`fr-CA_Olivier Varane`| ||`fr-CA_Raphael Jacques`| ||`fr-CH_Luca Dalot`| ||`fr-CH_Sylvie Gallace`| ||`fr-FR_Alain Hamel`| ||`fr-FR_Albertine Dubois`| ||`fr-FR_Antoine Petit`| ||`fr-FR_Brigitte Richard`| ||`fr-FR_Celeste Lefevre`| ||`fr-FR_Celine Bundchen`| ||`fr-FR_Damian Trezeguet`| ||`fr-FR_Diogo Pavard`| ||`fr-FR_Francoise LaFont`| ||`fr-FR_Gisele Guerin`| ||`fr-FR_Hugo Duval`| ||`fr-FR_Jacqueline Simon`| ||`fr-FR_Lois Allaire`| ||`fr-FR_Theo Bernard`| ||`ga-IE_Anja O'Brien`| ||`ga-IE_Liam Murphy`| ||`gl-ES_Clara Campos`| ||`gl-ES_Nicolas Montoya`| ||`gu-IN_Arzoo Chowdhury`| ||`gu-IN_Pramukh Barot`| ||`he-IL_Avi Goldmann`| ||`he-IL_Yael Haddad`| ||`hi-IN_Ashwin Nikhil`| ||`hi-IN_Uma Aravind`| ||`hr-HR_Krasna Perisic`| ||`hr-HR_Luka Horvat`| ||`hu-HU_Endre Szabo`| ||`hu-HU_Zoe Nagy`| ||`hy-AM_Arpi Hovhannisyan`| ||`hy-AM_Gor Grigoryan`| ||`id-ID_Bagaskoro Ulunjandi`| ||`id-ID_Diah Sukatendel`| ||`is-IS_Fridrika Sigurdsson`| ||`is-IS_Olafur Jonsdottir`| ||`it-IT_Alessandro Ferrari`| ||`it-IT_Alessia Ricci`| ||`it-IT_Allegra Greco`| ||`it-IT_Angelo Bianchi`| ||`it-IT_Antonio Colombo`| ||`it-IT_Eva De Luca`| ||`it-IT_Filomena Mancini`| ||`it-IT_Francesco Rossi`| ||`it-IT_Gaia Marino`| ||`it-IT_Gemma Conti`| ||`it-IT_Gianluigi Russo`| ||`it-IT_Greta Bruno`| ||`it-IT_Marco Romano`| ||`it-IT_Paul Esposito`| ||`it-IT_Serafina Gallo`| ||`ja-JP_Ayaka Musashi`| ||`ja-JP_Hiromi Tanaka`| ||`ja-JP_Hiroshi Maeda`| ||`ja-JP_Ichiro Sayaka`| ||`ja-JP_Naomi Sora`| ||`ja-JP_Sartoshi Juno`| ||`ja-JP_Sayuri Watanabe`| ||`jv-ID_Anom Zees`| ||`jv-ID_Bratawati Pulukadang`| ||`ka-GE_Ava Lomidze`| ||`ka-GE_Elijah Maisuradze`| ||`kk-KZ_Nurislam Omarov`| ||`kk-KZ_Rayana Kenes`| ||`km-KH_Chanthou Sok`| ||`km-KH_Kaliyanei Chea`| ||`kn-IN_Aadesh Madar`| ||`kn-IN_Rhyah Nayka`| ||`ko-KR_Eunjin Bae`| ||`ko-KR_Heechul Kim`| ||`ko-KR_Isu Choi`| ||`ko-KR_Jisoo Han`| ||`ko-KR_Meesun Kang`| ||`ko-KR_Minjoon Lee`| ||`ko-KR_Seung Hee Hwang`| ||`ko-KR_Yoosung Park`| ||`lo-LA_Lawan Vang`| ||`lo-LA_Sengphet Inthavong`| ||`lt-LT_Nojus Antanas`| ||`lt-LT_Ruta Bagdonas`| ||`lv-LV_Mozus Berzina`| ||`lv-LV_Santa Ozola`| ||`mk-MK_Berislav Stojanovski`| ||`mk-MK_Smaragda Jovanovska`| ||`ml-IN_Abha Nair`| ||`ml-IN_Akhil Kumar`| ||`mn-MN_Altan Batbayar`| ||`mn-MN_Enkhjargal Ganbold`| ||`mr-IN_Mihir Chitre`| ||`mr-IN_Vedvika Deo`| ||`ms-MY_Nur Tengku`| ||`ms-MY_Zikri Wan`| ||`mt-MT_Lola Farrugia`| ||`mt-MT_Milo Borg`| ||`my-MM_Dedan Khin`| ||`my-MM_Eindra Aung`| ||`nb-NO_Henrik Larsen`| ||`nb-NO_Vilde Hansen`| ||`nb_NO_Malin Pedersen`| ||`ne-NP_Batsal Khadka`| ||`ne-NP_Druhi Mahat`| ||`nl-BE_Arthur Mertens`| ||`nl-BE_Martine Claes`| ||`nl-NL_Adriana De Vries`| ||`nl-NL_Helena De Jong`| ||`nl-NL_Jan Visser`| ||`pl-PL_Ewa Grabowski`| ||`pl-PL_Piotr Duda`| ||`pl-PL_Zuzanna Kackz`| ||`ps-AF_Abdul-Alim Sayyid`| ||`ps-AF_Zahra Qurban`| ||`pt-BR_Adriana Rocha`| ||`pt-BR_Ana Bahiense`| ||`pt-BR_Anabella Teixeira`| ||`pt-BR_Antonia Macedo`| ||`pt-BR_Antonio Barros`| ||`pt-BR_Fernanda Pedreira`| ||`pt-BR_Francisco Guimaraes`| ||`pt-BR_Joao Azevedo`| ||`pt-BR_Jose Almeida`| ||`pt-BR_Juliana Costa`| ||`pt-BR_Marcia Ribeiro`| ||`pt-BR_Maria Cardoso`| ||`pt-BR_Paulo Correia`| ||`pt-BR_Pedro Magalhaes`| ||`pt-BR_Roberto Braga`| ||`pt-PT_Benedita Motta`| ||`pt-PT_Renato Matos`| ||`pt-PT_Rita Oliveira`| ||`ro-RO_Cristian Ionescu`| ||`ro-RO_Mirabela Gheata`| ||`ru-RU_Galina Ivanov`| ||`ru-RU_Nadezhda Smirnoff`| ||`ru-RU_Pyotr Semenov`| ||`si-LK_Kasun Perera`| ||`si-LK_Saanvi de Silva`| ||`sk-SK_Havel Varga`| ||`sk-SK_Olga Kovac`| ||`sl-SI_Neza Mlakar`| ||`sl-SI_Nik Krajnc`| ||`so-SO_Axado Ibrahim`| ||`so-SO_Taifa Mohamed`| ||`sq-AL_Bora Marku`| ||`sq-AL_Dren Kedare`| ||`sr-RS_Lara Markovic`| ||`sr-RS_Vlado Popovic`| ||`su-ID_Aarifa Bol`| ||`su-ID_Mustafa Deng`| ||`sv-SE_Agnes Lidstrom`| ||`sv-SE_Nicklas Forsberg`| ||`sv-SE_Wilma Sundin`| ||`sw-KE_Akeyo Njoroge`| ||`sw-KE_Chege Odhiambo`| ||`sw-TZ_Binti Ramadhani`| ||`sw-TZ_Darweshi Ally`| ||`ta-IN_Ashwin Kumar`| ||`ta-IN_Nila Suresh`| ||`ta-LK_Adya Pillai`| ||`ta-LK_Prahan Aachari`| ||`ta-MY_Aahna Konar`| ||`ta-MY_Kethan Nadar`| ||`ta-SG_Abilasha Naicker`| ||`ta-SG_Nemi Udayar`| ||`te-IN_Aarkash Reddy`| ||`te-IN_Tanvi Sharma`| ||`th-TH_Buppha Prasit`| ||`th-TH_Kanchana Sangthong`| ||`th-TH_Somchai Thongkham`| ||`tr-TR_Emre Ozdemir`| ||`tr-TR_Nehir Celik`| ||`uk-UA_Artem Shevchenko`| ||`uk-UA_Daryna Kovalenko`| ||`ur-IN_Farah Abbasi`| ||`ur-IN_Sharyar Alvi`| ||`ur-PK_Hamza Farooqi`| ||`ur-PK_Sana Dhanial`| ||`uz-UK_Javlonbek Yusupov`| ||`uz-UZ_Rustam Karimova`| ||`vi-VN_Huu Duong`| ||`vi-VN_Vi Ly`| ||`wuu-CN_Muchen Li`| ||`wuu-CN_Ruoxi Wang`| ||`yue-CN_Ah-lam Lei`| ||`yue-CN_Xiaoxiao Wong`| ||`zh-CN-henan_Genji Zhou`| ||`zh-CN-liaoning_Chu Zhang`| ||`zh-CN-shaanxi_Chunhua Lin`| ||`zh-CN-shandong_Jiayi Wu`| ||`zh-CN-sichuan_Juan Yang`| ||`zh-CN_An Liu`| ||`zh-CN_Bai Yang`| ||`zh-CN_Bao Huang`| ||`zh-CN_Chao Zhou`| ||`zh-CN_Chen Chen Huo`| ||`zh-CN_Cheng Sun`| ||`zh-CN_Chichi Wu`| ||`zh-CN_Chin Ma`| ||`zh-CN_Chun Hu`| ||`zh-CN_Cong Zhang`| ||`zh-CN_Da Xia Li`| ||`zh-CN_Daiyu Zhu`| ||`zh-CN_Diu Wang`| ||`zh-CN_Huan Luo`| ||`zh-CN_Huifen Chen`| ||`zh-CN_Huiqing Wang`| ||`zh-CN_Meng Li`| ||`zh-CN_Xuan Xu`| ||`zh-CN_Yifu Wu`| ||`zh-CN_Yihan Chen`| ||`zh-CN_Yinuo Zhang`| ||`zh-HK_Kun Lo`| ||`zh-HK_Lanying Lei`| ||`zh-HK_Lee Lam`| ||`zh-TW_Mingxia Luo`| ||`zh-TW_Mingzhu Gao`| ||`zh-TW_Susu Song`| ||`zu-ZA_Bonginkosi Masina`| ||`zu-ZA_Ulwazi Mangede`|  </details><details><summary>amazon</summary>      |Name|Value| |----|-----| |**amazon**|`ar-AE_Hala_Neural`| ||`arb_Zeina_Standard`| ||`ca-ES_Arlet_Neural`| ||`cmn-CN_Zhiyu_Neural`| ||`cmn-CN_Zhiyu_Standard`| ||`cy-GB_Gwyneth_Standard`| ||`da-DK_Mads_Standard`| ||`da-DK_Naja_Standard`| ||`de-AT_Hannah_Neural`| ||`de-DE_Daniel_Neural`| ||`de-DE_Hans_Standard`| ||`de-DE_Marlene_Standard`| ||`de-DE_Vicki_Neural`| ||`de-DE_Vicki_Standard`| ||`en-AU_Nicole_Neural`| ||`en-AU_Olivia_Standard`| ||`en-AU_Russell_Neural`| ||`en-GB_Amy_Neural`| ||`en-GB_Amy_Standard`| ||`en-GB_Arthur_Neural`| ||`en-GB_Brian_Neural`| ||`en-GB_Brian_Standard`| ||`en-GB_Emma_Neural`| ||`en-GB_Emma_Standard`| ||`en-IN_Aditi_Standard`| ||`en-IN_Kajal_Neural`| ||`en-IN_Raveena_Standard`| ||`en-NZ_Aria_Neural`| ||`en-US_Ivy_Neural`| ||`en-US_Ivy_Standard`| ||`en-US_Joanna_Neural`| ||`en-US_Joanna_Standard`| ||`en-US_Joey_Neural`| ||`en-US_Joey_Standard`| ||`en-US_Justin_Neural`| ||`en-US_Justin_Standard`| ||`en-US_Kendra_Neural`| ||`en-US_Kendra_Standard`| ||`en-US_Kevin_Neural`| ||`en-US_Kimberly_Neural`| ||`en-US_Kimberly_Standard`| ||`en-US_Matthew_Neural`| ||`en-US_Matthew_Standard`| ||`en-US_Ruth_Neural`| ||`en-US_Salli_Neural`| ||`en-US_Salli_Standard`| ||`en-US_Stephen_Neural`| ||`en-ZA_Ayanda_Neural`| ||`es-ES_Conchita_Standard`| ||`es-ES_Enrique_Standard`| ||`es-ES_Lucia_Neural`| ||`es-ES_Lucia_Standard`| ||`es-ES_Sergio_Neural`| ||`es-MX_Andres_Neural`| ||`es-MX_Mia_Neural`| ||`es-MX_Mia_Standard`| ||`es-US_Lupe_Neural`| ||`es-US_Lupe_Standard`| ||`es-US_Miguel_Standard`| ||`es-US_Pedro_Neural`| ||`es-US_Penelope_Standard`| ||`fi-FI_Suvi_Neural`| ||`fr-CA_Chantal_Standard`| ||`fr-CA_Gabrielle_Neural`| ||`fr-CA_Liam_Neural`| ||`fr-FR_Celine_Standard`| ||`fr-FR_Lea_Neural`| ||`fr-FR_Lea_Standard`| ||`fr-FR_Mathieu_Standard`| ||`fr-FR_Remi_Neural`| ||`hi-IN_Aditi_Standard`| ||`hi-IN_Kajal_Neural`| ||`is-IS_Dora_Standard`| ||`is-IS_Karl_Neural`| ||`is-IS_Karl_Standard`| ||`it-IT_Adriano_Neural`| ||`it-IT_Bianca_Neural`| ||`it-IT_Bianca_Standard`| ||`it-IT_Carla_Standard`| ||`it-IT_Giorgio_Standard`| ||`ja-JP_Kazuha_Neural`| ||`ja-JP_Mizuki_Standard`| ||`ja-JP_Takumi_Neural`| ||`ja-JP_Takumi_Standard`| ||`ja-JP_Tomoko_Neural`| ||`ko-KR_Seoyeon_Neural`| ||`ko-KR_Seoyeon_Standard`| ||`nb-NO_Liv_Standard`| ||`nl-NL_Laura_Neural`| ||`nl-NL_Lotte_Standard`| ||`nl-NL_Ruben_Standard`| ||`pl-PL_Ewa_Standard`| ||`pl-PL_Jacek_Standard`| ||`pl-PL_Jan_Standard`| ||`pl-PL_Maja_Standard`| ||`pl-PL_Ola_Neural`| ||`pt-BR_Camila_Neural`| ||`pt-BR_Camila_Standard`| ||`pt-BR_Ricardo_Standard`| ||`pt-BR_Thiago_Neural`| ||`pt-BR_Vitoria_Neural`| ||`pt-BR_Vitoria_Standard`| ||`pt-PT_Cristiano_Standard`| ||`pt-PT_Ines_Neural`| ||`pt-PT_Ines_Standard`| ||`ro-RO_Carmen_Standard`| ||`ru-RU_Maxim_Standard`| ||`ru-RU_Tatyana_Standard`| ||`sv-SE_Astrid_Standard`| ||`sv-SE_Elin_Neural`| ||`tr-TR_Filiz_Standard`| ||`yue-CN_Hiujin_Neural`|  </details>  </details>

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.launch_async_job_response import LaunchAsyncJobResponse
from openapi_client.models.text_to_speech_async_request_option import TextToSpeechAsyncRequestOption
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TextToSpeechAsyncApi(api_client)
    providers = 'providers_example' # str | It can be one (ex: **'amazon'** or **'google'**) or multiple provider(s) (ex: **'amazon,microsoft,google'**)             that the data will be redirected to in order to get the processed results.
    text = 'text_example' # str | Text to analyze
    fallback_providers = 'fallback_providers_example' # str | Providers in this list will be used as fallback if the call to provider in `providers` parameter fails.     To use this feature, you must input **only one** provider in the `providers` parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn't fail.   *Doesn't work with async subfeatures.*      (optional)
    show_original_response = False # bool | Optional : Shows the original response of the provider.<br>         When set to **true**, a new attribute *original_response* will appear in the response object. (optional) (default to False)
    webhook_receiver = 'webhook_receiver_example' # str | Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. (optional)
    users_webhook_parameters = None # Dict[str, object] | Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client's data ID to link the result internally).             Will only be used when webhook_receiver is set. (optional)
    settings = 'settings_example' # str | A dictionnary or a json object to specify specific models to use for some providers. <br>                     It can be in the following format: {\\\"google\\\" : \\\"google_model\\\", \\\"ibm\\\": \\\"ibm_model\\\"...}.                      **Caution**: setting models can be done only with `Content-Type` : `application/json`.                       (optional)
    language = '' # str | Language code expected (ex: en, fr) (optional) (default to '')
    option = openapi_client.TextToSpeechAsyncRequestOption() # TextToSpeechAsyncRequestOption |  (optional)
    rate = 0 # int | Increase or decrease the speaking rate by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) (optional) (default to 0)
    pitch = 0 # int | Increase or decrease the speaking pitch by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) (optional) (default to 0)
    volume = 0 # int | Increase or decrease the audio volume by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) (optional) (default to 0)
    audio_format = '' # str | Optional parameter to specify the audio format in which the audio will be generated. By default,             audios are encoded in MP3, except for lovoai which use the wav container. (optional) (default to '')
    sampling_rate = 0 # int | Optional. The synthesis sample rate (in hertz) for this audio. When this is specified, the audio will be converted             either to the right passed value, or to a the nearest value acceptable by the provider (optional) (default to 0)

    try:
        # Text to Speech launch job
        api_response = api_instance.audio_audio_text_to_speech_async_create(providers, text, fallback_providers=fallback_providers, show_original_response=show_original_response, webhook_receiver=webhook_receiver, users_webhook_parameters=users_webhook_parameters, settings=settings, language=language, option=option, rate=rate, pitch=pitch, volume=volume, audio_format=audio_format, sampling_rate=sampling_rate)
        print("The response of TextToSpeechAsyncApi->audio_audio_text_to_speech_async_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextToSpeechAsyncApi->audio_audio_text_to_speech_async_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers** | **str**| It can be one (ex: **&#39;amazon&#39;** or **&#39;google&#39;**) or multiple provider(s) (ex: **&#39;amazon,microsoft,google&#39;**)             that the data will be redirected to in order to get the processed results. | 
 **text** | **str**| Text to analyze | 
 **fallback_providers** | **str**| Providers in this list will be used as fallback if the call to provider in &#x60;providers&#x60; parameter fails.     To use this feature, you must input **only one** provider in the &#x60;providers&#x60; parameter. but you can put up to 5 fallbacks.  They will be tried in the same order they are input, and it will stop to the first provider who doesn&#39;t fail.   *Doesn&#39;t work with async subfeatures.*      | [optional] 
 **show_original_response** | **bool**| Optional : Shows the original response of the provider.&lt;br&gt;         When set to **true**, a new attribute *original_response* will appear in the response object. | [optional] [default to False]
 **webhook_receiver** | **str**| Webhook receiver should be a valid https URL (ex : https://your.listner.com/endpoint).             After the processing is done, the webhook endpoint will receive a POST request with the result. | [optional] 
 **users_webhook_parameters** | [**Dict[str, object]**](Dict.md)| Json data that contains of additional parameters that will be sent back to the webhook receiver             (ex: api key for security or client&#39;s data ID to link the result internally).             Will only be used when webhook_receiver is set. | [optional] 
 **settings** | **str**| A dictionnary or a json object to specify specific models to use for some providers. &lt;br&gt;                     It can be in the following format: {\\\&quot;google\\\&quot; : \\\&quot;google_model\\\&quot;, \\\&quot;ibm\\\&quot;: \\\&quot;ibm_model\\\&quot;...}.                      **Caution**: setting models can be done only with &#x60;Content-Type&#x60; : &#x60;application/json&#x60;.                       | [optional] 
 **language** | **str**| Language code expected (ex: en, fr) | [optional] [default to &#39;&#39;]
 **option** | [**TextToSpeechAsyncRequestOption**](TextToSpeechAsyncRequestOption.md)|  | [optional] 
 **rate** | **int**| Increase or decrease the speaking rate by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) | [optional] [default to 0]
 **pitch** | **int**| Increase or decrease the speaking pitch by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) | [optional] [default to 0]
 **volume** | **int**| Increase or decrease the audio volume by expressing a positif or negatif number ranging between             100 and -100 (a relative value as percentage varying from -100% to 100%) | [optional] [default to 0]
 **audio_format** | **str**| Optional parameter to specify the audio format in which the audio will be generated. By default,             audios are encoded in MP3, except for lovoai which use the wav container. | [optional] [default to &#39;&#39;]
 **sampling_rate** | **int**| Optional. The synthesis sample rate (in hertz) for this audio. When this is specified, the audio will be converted             either to the right passed value, or to a the nearest value acceptable by the provider | [optional] [default to 0]

### Return type

[**LaunchAsyncJobResponse**](LaunchAsyncJobResponse.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_audio_text_to_speech_async_destroy**
> audio_audio_text_to_speech_async_destroy()

Text To Speech delete Jobs

Generic class to handle method GET all async job for user  Attributes:     feature (str): EdenAI feature     subfeature (str): EdenAI subfeature

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TextToSpeechAsyncApi(api_client)

    try:
        # Text To Speech delete Jobs
        api_instance.audio_audio_text_to_speech_async_destroy()
    except Exception as e:
        print("Exception when calling TextToSpeechAsyncApi->audio_audio_text_to_speech_async_destroy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_audio_text_to_speech_async_retrieve**
> ListAsyncJobResponse audio_audio_text_to_speech_async_retrieve()

Text To Speech list jobs

Get a list of all jobs launched for this feature. You'll then be able to use the ID of each one to get its status and results.<br>                         Please note that a **job status doesn't get updated until a get request** is sent.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.list_async_job_response import ListAsyncJobResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TextToSpeechAsyncApi(api_client)

    try:
        # Text To Speech list jobs
        api_response = api_instance.audio_audio_text_to_speech_async_retrieve()
        print("The response of TextToSpeechAsyncApi->audio_audio_text_to_speech_async_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextToSpeechAsyncApi->audio_audio_text_to_speech_async_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListAsyncJobResponse**](ListAsyncJobResponse.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **audio_audio_text_to_speech_async_retrieve2**
> AsyncaudiotextToSpeechAsyncResponseModel audio_audio_text_to_speech_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)

Text To Speech Get Job Results

Get the status and results of an async job given its ID.

### Example

* Bearer (JWT) Authentication (FeatureApiAuth):

```python
import openapi_client
from openapi_client.models.asyncaudiotext_to_speech_async_response_model import AsyncaudiotextToSpeechAsyncResponseModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.edenai.run/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.edenai.run/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): FeatureApiAuth
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.TextToSpeechAsyncApi(api_client)
    public_id = 'public_id_example' # str | 
    response_as_dict = True # bool |  (optional) (default to True)
    show_original_response = False # bool |  (optional) (default to False)

    try:
        # Text To Speech Get Job Results
        api_response = api_instance.audio_audio_text_to_speech_async_retrieve2(public_id, response_as_dict=response_as_dict, show_original_response=show_original_response)
        print("The response of TextToSpeechAsyncApi->audio_audio_text_to_speech_async_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextToSpeechAsyncApi->audio_audio_text_to_speech_async_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_id** | **str**|  | 
 **response_as_dict** | **bool**|  | [optional] [default to True]
 **show_original_response** | **bool**|  | [optional] [default to False]

### Return type

[**AsyncaudiotextToSpeechAsyncResponseModel**](AsyncaudiotextToSpeechAsyncResponseModel.md)

### Authorization

[FeatureApiAuth](../README.md#FeatureApiAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**500** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


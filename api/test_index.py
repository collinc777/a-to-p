import os
import pytest
from index import generate_audio, Transcript, TranscriptLine


# @pytest.mark.asyncio
# async def test_do_tts():
#     result = await do_tts(line="hello world", voice="Amy")
#     assert result is not None


@pytest.mark.asyncio
async def test_generate_audio():
    transcript = Transcript(
        transcript_lines=[
            TranscriptLine(text="hello world", speaker="narrator"),
            TranscriptLine(text="right back at ya", speaker="allison"),
        ]
    )
    result = await generate_audio(transcript)
    assert result is not None
    # assert file audio.mp3 exists
    assert os.path.exists("audio.mp3")


# @pytest.mark.asyncio
# async def test_do_tts_v2():
#     from index import do_tts_v2

#     result = await do_tts_v2(line="hello world", voice="Amy")
#     assert result is not None


# @pytest.mark.asyncio
# async def test_openai_tts():
#     from index import do_tts_openai

#     result = await do_tts_openai(line="hello world", voice="Amy")
#     assert result is not None

import os
import pytest
from index import do_tts, generate_audio, Transcript, TranscriptLine


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

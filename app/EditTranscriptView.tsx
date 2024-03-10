import { useState } from "react";
import { updateEpisode } from "./actions";
import { ResultOf } from "gql.tada";
import { EpisodeFragment, TranscriptFragment } from "./queries";
import { EditEpisodeActionBar } from "./episode/[id]/EditEpisodeActionBar";
import { EditableTranscriptLine } from "./EditableTranscriptLine";

export function EditTranscriptView({
  episode,
  transcript,
}: {
  episode: ResultOf<typeof EpisodeFragment>;
  transcript: ResultOf<typeof TranscriptFragment>;
}) {
  const episodeId = episode.id;
  const [trascriptCopy, setTranscriptCopy] = useState(transcript);
  const addLineBefore = async (idx: number) => {
    const newTranscriptLines = trascriptCopy.transcriptLines.slice();
    newTranscriptLines.splice(idx, 0, {
      speaker: "Jake",
      text: "New Line",
    });
    const newTrancript = {
      ...trascriptCopy,
      transcriptLines: newTranscriptLines,
    };
    console.log({ newTrancript });
    setTranscriptCopy(newTrancript);
    await updateEpisode({
      id: episodeId,
      input: {
        transcript: newTrancript,
      },
    });
  };
  const addLineAfter = async (idx: number) => {
    const newTranscriptLines = trascriptCopy.transcriptLines.slice();
    newTranscriptLines.splice(idx + 1, 0, {
      speaker: "Jake",
      text: "New Line",
    });
    const newTrancript = {
      ...trascriptCopy,
      transcriptLines: newTranscriptLines,
    };
    console.log({ newTrancript });
    setTranscriptCopy(newTrancript);
    await updateEpisode({
      id: episodeId,
      input: {
        transcript: newTrancript,
      },
    });
  };
  const removeLine = async (idx: number) => {
    const newTranscriptLines = trascriptCopy.transcriptLines.filter(
      (line, i) => i !== idx
    );
    const newTrancript = {
      ...trascriptCopy,
      transcriptLines: newTranscriptLines,
    };
    console.log({ newTrancript });
    setTranscriptCopy(newTrancript);
    await updateEpisode({
      id: episodeId,
      input: {
        transcript: newTrancript,
      },
    });
  };
  const updateLine = async (idx: number, newText: string) => {
    const newTranscriptLines = trascriptCopy.transcriptLines.map((line, i) => {
      if (i === idx) {
        return { speaker: line.speaker, text: newText };
      }
      return line;
    });
    const newTrancript = {
      ...trascriptCopy,
      transcriptLines: newTranscriptLines,
    };
    console.log({ newTrancript });
    setTranscriptCopy(newTrancript);
    await updateEpisode({
      id: episodeId,
      input: {
        transcript: newTrancript,
      },
    });
  };
  return (
    <div className="space-y-3">
      <EditEpisodeActionBar
        episode={episode}
        editableTranscriptCopy={trascriptCopy}
      />
      {trascriptCopy.transcriptLines.map((line, idx) => {
        return (
          <EditableTranscriptLine
            key={idx}
            idx={idx}
            line={line}
            handleUpdate={updateLine}
            handleAddLineAfter={addLineAfter}
            handleRemoveLine={removeLine}
            handleAddLineBefore={addLineBefore}
          />
        );
      })}
    </div>
  );
}

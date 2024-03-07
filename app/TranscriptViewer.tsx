import { Key, useCallback, useEffect, useRef, useState } from "react";
import { CheckCheckIcon, CheckIcon, FilePenLine, Trash } from "lucide-react";
import { updateEpisode } from "./actions";
import debounce from "lodash.debounce";
import { FragmentOf, ResultOf, readFragment } from "gql.tada";
import { TranscriptFragment, TranscriptLineFragment } from "./queries";
import { Button } from "@/components/ui/button";
import Result from "postcss/lib/result";

export default function TranscriptViewer({
  transcript: transcript,
}: {
  episodeId: string;
  transcript: FragmentOf<typeof TranscriptFragment>;
  episodeStatus: string;
}) {
  const transcriptLines = transcript.transcriptLines;
  return (
    <div className="space-y-3">
      {transcriptLines?.map((line, idx) => {
        return <TranscriptLine key={idx} idx={idx} line={line} />;
      })}
    </div>
  );
}

export const SpeakerBadge = ({ speaker }: { speaker: string }) => {
  const className = () => {
    if (speaker === "Jake") {
      return "w-12 rounded-md bg-yellow-50 px-2 py-1 text-xs font-medium text-yellow-800 ring-1 ring-inset ring-yellow-600/20";
    } else {
      return "w-12 rounded-md bg-purple-50 px-2 py-1 text-xs font-medium text-purple-700 ring-1 ring-inset ring-purple-700/10";
    }
  };
  return <span className={className()}>{speaker}</span>;
};
function TranscriptLine({
  line,
  idx,
}: {
  line: any;
  idx: Key | null | undefined;
}) {
  const speaker = line.speaker;
  return (
    <div className="flex space-x-3" key={idx}>
      <SpeakerBadge speaker={speaker} />
      <p>{line.text}</p>
    </div>
  );
}

export function EditTranscriptView({
  episodeId,
  transcript,
}: {
  episodeId: string;
  transcript: ResultOf<typeof TranscriptFragment>;
}) {
  const [trascriptCopy, setTranscriptCopy] = useState(transcript);
  const updateLine = async (idx: Key, newText: string) => {
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
      {trascriptCopy.transcriptLines.map((line, idx) => {
        return (
          <EditableTranscriptLine
            key={idx}
            idx={idx}
            line={line}
            handleInput={updateLine}
          />
        );
      })}
    </div>
  );
}

function EditableTranscriptLine({
  line,
  idx,
  handleInput,
}: {
  line: ResultOf<typeof TranscriptLineFragment>;
  idx: Key;
  handleInput: (idx: Key, newText: string) => Promise<void>;
}) {
  const [isEditing, setIsEditing] = useState(false);
  const ref = useRef<HTMLParagraphElement>(null);

  return (
    <div className="flex space-x-3" key={idx}>
      <SpeakerBadge speaker={line.speaker} />
      <>
        <p ref={ref} className="grow" contentEditable={isEditing}>
          {line.text}
        </p>
        {!isEditing ? (
          <Button
            variant={"ghost"}
            onClick={() => {
              setIsEditing(true);
            }}
          >
            <FilePenLine />
          </Button>
        ) : (
          <Button
            variant={"success"}
            onClick={() => {
              setIsEditing(false);
              console.log(ref.current?.innerText);
              const newText = ref.current?.innerText;
              if (newText) {
                handleInput(idx, newText);
              }
            }}
          >
            <CheckIcon />
          </Button>
        )}
        <Button variant={"destructive"}>
          <Trash />
        </Button>
      </>
    </div>
  );
}

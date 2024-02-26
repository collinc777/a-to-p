import { Key, useCallback, useRef, useState } from "react";
import { CheckCheckIcon, CheckIcon, FilePenLine, Trash } from "lucide-react";
import { updateEpisode } from "./actions";
import debounce from "lodash.debounce";
import { FragmentOf, readFragment } from "gql.tada";
import { TranscriptFragment } from "./queries";
import { Button } from "@/components/ui/button";

export default function TranscriptViewer({
  episodeId,
  transcriptFrag,
  episodeStatus,
}: {
  episodeId: string;
  transcriptFrag: FragmentOf<typeof TranscriptFragment>;
  episodeStatus: string;
}) {
  const transcript = readFragment(TranscriptFragment, transcriptFrag);
  const transcriptLines = transcript.transcriptLines;
  const debouncedUpdateEpisode = useCallback(
    debounce((episodeId, newTranscriptLines) => {
      updateEpisode({
        id: episodeId,
        input: {
          transcript: {
            transcriptLines: newTranscriptLines.map((line: any) => ({
              speaker: line.speaker,
              text: line.text,
            })),
          },
        },
      });
    }, 500), // delay in ms
    []
  );

  const handleInput = (idx: number) => async (e: any) => {
    const newText = e.target.innerText;
    const newTranscriptLines = transcriptLines?.map((line, i) => {
      if (i === idx) {
        return { speaker: line.speaker, text: newText };
      }
      return line;
    });
    debouncedUpdateEpisode(episodeId, newTranscriptLines);
  };
  return (
    <div className="space-y-3">
      {transcriptLines?.map((line, idx) => {
        return (
          <TranscriptLine
            key={idx}
            idx={idx}
            episodeStatus={episodeStatus}
            line={line}
            handleInput={handleInput(idx)}
          />
        );
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
  episodeStatus,
  handleInput,
}: {
  line: any;
  idx: Key | null | undefined;
  handleInput: (e: any) => Promise<void>;
  episodeStatus: string;
}) {
  const speaker = line.speaker;
  const text = line.text;
  const [isEditing, setIsEditing] = useState(false);
  return (
    <div className="flex space-x-3" key={idx}>
      <SpeakerBadge speaker={speaker} />
      {episodeStatus === "done" ? (
        <>
          <p className="grow" contentEditable={isEditing}>
            {text}
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
            <Button variant={"success"} onClick={() => setIsEditing(false)}>
              <CheckIcon />
            </Button>
          )}
          <Button variant={"destructive"}>
            <Trash />
          </Button>
        </>
      ) : (
        <p>{text}</p>
      )}
    </div>
  );
}

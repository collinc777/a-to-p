import { useRef, useState } from "react";
import { CheckIcon, FilePenLine, Trash } from "lucide-react";
import { updateEpisode } from "./actions";
import { FragmentOf, ResultOf } from "gql.tada";
import { TranscriptFragment, TranscriptLineFragment } from "./queries";
import { Button } from "@/components/ui/button";
import { Dialog } from "@radix-ui/react-dialog";
import {
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";

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
  idx: number | null | undefined;
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

function EditableTranscriptLine({
  line,
  idx,
  handleUpdate,
  handleRemoveLine,
  handleAddLineAfter,
  handleAddLineBefore,
}: {
  handleAddLineAfter: (idx: number) => Promise<void>;
  handleAddLineBefore: (idx: number) => Promise<void>;
  handleRemoveLine: (idx: number) => Promise<void>;
  line: ResultOf<typeof TranscriptLineFragment>;
  idx: number;
  handleUpdate: (idx: number, newText: string) => Promise<void>;
}) {
  const [isEditing, setIsEditing] = useState(false);
  const ref = useRef<HTMLParagraphElement>(null);

  return (
    <Dialog>
      <div className="flex space-x-3">
        <SpeakerBadge speaker={line.speaker} />
        <>
          <p ref={ref} className="grow" contentEditable={isEditing}>
            {line.text}
          </p>
          <div className="flex flex-row items-center space-x-2">
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
                    handleUpdate(idx, newText);
                  }
                }}
              >
                <CheckIcon />
              </Button>
            )}
            <div className="flex flex-col space-y-1">
              <Button
                onClick={() => {
                  handleAddLineBefore(idx);
                }}
              >
                Add Line Before
              </Button>
              <Button
                onClick={() => {
                  handleAddLineAfter(idx);
                }}
              >
                Add Line After
              </Button>
            </div>
            <DialogTrigger asChild>
              <Button variant={"destructive"}>
                <Trash />
              </Button>
            </DialogTrigger>
          </div>
        </>
        <AreYouSureDialog onSuccess={handleRemoveLine} idx={idx} />
      </div>
    </Dialog>
  );
}

function AreYouSureDialog({
  onSuccess,
  idx,
}: {
  idx: number;
  onSuccess: (id: number) => Promise<void>;
}) {
  return (
    <DialogContent className="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Are You Sure?</DialogTitle>
      </DialogHeader>
      <div className="flex flex-row justify-between">
        <DialogClose asChild>
          <Button
            variant={"destructive"}
            onClick={async () => {
              console.log("does this work");
              await onSuccess(idx);
            }}
          >
            Yes
          </Button>
        </DialogClose>
        <DialogClose asChild>
          <Button>Cancel</Button>
        </DialogClose>
      </div>
    </DialogContent>
  );
}

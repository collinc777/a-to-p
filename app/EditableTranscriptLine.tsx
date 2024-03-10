import { useRef, useState } from "react";
import { CheckIcon, FilePenLine, Trash } from "lucide-react";
import { ResultOf } from "gql.tada";
import { TranscriptLineFragment } from "./queries";
import { Button } from "@/components/ui/button";
import { Dialog } from "@radix-ui/react-dialog";
import { DialogTrigger } from "@/components/ui/dialog";
import { SpeakerBadge } from "./TranscriptViewer";
import { AreYouSureDialog } from "./AreYouSureDialog";

export function EditableTranscriptLine({
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

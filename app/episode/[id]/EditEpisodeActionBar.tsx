"use client";
import { AudioPlayer } from "@/app/AudioPlayer";
import DownloadButton from "./DownloadButton";
import { Button } from "@/components/ui/button";
import { FragmentOf } from "@/app/graphql";
import { EpisodeFragment, TranscriptFragment } from "@/app/queries";
import { useMutation } from "@apollo/client";
import { GenerateAudioMutation } from "./EpisodeDetails";
import { isEqual } from "lodash";
import { Alert, AlertDescription, AlertTitle } from "@/components/ui/alert";
import { ExclamationTriangleIcon } from "@radix-ui/react-icons";

export function EditEpisodeActionBar({
  episode,
  editableTranscriptCopy,
}: {
  episode: FragmentOf<typeof EpisodeFragment>;
  editableTranscriptCopy: FragmentOf<typeof TranscriptFragment>;
}) {
  const [generateAudio] = useMutation(GenerateAudioMutation);
  const isDirty = !isEqual(episode.transcript, editableTranscriptCopy);
  return (
    <div className="flex flex-row items-center space-x-2">
      <AudioPlayer url={episode.url} />
      <DownloadButton url={episode.url} />
      <Button
        onClick={async () => {
          const result = await generateAudio({
            variables: { id: episode.id! },
          });
        }}
      >
        Regenerate Audio
      </Button>
      {isDirty && (
        <Alert variant={"warn"}>
          <ExclamationTriangleIcon className="h-4 w-4" />
          <AlertTitle>Edited transcript doesnt match audio</AlertTitle>
          <AlertDescription>
            Regenerate the audio to match the edited transcript
          </AlertDescription>
        </Alert>
      )}
    </div>
  );
}

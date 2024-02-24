import { AudioPlayer } from "@/app/AudioPlayer";
import TranscriptViewer from "@/app/TranscriptViewer";
import { Episode } from "@/app/types";
import Link from "next/link";
import DownloadButton from "./DownloadButton";
import { Button } from "@/components/ui/button";

export const EpisodeDetails = ({ episode }: { episode: Episode }) => {
  const isEditable = episode?.status === "done";
  const transcript = episode?.transcript;
  return (
    <main className="px-4 space-y-2 pb-4">
      <div>
        {episode?.extracted_article?.url ? (
          <Link
            href={episode?.extracted_article?.url}
            className="text-blue-500 hover:text-blue-700 underline"
          >
            <h1 className="text-3xl font-bold">
              Generated Episode: {episode?.extracted_article?.title}
            </h1>
          </Link>
        ) : (
          <h1 className="text-xl">
            Generated Episode: {episode?.extracted_article?.title}
          </h1>
        )}
      </div>
      <div className="flex flex-row items-center space-x-3 flex-wrap space-y-3">
        {episode.url ? (
          <>
            <AudioPlayer url={episode.url} />
            <DownloadButton url={episode.url} />
            <Button onClick={() => regenerateAudio(id)}>
              Regenerate episode
            </Button>
          </>
        ) : (
          <p>Audio not available</p>
        )}
      </div>
      <div>
        <h2 className="text-2xl font-semibold">Transcript</h2>
        {transcript ? (
          <TranscriptViewer
            episodeId={episode.id!}
            transcript={episode?.transcript}
            isEditable={isEditable}
          />
        ) : (
          <TranscriptLoading />
        )}
      </div>
    </main>
  );
};

export const TranscriptLoading = () => {
  return <p>Loading transcript...</p>;
};

import { AudioPlayer } from "@/app/AudioPlayer";
import TranscriptViewer from "@/app/TranscriptViewer";
import Link from "next/link";
import DownloadButton from "./DownloadButton";
import { Button } from "@/components/ui/button";
import { FragmentOf, ResultOf, readFragment } from "@/app/graphql";
import { EpisodeFragment } from "@/app/queries";

export const EpisodeDetails = ({
  episode,
}: {
  episode: ResultOf<typeof EpisodeFragment>;
}) => {
  const isEditable = episode?.status === "done";
  const transcript = episode?.transcript;
  return (
    <main className="px-4 space-y-2 pb-4">
      <div>
        {episode?.extractedArticle?.url ? (
          <Link
            href={episode?.extractedArticle?.url}
            className="text-blue-500 hover:text-blue-700 underline"
          >
            <h1 className="text-3xl font-bold">
              Generated Episode: {episode?.extractedArticle?.title}
            </h1>
          </Link>
        ) : (
          <h1 className="text-xl">
            Generated Episode: {episode?.extractedArticle?.title}
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
            transcriptFrag={episode?.transcript}
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

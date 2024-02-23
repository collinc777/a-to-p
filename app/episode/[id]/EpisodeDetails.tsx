import { AudioPlayer } from "@/app/AudioPlayer";
import TranscriptViewer from "@/app/TranscriptViewer";
import { Episode } from "@/app/types";
import Link from "next/link";
import DownloadButton from "./DownloadButton";

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
      <div>
        {episode.url ? (
          <AudioPlayer url={episode.url} />
        ) : (
          <p>Audio not available</p>
        )}
      </div>
      <div className="grid lg:grid-cols-2 gap-3">
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
        <div>
          <h2 className="text-2xl font-semibold">Article</h2>
          <p>{episode?.article_text}</p>
        </div>
      </div>
    </main>
  );
};

export const TranscriptLoading = () => {
  return <p>Loading transcript...</p>;
};

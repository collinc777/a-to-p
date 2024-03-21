"use client";
import TranscriptViewer from "@/app/TranscriptViewer";
import { EditTranscriptView } from "@/app/EditTranscriptView";
import Link from "next/link";
import { ResultOf, readFragment } from "@/app/graphql";
import { EpisodeFragment, ExtractedArticleFragment } from "@/app/queries";
import { Skeleton } from "@/components/ui/skeleton";
import { graphql } from "@/app/graphql";

export const EpisodeDetails = ({
  episode,
}: {
  episode: ResultOf<typeof EpisodeFragment>;
}) => {
  const extractedArticle = readFragment(
    ExtractedArticleFragment,
    episode.extractedArticle
  );
  const isEditable = episode?.status === "done";
  return (
    <main className="px-4 space-y-2 pb-4">
      <div>
        {extractedArticle?.url ? (
          <Link
            href={extractedArticle?.url}
            className="text-blue-500 hover:text-blue-700 underline"
          >
            <h1 className="text-3xl font-bold">
              Generated Episode: {extractedArticle?.title}
            </h1>
          </Link>
        ) : (
          <h1 className="text-xl">
            Generated Episode: {extractedArticle?.title}
          </h1>
        )}
      </div>
      <div>
        <h2 className="text-2xl font-semibold">Transcript</h2>
        {episode.transcript && episode.status ? (
          <>
            {isEditable ? (
              <EditTranscriptView
                transcript={episode?.transcript}
                episode={episode}
              />
            ) : (
              <TranscriptViewer
                episodeId={episode.id!}
                transcript={episode?.transcript}
                episodeStatus={episode.status!}
              />
            )}
          </>
        ) : (
          <TranscriptLoading />
        )}
      </div>
    </main>
  );
};

export const TranscriptLoading = () => {
  return <Skeleton className="w-full h-10" />;
};

export const GenerateAudioMutation = graphql(
  `
    mutation generateAudio($id: String!) {
      generateEpisodeAudio(episodeId: $id) {
        ...EpisodeFragment
      }
    }
  `,
  [EpisodeFragment]
);

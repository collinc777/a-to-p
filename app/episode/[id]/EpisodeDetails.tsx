"use client";
import { AudioPlayer } from "@/app/AudioPlayer";
import TranscriptViewer, { EditTranscriptView } from "@/app/TranscriptViewer";
import Link from "next/link";
import DownloadButton from "./DownloadButton";
import { Button } from "@/components/ui/button";
import { FragmentOf, ResultOf, readFragment } from "@/app/graphql";
import { EpisodeFragment, ExtractedArticleFragment } from "@/app/queries";
import { Skeleton } from "@/components/ui/skeleton";
import { graphql } from "@/app/graphql";
import { useMutation } from "@apollo/client";

export const EpisodeDetails = ({
  episode,
}: {
  episode: ResultOf<typeof EpisodeFragment>;
}) => {
  const [generateAudio] = useMutation(GenerateAudioMutation);

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
      <div className="flex flex-row items-center space-x-3 flex-wrap space-y-3">
        {episode.url && episode.status === "done" ? (
          <>
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
          </>
        ) : (
          <Skeleton className="w-40 h-10" />
        )}
      </div>
      <div>
        <h2 className="text-2xl font-semibold">Transcript</h2>
        {episode.transcript && episode.status ? (
          <>
            <EditTranscriptView
              transcript={episode?.transcript}
              episodeId={episode.id}
            />
            <TranscriptViewer
              episodeId={episode.id!}
              transcript={episode?.transcript}
              episodeStatus={episode.status!}
            />
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

const GenerateAudioMutation = graphql(
  `
    mutation generateAudio($id: String!) {
      generateEpisodeAudio(episodeId: $id) {
        ...EpisodeFragment
      }
    }
  `,
  [EpisodeFragment]
);

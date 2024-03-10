import { FragmentOf } from "gql.tada";
import { TranscriptFragment } from "./queries";
import { Skeleton } from "@/components/ui/skeleton";
import { TranscriptLoading } from "./episode/[id]/EpisodeDetails";
import { graphql } from "./graphql";

export default function TranscriptViewer({
  transcript: transcript,
}: {
  episodeId: string;
  transcript: FragmentOf<typeof TranscriptFragment>;
  episodeStatus: ReturnType<typeof graphql.scalar<"EpisodeStatus">>;
}) {
  const transcriptLines = transcript.transcriptLines;
  return (
    <div className="space-y-3">
      <TranscriptLoading />
      {transcriptLines?.map((line, idx) => {
        return <TranscriptLine key={idx} idx={idx} line={line} />;
      })}
      <TranscriptLoading />
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

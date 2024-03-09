"use client";
import { usePollEpisodeV3 } from "@/app/hooks/usePollEpisode";
import { EpisodeDetails } from "./EpisodeDetails";

export default function EpisodeDetailsPoller({
  episodeId,
}: {
  episodeId: string;
}) {
  const episodeResult = usePollEpisodeV3(episodeId);
  if (!episodeResult) return null;
  return <EpisodeDetails episode={episodeResult} />;
}

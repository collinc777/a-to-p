"use client";
import { Episode } from "@/app/types";
import { EpisodeDetails } from "./EpisodeDetails";
import { usePollEpisodeV2 } from "@/app/hooks/usePollEpisode";

export default function EpisodeDetailsPoller({
  episode,
}: {
  episode: Episode;
}) {
  const episodeResult = usePollEpisodeV2(episode);
  return <EpisodeDetails episode={episodeResult} />;
}

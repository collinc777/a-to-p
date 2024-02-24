"use client";
import { Episode } from "@/app/types";
import { EpisodeDetails } from "./EpisodeDetails";
import { usePollEpisodeV2 } from "@/app/hooks/usePollEpisode";
import { ResultOf } from "gql.tada";

export default function EpisodeDetailsPoller({
  episode,
}: {
  episode: ResultOf<typeof Episode>;
}) {
  const episodeResult = usePollEpisodeV2(episode);
  return <EpisodeDetails episode={episodeResult} />;
}

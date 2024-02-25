"use client";
import { usePollEpisodeV3 } from "@/app/hooks/usePollEpisode";
import { EpisodeDetails } from "./EpisodeDetails";
import { EpisodeFragment, EpisodeQuery } from "@/app/queries";
import { ResultOf } from "gql.tada";
import { Fragment } from "react";

export default function EpisodeDetailsPoller({
  episode,
}: {
  episode: ResultOf<typeof EpisodeFragment>;
}) {
  const episodeResult = usePollEpisodeV3(episode);
  if (!episodeResult) return null;
  return <EpisodeDetails episode={episodeResult} />;
}

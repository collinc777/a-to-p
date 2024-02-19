import { useEffect, useState } from "react";
import { Episode } from "../types";
import { frontendClient } from "../clients";

export function usePollEpisodeV2(episode: Episode) {
  const [episodeResult, setEpisodeResult] = useState<Episode>(episode);
  useEffect(() => {
    const isPollable = () => {
      return !["failed", "done"].includes(episode.status);
    };
    if (isPollable() && episode.id) {
      const interval = setInterval(async () => {
        const updatedEpisode = await frontendClient.GET("/api/episode/{id}", {
          params: {
            path: {
              id: episode.id as string,
            },
          },
        });
        if (updatedEpisode?.data) {
          setEpisodeResult(updatedEpisode.data);
        }
        if (updatedEpisode?.data?.status === "done") {
          clearInterval(interval);
        }
      }, 1000);
      return () => clearInterval(interval);
    }
  }, [episode]);
  return episodeResult;
}

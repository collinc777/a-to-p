import { useEffect } from "react";
import { useQuery } from "@apollo/experimental-nextjs-app-support/ssr";
import { EpisodeFragment, EpisodeQuery } from "../queries";
import { ResultOf, readFragment } from "../graphql";
type EpisodeType = ResultOf<typeof EpisodeFragment>;
const isPollable = (episode: EpisodeType) =>
  !["done", "failed"].includes(episode.status);

export function usePollEpisodeV3(serverSideEpisode: EpisodeType) {
  const { data, startPolling, stopPolling } = useQuery(EpisodeQuery, {
    variables: {
      id: serverSideEpisode.id as string,
    },
    skip: ["done", "failed"].includes(serverSideEpisode.status),
    notifyOnNetworkStatusChange: true, // Optional: to make the component re-render on poll updates
  });
  const episodeFrag = readFragment(EpisodeFragment, data?.episode);

  useEffect(() => {
    if (isPollable(serverSideEpisode)) {
      // Start polling
      startPolling(1000); // Poll every 5000 milliseconds (5 seconds)

      // Stop polling when the episode status is 'done' or 'failed'
      if (episodeFrag?.status && !isPollable(episodeFrag)) {
        stopPolling();
      }

      // Cleanup function to stop polling when the component unmounts
      return () => stopPolling();
    }
  }, [
    data,
    episodeFrag,
    episodeFrag?.status,
    serverSideEpisode,
    startPolling,
    stopPolling,
  ]);

  // Extract and return the episode fragment, if needed
  return episodeFrag ?? serverSideEpisode;
}

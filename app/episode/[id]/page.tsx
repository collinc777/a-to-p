import EpisodeDetailsPoller from "./EpisodeDetailsPoller";
import { getClient } from "@/app/ApolloClient";
import { ResultOf, readFragment } from "@/app/graphql";
import { EpisodeFragment, EpisodeQuery } from "@/app/queries";

export const dynamic = "force-dynamic";

async function getEpisode(
  episodeId: string
): Promise<ResultOf<typeof EpisodeQuery>> {
  const response = await getClient().query({
    query: EpisodeQuery,
    variables: {
      id: episodeId,
    },
  });
  if (response.data) {
    return response.data;
  } else {
    throw new Error("No episode found");
  }
}
export default async function EpisodeDetailPage({
  params,
}: {
  params: { id: string };
}) {
  const data = await getEpisode(params.id);
  const episode = readFragment(EpisodeFragment, data.episode);
  return <EpisodeDetailsPoller episode={episode} />;
}

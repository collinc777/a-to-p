import EpisodeDetailsPoller from "./EpisodeDetailsPoller";
import { getClient } from "@/app/ApolloClient";
import { Episode } from "@/app/fragments/episode";
import { ResultOf, graphql, readFragment } from "@/app/graphql";

async function getEpisode(
  episodeId: string
): Promise<ResultOf<typeof Episode>> {
  const response = await getClient().query({
    query: EpisodeQuery,
    variables: {
      id: episodeId,
    },
  });
  if (response.data) {
    const episode = readFragment(Episode, response.data.episode);
    return episode;
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
  return <EpisodeDetailsPoller episode={data} />;
}

const EpisodeQuery = graphql(
  `
    query getEpisode($id: String!) {
      episode(id: $id) {
        ...EpisodeFragment
      }
    }
  `,
  [Episode]
);

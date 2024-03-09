import EpisodeDetailsPoller from "./EpisodeDetailsPoller";

export default async function EpisodeDetailPage({
  params,
}: {
  params: { id: string };
}) {
  return <EpisodeDetailsPoller episodeId={params.id} />;
}

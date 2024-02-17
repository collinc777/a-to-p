async function getEpisode(episodeId: string) {
  return (await fetch(`${process.env.BACKEND_HOST}/api/episode/${episodeId}`)).json();
}
export default async function EpisodePageDetail({
  params,
}: {
  params: { id: string };
}) {
  const data = await getEpisode(params.id);
  return (
    <div>
      <div>hello world: {params.id}</div>
      <div>{JSON.stringify(data)}</div>
    </div>
  );
}

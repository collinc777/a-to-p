import TranscriptViewer from "@/app/TranscriptViewer";
import { Episode } from "@/app/types";
import Link from "next/link";

async function getEpisode(episodeId: string): Promise<Episode> {
  return (
    await fetch(`${process.env.BACKEND_HOST}/api/episode/${episodeId}`)
  ).json();
}
export default async function EpisodePageDetail({
  params,
}: {
  params: { id: string };
}) {
  const data = await getEpisode(params.id);
  const transcript = data.transcript;
  console.log({ data });
  return (
    <div>
      <div>
        {data?.url ? (
          <Link
            href={data?.url}
            className="text-blue-500 hover:text-blue-700 underline"
          >
            <h1 className="text-3xl font-bold">
              Generated Episode {data?.extracted_article?.title}
            </h1>
          </Link>
        ) : (
          <h1 className="text-xl">
            Generated Episode {data?.extracted_article?.title}
          </h1>
        )}
      </div>
      {transcript && <TranscriptViewer transcript={data?.transcript} />}
    </div>
  );
}

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
  return (
    <main className="px-4 space-y-2 pb-4">
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
      <div>
        <audio controls src={data?.url} />
      </div>
      <div className="grid lg:grid-cols-2 gap-3">
        <div>
          <h2 className="text-2xl font-semibold">Transcript</h2>
          {transcript && <TranscriptViewer transcript={data?.transcript} />}
        </div>
        <div>
          <h2 className="text-2xl font-semibold">Article</h2>
          <p>{data?.article_text}</p>
        </div>
      </div>
    </main>
  );
}

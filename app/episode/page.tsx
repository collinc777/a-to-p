"use client";

import { useCallback, useEffect, useState } from "react";
import { start } from "repl";

function usePollEpisode() {
  const [episodeId, setEpisodeId] = useState<string>("");
  const [url, setUrl] = useState<string>("");
  // poll for episode once the episode id is set
  // stop polling once the url exists
  useEffect(() => {
    if (episodeId) {
      const interval = setInterval(async () => {
        const episode = await fetchEpisode(episodeId);
        const episodeUrl = await episode["url"];
        if (episodeUrl) {
          setUrl(episodeUrl);
          clearInterval(interval);
        }
      }, 5000);
    }
  }, [episodeId]);
  return { episodeId, setEpisodeId, url };
}

export default function EpisodePage() {
  const [articleText, setArticleText] = useState<string>("");
  const { episodeId, setEpisodeId, url } = usePollEpisode();
  return (
    <main>
      <div>
        <h1>Generate a podcast episode</h1>
        <textarea
          className="text-black"
          id="article_text"
          name="article_text"
          rows={4}
          cols={50}
          onChange={(e) => setArticleText(e.target.value)}
        />
        <button
          onClick={async () => {
            const response = await (
              await fetch("/api/episode_create_task", {
                method: "POST",
                body: JSON.stringify({
                  article_text: articleText,
                }),
                headers: {
                  "Content-Type": "application/json",
                },
              })
            ).json();
            console.log({ response });
            const episodeId = await response["id"];
            setEpisodeId(episodeId);
          }}
        >
          Generate Episode
        </button>
        {url && <audio src={url}></audio>}
        <AudioPlayer url={url} />
      </div>
    </main>
  );
}
const AudioPlayer = ({ url }: { url: string }) => {
  return (
    <audio controls>
      <source src={url} type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  );
};

async function fetchEpisode(episodeId: any) {
  return await (
    await fetch(`/api/episode/${episodeId}`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
      next: {
        revalidate: 0,
      },
    })
  ).json();
}

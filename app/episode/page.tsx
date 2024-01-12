"use client";

import { useState } from "react";

export default function EpisodePage() {
  const [articleText, setArticleText] = useState<string>("");
  const [sound, setSoundURL] = useState<string>();
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
            const audio = await fetch("/api/episode", {
              method: "POST",
              body: JSON.stringify({
                article_text: articleText,
              }),
              headers: {
                "Content-Type": "application/json",
              },
            });
            await audio.blob().then((blob) => {
              const url = URL.createObjectURL(blob);
              setSoundURL(url);
            });
          }}
        >
          Generate Episode
        </button>
        {sound && <audio src={sound}></audio>}
      </div>
    </main>
  );
}

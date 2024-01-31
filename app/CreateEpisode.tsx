"use client";
import { useCompletion } from "ai/react";
/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/GodnNeW0haD
 */
import Link from "next/link";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useEffect, useState } from "react";
import { Label } from "@/components/ui/label";
import { usePostHog } from "posthog-js/react";
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

function usePollEpisode() {
  const [episodeId, setEpisodeId] = useState<string>("");
  const [url, setUrl] = useState<string>("");
  const [episodeLoading, setEpisodeLoading] = useState<boolean>(false);
  const [transcript, setTranscript] = useState<string>("");

  useEffect(() => {
    if (episodeId) {
      setEpisodeLoading(true);
      const interval = setInterval(async () => {
        const episode = await fetchEpisode(episodeId);
        const transcriptResponse = episode["transcript"];
        if (transcriptResponse) {
          setTranscript(transcriptResponse);
        }
        const episodeUrl = episode["url"];
        if (episodeUrl) {
          setUrl(episodeUrl);
          clearInterval(interval);
          setEpisodeLoading(false);
        }
      }, 5000);
    }
  }, [episodeId]);

  return { episodeId, setEpisodeId, url, episodeLoading, transcript };
}

export function CreateEpisode() {
  const { completion, complete, handleInputChange, handleSubmit, input } =
    useCompletion({
      api: "/api/custom_completions",
    });
  const result = completion.split("[SENTINEL]");
  const { episodeId, setEpisodeId, url, episodeLoading, transcript } =
    usePollEpisode();
  const [formSubmitting, setFormSubmitting] = useState<boolean>(false);
  return (
    <div className="flex flex-col min-h-screen bg-white dark:bg-gray-900">
      <header className="w-full py-6 px-4 bg-white border-b dark:bg-gray-900 dark:border-gray-800">
        <div className="container mx-auto flex items-center justify-between">
          <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">
            Article to Podcast
          </h1>
        </div>
      </header>
      <main className="flex-1 py-8 px-4 bg-gray-50 dark:bg-gray-800">
        <div className="container mx-auto">
          <form onSubmit={handleSubmit}>
            <label htmlFor="ask-input"></label>
            <input
              id="ask-input"
              className="text-black"
              type="text"
              value={input}
              onChange={handleInputChange}
            />
            <p>{result[result.length - 2]}</p>
            <button type="submit">POST</button>
          </form>

          <form
            className="w-full max-w-lg mx-auto space-y-4"
            onSubmit={async (e) => {
              setFormSubmitting(true);
              e.preventDefault();
              const text = (e.target as any).inputText.value;
              let payload = {};
              if (text.startsWith("http")) {
                payload = { article_url: text };
              } else {
                payload = { article_text: text };
              }
              const response = await (
                await fetch("/api/episode_create_task", {
                  method: "POST",
                  body: JSON.stringify(payload),
                  headers: {
                    "Content-Type": "application/json",
                  },
                })
              ).json();
              const epId = await response["id"];
              setEpisodeId(epId);
              setFormSubmitting(false);
            }}
          >
            <Label htmlFor="inputText">
              Paste an article URL or some text to generate a podcast from it
            </Label>
            <Input
              name="inputText"
              className="w-full"
              placeholder="Paste your text or URL here"
              type="text"
            />
            <Button
              className="w-full"
              type="submit"
              disabled={episodeLoading || formSubmitting}
            >
              Generate Podcast Episode
            </Button>
          </form>
          <div className="mt-8 space-y-4">
            <h2 className="text-xl font-bold text-gray-900 dark:text-gray-100">
              Your Podcast Episode
            </h2>
            <p>Episode generation takes around 3 minutes</p>
            <div className="flex flex-col items-center space-x-4">
              {url && (
                <div>
                  <AudioPlayer url={url} />
                </div>
              )}
              {episodeLoading && (
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-gray-900 dark:border-gray-100"></div>
              )}
              {episodeLoading && transcript && (
                <div>
                  <p>Generating Audio</p>
                </div>
              )}
              {transcript && (
                <div>
                  <h3 className="text-lg font-bold text-gray-900 dark:text-gray-100">
                    Transcript
                  </h3>
                  <p>{JSON.stringify(transcript)}</p>
                </div>
              )}
              {episodeLoading && !transcript && (
                <div>
                  <p>Generating Transcript</p>
                </div>
              )}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

const AudioPlayer = ({ url }: { url: string }) => {
  const something = usePostHog();
  return (
    <audio
      controls
      onPlay={() => {
        something.capture("played");
      }}
    >
      <source src={url} type="audio/mpeg" />
      Your browser does not support the audio element.
    </audio>
  );
};

"use client";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FormButton } from "./FormButton";
import { createEpisode } from "./actions";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { graphql } from "./graphql";
import { useSuspenseQuery } from "@apollo/experimental-nextjs-app-support/ssr";
import { usePostHog } from "posthog-js/react";

export function CreateEpisode() {
  const { data } = useSuspenseQuery(EpisodeFormatChoicesQuery);
  const ph = usePostHog();
  return (
    <main className="flex-1 py-8 px-4">
      <div className="container mx-auto">
        <form
          className="w-full max-w-lg mx-auto space-y-4"
          action={createEpisode}
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
          <Select
            name="podcastFormatSelector"
            onValueChange={(e) => {
              ph.capture("Podcast Format Selected", {
                podcastFormat: e,
              });
              const selectedFormat = data.episodeFormatChoices.find(
                (format) => format.value === e
              );
              if (!selectedFormat?.isReady) {
              }
            }}
          >
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Podcast Format..." />
            </SelectTrigger>
            <SelectContent>
              {data.episodeFormatChoices.map((format) => (
                <SelectItem
                  key={format.value}
                  value={format.value}
                  disabled={!format.isReady}
                >
                  {format.displayName}
                </SelectItem>
              ))}
              <SelectItem value="other">Other</SelectItem>
            </SelectContent>
          </Select>
          <FormButton />
        </form>
      </div>
    </main>
  );
}

const EpisodeFormatChoicesQuery = graphql(`
  query EpisodeFormatChoicesQuery {
    episodeFormatChoices {
      value
      displayName
      isReady
    }
  }
`);

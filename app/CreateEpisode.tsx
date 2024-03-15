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
import { ResultOf, graphql, readFragment } from "./graphql";
import { useSuspenseQuery } from "@apollo/experimental-nextjs-app-support/ssr";
import { usePostHog } from "posthog-js/react";

const EpisodeFormatChoiceFragment = graphql(`
  fragment EpisodeFormatChoice on EpisodeFormatChoice {
    value
    displayName
    isReady
  }
`);

const EpisodeFormatChoicesQuery = graphql(
  `
    query EpisodeFormatChoicesQuery {
      episodeFormatChoices {
        ...EpisodeFormatChoice
      }
    }
  `,
  [EpisodeFormatChoiceFragment]
);

export function CreateEpisode() {
  const { data } = useSuspenseQuery(EpisodeFormatChoicesQuery);
  const ph = usePostHog();
  const episodeFormatChoices = readFragment(
    EpisodeFormatChoiceFragment,
    data?.episodeFormatChoices
  );
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
              const selectedFormat = episodeFormatChoices.find(
                (format) => format.value === e
              );
            }}
          >
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Podcast Format..." />
            </SelectTrigger>
            <SelectContent>
              {episodeFormatChoices.map((format) => (
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

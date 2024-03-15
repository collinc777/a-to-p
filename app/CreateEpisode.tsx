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
  fragment EpisodeFormatFragment on EpisodeFormat {
    id
    displayValue
  }
`);

const EpisodeFormatChoicesQuery = graphql(
  `
    query EpisodeFormat {
      episodeFormats {
        ...EpisodeFormatFragment
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
    data?.episodeFormats
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
                (format) => format.id === e
              );
            }}
          >
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Podcast Format..." />
            </SelectTrigger>
            <SelectContent>
              {episodeFormatChoices.map((format) => (
                <SelectItem key={format.id} value={format.id}>
                  {format.displayValue}
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

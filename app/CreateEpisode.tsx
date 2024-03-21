"use client";
import { Input } from "@/components/ui/input";
import { FormButton } from "./FormButton";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { graphql, readFragment } from "./graphql";
import { useSuspenseQuery } from "@apollo/experimental-nextjs-app-support/ssr";
import { usePostHog } from "posthog-js/react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { useMutation } from "@apollo/client";
import { useRouter } from "next/navigation";

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

const formSchema = z.object({
  inputText: z.string(),
  podcastFormatSelector: z.string(),
});
export function CreateEpisode() {
  const router = useRouter();
  const { data } = useSuspenseQuery(EpisodeFormatChoicesQuery);
  const [createEpisode] = useMutation(CreateEpisodeMutation);
  const ph = usePostHog();
  const episodeFormatChoices = readFragment(
    EpisodeFormatChoiceFragment,
    data?.episodeFormats
  );
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
  });
  return (
    <main className="flex-1 py-8 px-4">
      <div className="container mx-auto">
        <Form {...form}>
          <form
            className="w-full max-w-lg mx-auto space-y-4"
            onSubmit={form.handleSubmit(
              async ({ inputText, podcastFormatSelector }) => {
                let payload = {};
                if (inputText.startsWith("http")) {
                  payload = { articleUrl: inputText };
                } else {
                  payload = { articleText: inputText };
                }
                const result = await createEpisode({
                  variables: {
                    input: {
                      ...payload,
                      episodeFormatId: podcastFormatSelector,
                    },
                  },
                });
                const id = result?.data?.createEpisodeCreationTask?.id;
                router.push(`/episode/${id}`);
              }
            )}
          >
            <FormField
              name="inputText"
              control={form.control}
              render={({ field }) => {
                return (
                  <FormItem>
                    <FormLabel>
                      Paste an article URL or some text to generate a podcast
                      from it
                    </FormLabel>
                    <FormControl>
                      <Input {...field} />
                    </FormControl>
                  </FormItem>
                );
              }}
            />
            <FormField
              name="podcastFormatSelector"
              control={form.control}
              render={({ field }) => {
                return (
                  <FormItem>
                    <Select
                      onValueChange={(e) => {
                        field.onChange(e);
                        ph.capture("Podcast Format Selected", {
                          podcastFormat: e,
                        });
                      }}
                    >
                      <FormControl>
                        <SelectTrigger className="w-full">
                          <SelectValue placeholder="Podcast Format..." />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        {episodeFormatChoices.map((format) => (
                          <SelectItem key={format.id} value={format.id}>
                            {format.displayValue}
                          </SelectItem>
                        ))}
                      </SelectContent>
                    </Select>
                    <FormMessage />
                  </FormItem>
                );
              }}
            />
            <FormButton />
          </form>
        </Form>
      </div>
    </main>
  );
}

export const CreateEpisodeMutation = graphql(`
  mutation createEpisode($input: CreateEpisodeInput!) {
    createEpisodeCreationTask(input: $input) {
      id
    }
  }
`);

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
import {
  useReadQuery,
  useSuspenseQuery,
} from "@apollo/experimental-nextjs-app-support/ssr";
import { usePostHog } from "posthog-js/react";
import { Control, useForm } from "react-hook-form";
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
import { useApolloClient, useMutation } from "@apollo/client";
import { RedirectType, redirect, useRouter } from "next/navigation";
import { use, useEffect } from "react";
import { set } from "lodash";

const EpisodeFormatChoiceFragment = graphql(`
  fragment EpisodeFormatFragment on EpisodeFormat {
    id
    displayValue
    episodeFormatType
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

const baseSchema = z.object({
  inputText: z.string(),
});

const monologueSchema = baseSchema.extend({
  episodeFormat: z.literal("monologue"),
  speakerName: z.string(),
});
const dialogueSchema = baseSchema.extend({
  episodeFormat: z.literal("dialogue"),
  firstSpeakerName: z.string(),
  secondSpeakerName: z.string(),
});
const FormSchema = z.discriminatedUnion("episodeFormat", [
  monologueSchema,
  dialogueSchema,
]);

export function CreateEpisode() {
  const router = useRouter();
  const { data } = useSuspenseQuery(EpisodeFormatChoicesQuery);
  const [createEpisode] = useMutation(CreateEpisodeMutation);
  const ph = usePostHog();
  const episodeFormatChoices = readFragment(
    EpisodeFormatChoiceFragment,
    data?.episodeFormats
  );
  const form = useForm<z.infer<typeof FormSchema>>({
    resolver: zodResolver(FormSchema),
  });
  const { watch, setValue, control } = form;

  const watchEpisodeFormat = watch("episodeFormat");

  return (
    <main className="flex-1 py-8 px-4">
      <div className="container mx-auto">
        <Form {...form}>
          <form
            className="w-full max-w-lg mx-auto space-y-4"
            onSubmit={form.handleSubmit(
              async ({ inputText, episodeFormat }) => {
                const episodeFormatId = episodeFormatChoices.find(
                  (format) => format.episodeFormatType === episodeFormat
                )?.id;
                if (!episodeFormatId) {
                  return;
                }
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
                      episodeFormatId,
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
              rules={{ required: "This field is required" }}
              render={({ field, formState }) => {
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
              name="episodeFormat"
              control={form.control}
              render={({ field }) => {
                return (
                  <FormItem>
                    <Select
                      onValueChange={(e) => {
                        field.onChange(e);
                      }}
                    >
                      <FormControl>
                        <SelectTrigger className="w-full">
                          <SelectValue placeholder="Podcast Format..." />
                        </SelectTrigger>
                      </FormControl>
                      <SelectContent>
                        {episodeFormatChoices.map((format) => (
                          <SelectItem
                            key={format.id}
                            value={format.episodeFormatType}
                          >
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
            {watchEpisodeFormat === "monologue" && (
              <FormatConfigurationSettings
                config={monologueConfig}
                control={form.control}
              />
            )}
            <FormButton />
          </form>
        </Form>
      </div>
    </main>
  );
}
const monologueConfig = {
  field: {
    name: "speakerName",
    label: "Speaker Name",
  },
};

export const FormatConfigurationSettings = ({
  config,
  control,
}: {
  config: typeof monologueConfig;
  control: Control<any>;
}) => {
  return (
    <>
      <FormField
        name="speakerName"
        control={control}
        render={({ field }) => {
          return (
            <FormItem>
              <FormLabel>{config.field.label}</FormLabel>
              <FormControl>
                <Input {...field} />
              </FormControl>
            </FormItem>
          );
        }}
      />
    </>
  );
};

export const CreateEpisodeMutation = graphql(`
  mutation createEpisode($input: CreateEpisodeInput!) {
    createEpisodeCreationTask(input: $input) {
      id
    }
  }
`);

"use server";
import { RedirectType, redirect } from "next/navigation";
import { backendClient } from "./clients";
import { ResultOf, VariablesOf, graphql } from "./graphql";
import { EpisodeFragment } from "./queries";
import { getClient } from "./ApolloClient";
export async function createEpisode(formData: FormData) {
  const text = formData.get("inputText") as string;
  let payload = {};
  if (text.startsWith("http")) {
    payload = { article_url: text };
  } else {
    payload = { article_text: text };
  }
  const response = await backendClient.POST("/api/episode_create_task", {
    body: payload,
  });
  const id = response.data?.id
  if (id) {
    redirect(`/episode/${id}`, RedirectType.push)
  }
}

export async function updateEpisode(input: VariablesOf<typeof UpdateEpisodeMutation>) {
  const result = await getClient().mutate({
    mutation: UpdateEpisodeMutation,
    variables: input,
  })
  return result
}

export async function regenerateAudio(id: string) {
  // todo regen audio
}

const UpdateEpisodeMutation = graphql(`
mutation updateEpisode($id: String!, $input: UpdateEpisodeInput!) {
  updateEpisode(id: $id, input: $input) {
    ...EpisodeFragment

    }
    }`, [EpisodeFragment]);
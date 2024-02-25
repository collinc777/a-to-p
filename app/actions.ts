"use server";
import { RedirectType, redirect } from "next/navigation";
import { VariablesOf, graphql } from "./graphql";
import { EpisodeFragment } from "./queries";
import { getClient } from "./ApolloClient";
export async function createEpisode(formData: FormData) {
  const text = formData.get("inputText") as string;
  let payload = {};
  if (text.startsWith("http")) {
    payload = { articleUrl: text };
  } else {
    payload = { articleText: text };
  }
  const result = await getClient().mutate({
    mutation: CreateEpisodeMutation,
    variables: {
      input: payload,
    },
  });
  const id = result?.data?.createEpisodeCreationTask?.id;
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


const UpdateEpisodeMutation = graphql(`
mutation updateEpisode($id: String!, $input: UpdateEpisodeInput!) {
  updateEpisode(id: $id, input: $input) {
    ...EpisodeFragment

    }
    }`, [EpisodeFragment]);

  const CreateEpisodeMutation = graphql(`
  mutation createEpisode($input: CreateEpisodeInput!) {
    createEpisodeCreationTask(input: $input) {
      id
    }
  }
`);


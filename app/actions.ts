"use server";
import { RedirectType, redirect } from "next/navigation";
import { VariablesOf, graphql } from "./graphql";
import { EpisodeFragment } from "./queries";
import { getClient } from "./ApolloClient";
import { revalidatePath } from "next/cache";


export async function updateEpisode(input: VariablesOf<typeof UpdateEpisodeMutation>) {
  const result = await getClient().mutate({
    mutation: UpdateEpisodeMutation,
    variables: input,
  })
  revalidatePath("/episode/" + input.id)
  return result
}

const UpdateEpisodeMutation = graphql(`
mutation updateEpisode($id: String!, $input: UpdateEpisodeInput!) {
  updateEpisode(id: $id, input: $input) {
    ...EpisodeFragment

    }
    }`, [EpisodeFragment]);



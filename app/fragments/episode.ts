import { graphql } from "../graphql";

export const Episode = graphql(`
  fragment EpisodeFragment on EpisodeType {
    id
    createdAt
    lastEdited
    title
    status
    url
    __typename
    transcript {
      transcriptLines {
        speaker
        text
        __typename
      }
    }
    extractedArticle {
      url
      title
      hostname
      text
      sitename
      author
      date
      description
      __typename
    }
  }
`);
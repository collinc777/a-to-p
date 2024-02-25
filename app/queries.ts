import {graphql} from "./graphql";

export const ExtractedArticleFragment = graphql(`
    fragment ExtractedArticleFragment on ExtractedArticleType {
        url
        title
        hostname
        text
        sitename
        author
        date
        description
    }
    `);

export const TranscriptFragment = graphql(`
    fragment TranscriptFragment on TranscriptType {
        transcriptLines {
        speaker 
        text
        }
    }
    `);
  
export const EpisodeFragment = graphql(`
  fragment EpisodeFragment on EpisodeType {
    id
    createdAt
    lastEdited
    title
    status
    url
    transcript {
       ...TranscriptFragment 
    }
    extractedArticle {
        ...ExtractedArticleFragment
    }
  }
`, [TranscriptFragment, ExtractedArticleFragment]);

export const EpisodeQuery = graphql(
    `
      query getEpisode($id: String!) {
        episode(id: $id) {
          ...EpisodeFragment
        }
      }
    `,
    [EpisodeFragment]
  );
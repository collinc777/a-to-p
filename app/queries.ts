import {graphql} from "./graphql";

export const ExtractedArticleFragment = graphql(`
    fragment ExtractedArticleFragment on ExtractedArticleType @_unmask {
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

export const TranscriptLineFragment = graphql(` 
    fragment TranscriptLineFragment on TranscriptLineType @_unmask {
        speaker
        text
    }
    `);


export const TranscriptFragment = graphql(`
    fragment TranscriptFragment on TranscriptType @_unmask {
        transcriptLines {
          ...TranscriptLineFragment
          
        }
    }
    `, [ TranscriptLineFragment ]);
  
export const EpisodeFragment = graphql(`
  fragment EpisodeFragment on EpisodeType @_unmask {
    id
    createdAt
    lastEdited
    title
    status
    url
    transcript {
       ...TranscriptFragment 
    }
    extractedArticlePydantic {
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
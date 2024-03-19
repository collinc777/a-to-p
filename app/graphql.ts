import { initGraphQLTada } from 'gql.tada';
import type { introspection } from './graphql-env.d.ts';

export const graphql = initGraphQLTada<{
  introspection: introspection;
  scalars: {
    UUID: string;
    ID: string;
  }
}>();

export type { FragmentOf, ResultOf, VariablesOf, TadaDocumentNode } from 'gql.tada';
export { readFragment } from 'gql.tada';
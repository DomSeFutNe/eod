import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const authQuery = createApi({
  reducerPath: 'authApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000' }),
  tagTypes: ['Auth'],
  endpoints: (builder) => ({
    signIn: builder.query({
      query: (data: { username: string; password: string }) => ({
        url: '/auth/signin',
        method: 'POST',
        body: data,
      }),
      providesTags: ['Auth'],
    }),
    getUser: builder.query({
      query: () => '/auth/user',
      providesTags: () => [{ type: 'Auth', id: 'USER' }],
    }),
    signOut: builder.mutation({
      query: () => '/auth/signout',
      invalidatesTags: ['Auth'] as const,
    }),
  }),
});

export const { useLazyGetUserQuery, useLazySignInQuery } = authQuery;

export default authQuery;

import { configureStore } from '@reduxjs/toolkit';
import { useDispatch, useSelector } from 'react-redux';

import combinedMiddleware from './combinedMiddleware';
import combinedReducers from './combinedReducers';

const store = configureStore({
  reducer: combinedReducers,
  middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(combinedMiddleware),
  devTools: import.meta.env.NODE_ENV !== 'production',
  preloadedState: {},
});

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch;

// Use throughout your app instead of plain `useDispatch` and `useSelector`
export const useAppDispatch = useDispatch.withTypes<AppDispatch>();
export const useAppSelector = useSelector.withTypes<RootState>();

export default store;

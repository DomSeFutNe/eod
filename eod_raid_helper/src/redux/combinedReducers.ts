import authQuery from './querys/auth';

const combinedReducers = {
  [authQuery.reducerPath]: authQuery.reducer,
};

export default combinedReducers;

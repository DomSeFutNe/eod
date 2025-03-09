import { Middleware } from '@reduxjs/toolkit';
import { createLogger } from 'redux-logger';

import authQuery from './querys/auth';

const middleware: Array<Middleware> = [];

const logger = createLogger({
  collapsed: true,
});

if (import.meta.env.NODE_ENV === 'development') {
  middleware.push(logger);
}

const combinedMiddleware = middleware.concat(authQuery.middleware);

export default combinedMiddleware;

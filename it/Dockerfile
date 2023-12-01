FROM node:16-alpine

WORKDIR /it

ARG NODE_ENV
ENV NODE_ENV ${NODE_ENV:-development}

COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .

RUN yarn tsc

ENTRYPOINT [ "yarn" ]
CMD [ "test" ]

# Stage 1: Build stage
FROM node:20.12.2 as builder

# Set environment variables
ENV HUGO_ENV production
ENV HUGO_VERSION 0.115.4
ENV GO_VERSION 1.22.2

ENV BASE_URL http://localhost
ENV BASE_PORT 8000

# Install Hugo
RUN apt-get update && apt-get install -y curl \
    && curl -LO "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz" \
    && tar -xvf hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz \
    && mv hugo /usr/local/bin/ \
    && rm hugo_extended_${HUGO_VERSION}_Linux-64bit.tar.gz \
    && echo "Hugo ${HUGO_VERSION} installed"

# Install Go
RUN curl -LO "https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz" \
    && tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz \
    && rm go${GO_VERSION}.linux-amd64.tar.gz \
    && echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile \
    && . /etc/profile \
    && echo "Go ${GO_VERSION} installed"

# Export the PATH variable
RUN export PATH=$PATH:/usr/local/go/bin

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install project dependencies
RUN npm install

# Copy project files
COPY . .

# Run project setup and build
RUN PATH=$PATH:/usr/local/go/bin hugo --gc --minify --templateMetrics --templateMetricsHints --forceSyncStatic -e production --minify

# --baseURL=$BASE_URL:$BASE_PORT


# Stage 2: Serve stage
FROM nginx:alpine
# FROM tiangolo/uwsgi-nginx-flask:python3.11

# Copy built site from builder stage
COPY --from=builder /app/public /usr/share/nginx/html
COPY --from=builder /app/nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 8000

# Command to start nginx
CMD ["nginx", "-g", "daemon off;"]

# CMD ["python3", "-m", "http.server", "-d", "/usr/share/nginx/html", "8000"]

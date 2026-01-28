# Stage 1: Build the JavaScript bundle
FROM node:18-slim AS js-builder

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install --legacy-peer-deps

COPY . .
RUN npm run build:js

# Stage 2: Python Runtime
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy Python code and built assets from Stage 1
COPY . .
COPY --from=js-builder /app/dash_tiptap/dash_tiptap.min.js /app/dash_tiptap/
COPY --from=js-builder /app/dash_tiptap/dash_tiptap.min.js.map /app/dash_tiptap/

EXPOSE 8050

CMD ["python", "usage.py"]
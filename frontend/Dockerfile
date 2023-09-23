# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY . .

# Install dependencies
RUN npm install

# Copy the app files to the working directory
COPY . .

# Build the React app
RUN npm run build

# Expose the port the app runs on
EXPOSE 3000

# Command to start the app
CMD ["npm", "start"]

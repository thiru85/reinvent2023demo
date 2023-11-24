# Use the official Node.js 14 image as the base image
FROM node:17

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application files to the working directory
COPY . /app

# Expose the port that the app runs on (change if different in your app)
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]

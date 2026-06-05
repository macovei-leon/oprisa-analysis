# Use the official lightweight Nginx Alpine image
FROM nginx:alpine

# Copy the custom Nginx server configuration
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy the HTML frontend and preprocessed JSON dataset to the Nginx serving folder
COPY index.html /usr/share/nginx/html/
COPY dashboard_data.json /usr/share/nginx/html/

# Expose port 8089 as requested
EXPOSE 8089

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

# Use the official lightweight Nginx Alpine image
FROM nginx:alpine

# Copy the custom Nginx server configuration
COPY default.conf /etc/nginx/conf.d/default.conf

# Copy the HTML frontend and preprocessed JSON dataset to the Nginx serving folder
COPY *.html /usr/share/nginx/html/
COPY assets/ /usr/share/nginx/html/assets/
COPY dashboard_data.json /usr/share/nginx/html/

# Expose port 8057 as requested
EXPOSE 8057

# Start Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

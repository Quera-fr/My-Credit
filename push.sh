# Connect to Heroku
#heroku login

# Heroku container login
heroku container:login

# Create Heroku app
#heroku create api-isen-g2


# Build Image MAC ARM api-iseng2
#docker buildx build --platform linux/amd64 -t api-iseng2  .

# Build Image 
docker build -t api-iseng2  .

# Tag Image to Heroku app
docker tag api-iseng2 registry.heroku.com/api-isen-g2/web

# Push Image to Heroku
docker push registry.heroku.com/api-isen-g2/web

# Release Image to Heroku
heroku container:release web -a api-isen-g2

# Open Heroku app
heroku open -a api-isen-g2

# Logs
heroku logs --tail -a api-isen-g2
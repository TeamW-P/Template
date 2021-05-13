# stops, removes and builds an image for Template
# runs the container on port 5000 
# TODO replace with same port as Dockerfile
# TODO replace "template" with name of the tool

sudo docker container stop template
sudo docker container rm template 

sudo docker build -t template .
sudo docker run -p 5000:5000 -d -t --restart on-failure --network=PipelineNetwork  --name template template 
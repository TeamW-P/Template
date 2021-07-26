# TODO replace "template" with the tool name and pick a port number that is NOT ALREADY IN USE
FROM continuumio/anaconda3

WORKDIR /template

COPY . .

RUN chmod +x boot.sh
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "template", "/bin/bash", "-c"]

EXPOSE 5000

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "template", "./boot.sh"]
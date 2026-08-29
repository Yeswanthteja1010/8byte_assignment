FROM jenkins/jenkins:lts-jdk21

USER root

# Copy Docker CLI from the official Docker CLI image
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/docker

USER jenkins
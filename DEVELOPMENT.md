# rterminal Development

## Releasing new versions through docker images

When a new version of rterminal is ready for production, it is released
as a **multiarch** docker image for portability.

### Prerequisites for development machine

Below steps are required only the first time that a machine is being used
to build rterminal docker images.

#### 1. Create dedicated builder with support for multiple architectures

Docker provides de `buildx` command that allows to use different builder for
images building process. Create an specific builder with multiarch support

```bash
docker buildx create --name hservices --use


# Other useful commands:

# List all available builders
docker buildx ls

# Switch to a specific builder
docker buildx use hservices

# List all docker contexts
docker context ls
```

#### 2. Login to docker registry to push images

In order to allow docker pushes multiarch images to the registry
make sure to be logged in

```bash
docker login

# Enter username and password
```

### Building and releasing image for new version

> Make sure you're using the appropriate docker builder
>   `docker buildx ls`
>   `docker buildx use <builder-name>

With the right builder selected and with docker cli logged in to the docker
registry, run the script to build and push rterminal image.

```bash
# Assuming you're in rterminal's root directory

cd docker
./build_image.sh <new_version>
```

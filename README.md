# Remote terminal

Background services to remotely monitor hosts to a [central](https://github.com/giobyte8/central)  service instance.

## Features

- Setup conditional tasks to be executed during boot time
- Report restart/boot events to central
- Report host status constantly to central

## Deployment

### Environment setup

Prepare a `.env` file with your own values

```bash
cp env.template .env
vim .env

# Enter your own values
```

> Pay attention to comments in .env file about how to escape '$' signs
> in hashed passwords

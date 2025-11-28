# Remote terminal

Background services to remotely monitor hosts throught a
[central](https://github.com/giobyte8/central) service instance.

## Features

- Report restart/boot events to central
- Report host status constantly to central
- Setup tasks to be executed during boot time

## Deployment

### Environment setup

Prepare a `.env` file with your own values
```bash
cp env.template .env
vim .env

# Enter your own values
```

Prepare python virtual env
...

### Running tasks

Run tasks manually
```shell
python rterminal/tasks/boot.py
python rterminal/tasks/host_status_update.py

# Make sure virtual env is active before running tasks
```

Run through systemd
...

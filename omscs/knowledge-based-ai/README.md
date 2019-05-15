Before we get into this, let me just say that all the hard work here was done by the KBAI teaching team and [Alex Peattie](https://github.com/alexpeattie). I just threw Docker around it a fixed a few bugs.

# KBAI RPM Runner
Alright, what is this thing? Well, you need to write an AI agent that solves RPM problems, right? And you downloaded the starter code from the class GitHub repo. Great. Now... how do you run this thing again? I'll tell you how, fell classmate!

```bash
docker-compose up
```

Then go to [http://localhost](http://localhost). That's it. That'll build the docker image for you and launch a container from it. Now you can make edits to Agent.py and see the results in realtime. No messing with local python installations and package versions. Just good old Docker to the rescue.

Already started on the project? No worries! Just add everything in this repo to the root folder of your project and get going!

## Configuration
You have the following knobs to tweak in docker-compose.yml:
- Listening port: change the port forwarded from the host, because the black market art store running on your machine is using ports 80 and 81.
- Polling: on Windows machines, you have to use polling to monitor for file changes. If that doesn't apply to you, just remove the POLLING environment variable.

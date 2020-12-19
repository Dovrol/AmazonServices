from fabric import task


def kill(c):
    result = c.run(f"ps -al")
    lines = result.stdout.split('\n')
    for line in lines:
        if ("python" in line):
            pid = line.split(' ')[9]
            c.run(f"kill {pid}")

def pull(c):
    c.run("cd AmazonServices && git pull")

def start(c):
    c.run("cd AmazonServices && screen -dm venv/bin/python index.py")

@task
def pull_and_restart(c):
    kill(c)
    pull(c)
    start(c)


    




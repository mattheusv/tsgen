import os
import git


def compute_version():
    repo = git.Repo(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    tags = sorted(repo.tags, key=lambda t: t.tag.tagged_date)
    if len(tags) == 0:
        with open(os.path.join(os.path.dirname(__file__), "VERSION"), "w") as f:
            f.write("0.1.0")
            return
    with open(os.path.join(os.path.dirname(__file__), "VERSION"), "w") as f:
        f.write(tags[-1].name)


VERSION = compute_version()

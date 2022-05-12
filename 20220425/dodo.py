DOIT_CONFIG = {'default_tasks': ['babel', 'test']}

def task_babel():
    """Update and compile translation"""
    return {
        "actions": ["pybabel update -l ru -i po/task.pot -d po",
                    "pybabel compile -d po"],
        "file_dep": ["po/task.pot"]
    }

def task_test():
    """Run tests"""
    return {
        "actions": ["python3 -m unittest"]
    }

def task_cleanup():
    """Remove all"""
    return {
        "actions": ["rm -rf *.po"]
    }
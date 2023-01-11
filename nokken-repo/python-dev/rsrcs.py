import dotenv
import os


def get_env_var(filename, varname):
    cur_dir = __file__.rpartition('\\')[0]
    env_path = f"{cur_dir}\\{filename}"
    dotenv.load_dotenv(env_path)
    return os.getenv(varname)


test = get_env_var('test.env', 'test_var')

print(test)


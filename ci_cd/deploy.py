from fabric import Connection, task

# Данные сервера
HOST = "192.168.1.105"
USER = "alex"
PROJECT_DIR = "~/rpi_sms_receiver"
def deploy():
    """Деплой проекта на сервер"""
    with Connection(host=HOST, user=USER) as c:
        print("🚀 Обновляем код...")
        result = c.run(f"cd {PROJECT_DIR} && git pull")
        print(f'{result = }')
        try:

            c.run("PID=$(ps -xa | grep \"rpi_sms_receiver\" | grep -v \"grep\" | awk '{print $1}' | head -n 1) && [ -n \"$PID\" ] && kill \"$PID\"")
            print(f'{result = }')
        except Exception as e:
            print(e)

        result = c.run(f"cd {PROJECT_DIR} && nohup ~/rpi_sms_receiver/.venv/bin/python -m src.main", disown=True)
        print(f'{result = }')



if __name__ == '__main__':
    deploy()

from Client import Client


def get_content(file_name):
    watch_content = Client()
    watch_content.get_video(file_name)


if __name__ == '__main__':
    get_content('some_content')

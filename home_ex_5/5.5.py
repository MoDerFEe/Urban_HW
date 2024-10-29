import time


class User:
    database = {}

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        User.database[self.nickname] = [self.password, self.age]


class Video:
    database = {}

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.database[self.title] = [self.duration, self.time_now, self.adult_mode]


class UrTube:
    def __init__(self, current_user=None):
        self.users = User.database
        self.videos = Video.database
        self.current_user = current_user

    def log_in(self, nickname, password):
        self.users = User.database
        try:
            if self.users.get(nickname)[0] == hash(password):
                self.current_user = nickname
            else:
                print('Введен неверный пароль')
        except:
            print('Такого пользователя не существует!')

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            User(nickname, password, age)
        self.log_in(nickname, password)

    def logout(self):
        self.current_user = None

    def add(self, *args):
        self.video = Video.database

    def get_videos(self, word):
        mas = []
        for i in self.video.keys():
            if word.lower() in i.lower():
                mas.append(i)
        return mas

    def watch_video(self, title):
        try:
            if self.current_user == None:
                print('Войдите в аккаунт, чтобы смотреть видео')
            elif self.videos.get(title)[2] == True and self.users.get(self.current_user)[1] < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                for i in range(self.videos.get(title)[0]):
                    print(i + 1, end=' ')
                    time.sleep(1)
                    if i == self.videos.get(title)[0] - 1:
                        print(f'конец')

        except:
            False


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
